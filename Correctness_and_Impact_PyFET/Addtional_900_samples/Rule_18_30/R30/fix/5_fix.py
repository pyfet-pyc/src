def show_keyboard(
    self,
    system_keyboard,
    softinput_mode,
    input_type,
    keyboard_suggestions=True,
):
    if SDL_IsTextInputActive():
        return
    cdef SDL_Rect *rect = <SDL_Rect *>PyMem_Malloc(sizeof(SDL_Rect))
    if not rect:
        raise MemoryError('Memory error in rect allocation')
    try:
        if platform == 'android':
            # This could probably be safely done on every platform
            # (and should behave correctly with e.g. the windows
            # software keyboard), but this hasn't been tested

            wx, wy = self.window_size

            # Note Android's coordinate system has y=0 at the top
            # of the screen

            if softinput_mode == 'below_target':
                target = system_keyboard.target
                rect.y = max(
                    0, wy - target.to_window(0, target.top)[1]
                ) if target else 0
                rect.x = max(
                    0, target.to_window(target.x, 0)[0]
                ) if target else 0
                rect.w = max(0, target.width) if target else 0
                rect.h = max(0, target.height) if target else 0
                SDL_SetTextInputRect(rect)
            elif softinput_mode == 'pan':
                # tell Android the TextInput is at the screen
                # bottom, so that it always pans
                rect.y = wy - 5
                rect.x = 0
                rect.w = wx
                rect.h = 5
                SDL_SetTextInputRect(rect)
            else:
                # Supporting 'resize' needs to call the Android
                # API to set ADJUST_RESIZE mode, and change the
                # java bootstrap to a different root Layout.
                rect.y = 0
                rect.x = 0
                rect.w = 10
                rect.h = 1
                SDL_SetTextInputRect(rect)

            """
            Android input type selection.
            Based on input_type and keyboard_suggestions arguments, set the
            keyboard type to be shown. Note that text suggestions will only
            work when input_type is "text" or a text variation.
            """

            from android import mActivity

            # InputType definitions, from Android documentation

            TYPE_CLASS_DATETIME = 4
            TYPE_CLASS_NUMBER = 2
            TYPE_CLASS_PHONE = 3
            TYPE_CLASS_TEXT = 1
            TYPE_CLASS_NULL = 0

            TYPE_TEXT_VARIATION_EMAIL_ADDRESS = 32
            TYPE_TEXT_VARIATION_URI = 16
            TYPE_TEXT_VARIATION_POSTAL_ADDRESS = 112

            TYPE_TEXT_FLAG_NO_SUGGESTIONS = 524288

            input_type_value = {
                            "null": TYPE_CLASS_NULL,
                            "text": TYPE_CLASS_TEXT,
                            "number": TYPE_CLASS_NUMBER,
                            "url":
                            TYPE_CLASS_TEXT |
                            TYPE_TEXT_VARIATION_URI,
                            "mail":
                            TYPE_CLASS_TEXT |
                            TYPE_TEXT_VARIATION_EMAIL_ADDRESS,
                            "datetime": TYPE_CLASS_DATETIME,
                            "tel": TYPE_CLASS_PHONE,
                            "address":
                            TYPE_CLASS_TEXT |
                            TYPE_TEXT_VARIATION_POSTAL_ADDRESS
                            }.get(input_type, TYPE_CLASS_TEXT)

            text_keyboards = {"text", "url", "mail", "address"}

            if not keyboard_suggestions and input_type in text_keyboards:
                """
                Looks like some (major) device vendors and keyboards are de-facto ignoring this flag,
                so we can't really rely on this one to disable suggestions.
                """
                input_type_value |= TYPE_TEXT_FLAG_NO_SUGGESTIONS

            mActivity.changeKeyboard(input_type_value)

        SDL_StartTextInput()
    finally:
        PyMem_Free(<void *>rect)
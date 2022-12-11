async def do_keyboard_key(
        self, key, modifiers=(), duration=.05, num_press=1):
    from kivy.core.window import Window
    if key == ' ':
        key = 'spacebar'
    key_lower = key.lower()
    key_code = Window._system_keyboard.string_to_keycode(key_lower)

    known_modifiers = {'shift', 'alt', 'ctrl', 'meta'}
    if set(modifiers) - known_modifiers:
        raise ValueError('Unknown modifiers "{}"'.
                            format(set(modifiers) - known_modifiers))

    special_keys = {
        27: 'escape',
        9: 'tab',
        8: 'backspace',
        13: 'enter',
        127: 'del',
        271: 'enter',
        273: 'up',
        274: 'down',
        275: 'right',
        276: 'left',
        278: 'home',
        279: 'end',
        280: 'pgup',
        281: 'pgdown',
        300: 'numlock',
        301: 'capslock',
        145: 'screenlock',
    }

    text = None
    try:
        text = chr(key_code)
        if key_lower != key:
            text = key
    except ValueError:
        pass

    dt = duration / num_press
    for i in range(num_press):
        await self.async_sleep(dt)

        Window.dispatch('on_key_down', key_code, 0, text, modifiers)
        if (key not in known_modifiers and
                key_code not in special_keys and
                not (known_modifiers & set(modifiers))):
            Window.dispatch('on_textinput', text)

        await self.wait_clock_frames(1)
        yield 'down', (key, key_code, 0, text, modifiers)

    Window.dispatch('on_key_up', key_code, 0)
    await self.wait_clock_frames(1)
    yield 'up', (key, key_code, 0, text, modifiers)

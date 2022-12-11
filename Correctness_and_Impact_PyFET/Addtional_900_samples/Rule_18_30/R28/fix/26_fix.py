def tearDown(self, *args, **kwargs):
    self.etype = None
    self.motion_event = None
    self.touch_event = None
    from kivy.base import EventLoop
    win = EventLoop.window
    win.mouse_pos = self.old_mouse_pos
    win.rotation = self.old_rotation
    win.old_system_size = self.old_system_size
    self.old_mouse_pos = None
    self.old_rotation = None
    self.old_system_size = None
    if self.button_widget:
        win.remove_widget(self.button_widget)
        self.button_widget = None
    mouse = self.mouse
    mouse.stop()
    EventLoop.remove_input_provider(mouse)
    self.mouse = None
    win.funbind('on_motion', self.on_motion)
    # Restore method `on_close` to window
    win.on_close = self.old_on_close
    self.old_on_close = None
    super().tearDown(*args, **kwargs)
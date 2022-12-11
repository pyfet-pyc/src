def __init__(self, app=None, *args, **kwargs):
    if app is None:
        app = App()
    EventLoop.safe = Event()
    self.safe = EventLoop.safe
    self.safe.set()
    EventLoop.confirmed = Event()
    self.confirmed = EventLoop.confirmed
    self.app = app

    def startApp(app=app, *args, **kwargs):
        app.run(*args, **kwargs)

    self.thread = Thread(target=startApp, *args, **kwargs)
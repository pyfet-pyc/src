def __init__(self, *args, **kwargs):
    """
    Create & set window variables.
    """
    tk.Tk.__init__(self, *args, **kwargs)

    self.chatbot = ChatBot(
        "GUI Bot",
        storage_adapter="chatterbot.storage.SQLStorageAdapter",
        logic_adapters=[
            "chatterbot.logic.BestMatch"
        ],
        database_uri="sqlite:///database.sqlite3"
    )

    self.title("Chatterbot")

    self.initialize()
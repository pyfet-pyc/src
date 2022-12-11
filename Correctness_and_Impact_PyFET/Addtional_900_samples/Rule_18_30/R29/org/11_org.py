    def __init__(self):
        self.phones = []
        self.features = ["Brand", "Model Name", "Model Image"]
        self.temp1 = []
        self.phones_brands = []
        self.url = "https://www.phonearena.com/phones/"  # GSMArena website url
        # Folder name on which files going to save.
        self.new_folder_name = "GSMArenaDataset"
        # It create the absolute path of the GSMArenaDataset folder.
        self.absolute_path = os.getcwd().strip() + "/" + self.new_folder_name

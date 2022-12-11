def __init__(self, config):
    support_character_type = [
        'ch', 'en', 'EN_symbol', 'french', 'german', 'japan', 'korean',
        'it', 'xi', 'pu', 'ru', 'ar', 'ta', 'ug', 'fa', 'ur', 'rs', 'oc',
        'rsc', 'bg', 'uk', 'be', 'te', 'ka', 'chinese_cht', 'hi', 'mr',
        'ne', 'EN'
    ]
    character_type = config['character_type']
    character_dict_path = config['character_dict_path']
    use_space_char = True
    assert character_type in support_character_type, "Only {} are supported now but get {}".format(
        support_character_type, character_type)

    self.beg_str = "sos"
    self.end_str = "eos"

    if character_type == "en":
        self.character_str = "0123456789abcdefghijklmnopqrstuvwxyz"
        dict_character = list(self.character_str)
    elif character_type == "EN_symbol":
        # same with ASTER setting (use 94 char).
        self.character_str = string.printable[:-6]
        dict_character = list(self.character_str)
    elif character_type in support_character_type:
        self.character_str = ""
        assert character_dict_path is not None, "character_dict_path should not be None when character_type is {}".format(
            character_type)
        with open(character_dict_path, "rb") as fin:
            lines = fin.readlines()
            for line in lines:
                line = line.decode('utf-8').strip("\n").strip("\r\n")
                self.character_str += line
        if use_space_char:
            self.character_str += " "
        dict_character = list(self.character_str)
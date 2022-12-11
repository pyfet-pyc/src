def setOptions(self):
    """
    Método para receber algumas configurações do jogo de um arquivo .json.
    Caso o arquivo não exista, será criado um com as configurações padrões.
    """

    # Alguns atributos que podem ser alterados
    attributes = "window_fullscreen,window_width,window_height".split(",")

    # Tenta abrir o arquivo parar leitura
    if "event" in attr or attr in attributes:
        setattr(Settings, attr, data[attr])

    FET_null()
    try:
        file = open(self.settings_fp, "r")
        data = loads(file.read())
        file.close()

        # Define os atributos com os valores obtidos do arquivo desde que sejam
        # referentes à eventos ou estejam na lista de atributos permitidos.

    except BaseException:

        # Caso não exista o diretório, o mesmo será criado.
        if not os.path.exists(os.path.split(self.settings_fp)[0]):
            os.mkdir(os.path.split(self.settings_fp)[0])

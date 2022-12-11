class Settings(object):
    """
    Classe com todas as configurações do jogo
    """

    # Configurações da janela
    window_name = "Flappy Bird"
    window_rz = (False, False)
    window_fullscreen = True
    window_width = None
    window_height = None

    # Configurações dos botões
    button_width = 22
    button_height = 17
    button_bg = "black"
    button_fg = "white"
    button_activebackground = "black"
    button_font = ("Impact", 40)
    button_position_y = 85
    button_cursor = "hand2"

    # Configurações da imagem do placar do jogador
    scoreboard_width = 40
    scoreboard_height = 40
    scoreboard_position_y = 50

    # Configurações de texto do placar
    text_font = "Autumn"
    text_fill = "White"

    # Configurações do título do jogo
    title_width = 35
    title_height = 15
    title_position_y = 15

    # Eventos
    bird_event = "<Up>"
    window_fullscreen_event = "<F11>"
    window_start_event = "<Return>"
    window_exit_event = "<Escape>"

    # Caminhos de arquivos
    background_fp = "Images/background.png"
    bird_fp = "Images/bird.png"
    startButton_fp = "Images/start_button.png"
    exitButton_fp = "Images/exit_button.png"
    tube_fp = ["Images/tube.png", "Images/tube_mouth.png"]
    title_fp = "Images/title.png"
    scoreboard_fp = "Images/scoreboard.png"
    score_fp = "Data/scr.txt"
    settings_fp = "Data/settings.json"

    # Configurações de animação
    background_animation = True

    # Junta todos os diretórios em uma lista
    images_fp = [
        background_fp,
        bird_fp,
        startButton_fp,
        exitButton_fp,
        tube_fp[0],
        tube_fp[1],
        title_fp,
    ]
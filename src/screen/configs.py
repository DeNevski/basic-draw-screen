from pygame import display

display.init()

# Dimensões
WIDTH = display.get_desktop_sizes()[0][0]
HEIGHT = display.get_desktop_sizes()[0][1] - 50

# Título
TITLE = display.set_caption('Drawing Screen')

# Cor de fundo
BACKGROUND_COLOR = (240,240,240)

from src.screen.surface import Screen
from src.functions.drawing import Drawing
from src.screen.toolbar import Toolbar

def main():
    screen = Screen()
    drawing = Drawing(screen)
    toolbar = Toolbar(screen, drawing)

    while True:
        screen.close_window()
        screen.clock()

        toolbar.background()

        drawing.draw()
        drawing.erase()

        screen.update()

if __name__ == "__main__":
    main()

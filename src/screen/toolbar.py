import pygame

class Toolbar:
    def __init__(self, screen, drawing):
        self.screen = screen
        self.drawing = drawing
        self.toolbar_height = self.screen.get_h() / 8
        self.background_color = (220,220,220)

    def background(self) -> None:
        """
        Este método desenha um retângulo no topo da superfície para representar o fundo, 
        usando a cor de fundo definida. Também chama métodos para exibir o menu de cores,
        o menu de tamanhos e o texto de comandos.
        """

        pygame.draw.rect(self.screen.get_surface(), self.background_color, (0, 0, self.screen.get_w(), self.toolbar_height))

        self.colors_menu()
        self.sizes_menu()
        self.command_text()

    def sizes_menu(self) -> None:
        """
        Desenha o menu de seleção de tamanhos de pincel na interface.
        As opções de tamanho e suas respectivas formas são armazenadas em um dicionário.
        """

        height = self.toolbar_height / 2

        shapes = {
        30 : pygame.draw.circle(self.screen.get_surface(), 'black', (self.screen.get_w() * 0.02, height), 30),
        20 : pygame.draw.circle(self.screen.get_surface(), 'black', (self.screen.get_w() * 0.065, height), 20),
        10 : pygame.draw.circle(self.screen.get_surface(), 'black', (self.screen.get_w() * 0.095, height), 10),
        5 : pygame.draw.circle(self.screen.get_surface(), 'black', (self.screen.get_w() * 0.115, height), 5)
        }

        self._size_function(shapes)

    def _size_function(self, shapes_dict: dict) -> None:
        """
        Processa a interação do mouse com as opções de tamanho de pincel.

        Args:
            shapes_dict (dict): Um dicionário contendo os tamanhos dos pincéis como chaves e as formas desenhadas como valores.
        """

        mouse_pos = pygame.mouse.get_pos()

        for i in shapes_dict.items():
            if pygame.mouse.get_pressed(num_buttons=3)[0]:

                if pygame.Rect.collidepoint(i[1], mouse_pos[0], mouse_pos[1]):
                    self.drawing.update_size(i[0])

    def colors_menu(self) -> None:
        """
        Desenha o menu de seleção de cores na interface. As cores são armazenadas em um dicionário, sendo as chaves o "código" da cor
        e os valores formas com suas respectivas cores.
        """

        size_w = self.screen.get_w() / 60
        size_h = self.screen.get_h() / 30

        top_position = self.toolbar_height / 5
        low_position = self.toolbar_height / 2

        # Colunas da direita para a esquerda
        colors = {
        # column 1
        'White' : pygame.draw.rect(self.screen.get_surface(), 'White', (self.screen.get_w() * 0.98, top_position, size_w, size_h)),
        'Black' : pygame.draw.rect(self.screen.get_surface(), 'Black', (self.screen.get_w() * 0.98, low_position, size_w, size_h)),
        # column 2
        'Gray' : pygame.draw.rect(self.screen.get_surface(), 'Gray', (self.screen.get_w() * 0.96, top_position, size_w, size_h)),
        'SaddleBrown' : pygame.draw.rect(self.screen.get_surface(), 'SaddleBrown', (self.screen.get_w() * 0.96, low_position, size_w, size_h)),
        # column 3
        'Red' : pygame.draw.rect(self.screen.get_surface(), 'Red', (self.screen.get_w() * 0.94, top_position, size_w, size_h)),
        'Crimson' : pygame.draw.rect(self.screen.get_surface(), 'Crimson', (self.screen.get_w() * 0.94, low_position, size_w, size_h)),
        # column 4
        'Pink' : pygame.draw.rect(self.screen.get_surface(), 'Pink', (self.screen.get_w() * 0.92, top_position, size_w, size_h)),
        'Magenta' : pygame.draw.rect(self.screen.get_surface(), 'Magenta', (self.screen.get_w() * 0.92, low_position, size_w, size_h)),
        # column 5
        'Purple' : pygame.draw.rect(self.screen.get_surface(), 'Purple', (self.screen.get_w() * 0.90, top_position, size_w, size_h)),
        'Indigo' : pygame.draw.rect(self.screen.get_surface(), 'Indigo', (self.screen.get_w() * 0.90, low_position, size_w, size_h)),
        # column 6
        'Blue' : pygame.draw.rect(self.screen.get_surface(), 'Blue', (self.screen.get_w() * 0.88, top_position, size_w, size_h)),
        'DarkBlue' : pygame.draw.rect(self.screen.get_surface(), 'DarkBlue', (self.screen.get_w() * 0.88, low_position, size_w, size_h)),
        # column 7
        'Cyan' : pygame.draw.rect(self.screen.get_surface(), 'Cyan', (self.screen.get_w() * 0.86, top_position, size_w, size_h)),
        'DarkCyan' : pygame.draw.rect(self.screen.get_surface(), 'DarkCyan', (self.screen.get_w() * 0.86, low_position, size_w, size_h)),
        # column 8
        'ForestGreen' : pygame.draw.rect(self.screen.get_surface(), 'ForestGreen', (self.screen.get_w() * 0.84, top_position, size_w, size_h)),
        'DarkGreen' : pygame.draw.rect(self.screen.get_surface(), 'DarkGreen', (self.screen.get_w() * 0.84, low_position, size_w, size_h)),
        # column 9
        'Lime' : pygame.draw.rect(self.screen.get_surface(), 'Lime', (self.screen.get_w() * 0.82, top_position, size_w, size_h)),
        'Yellow' : pygame.draw.rect(self.screen.get_surface(), 'Yellow', (self.screen.get_w() * 0.82, low_position, size_w, size_h)),
        # column 10
        'Orange' : pygame.draw.rect(self.screen.get_surface(), 'Orange', (self.screen.get_w() * 0.80, top_position, size_w, size_h)),
        'DarkOrange' : pygame.draw.rect(self.screen.get_surface(), 'DarkOrange', (self.screen.get_w() * 0.80, low_position, size_w, size_h))
        }

        self.color_function(colors)

    def color_function(self, color_dict: dict) -> None:
        """
        Processa a interação do mouse com as opções de cores na interface.

        Args:
            color_dict (dict): Um dicionário onde as chaves são os nomes das cores 
            (strings) e os valores são os retângulos desenhados para representar essas cores na interface.
        """

        mouse_pos = pygame.mouse.get_pos()

        for i in color_dict.items():
            if pygame.mouse.get_pressed(num_buttons=3)[0]:

                if pygame.Rect.collidepoint(i[1], mouse_pos[0], mouse_pos[1]):
                    self.drawing.update_color(i[0])

    def command_text(self) -> None:
        """
        Escreve os comandos na toolbar.
        """
        
        height = self.toolbar_height / 2

        pygame.font.init()

        left_button = 'Left mouse button to draw'
        right_button = 'Right mouse button to erase'

        font = pygame.font.SysFont('arial', 20)

        left_mouse_text = font.render(left_button, True, 'white')
        right_mouse_text = font.render(right_button, True, 'white')

        self.screen.get_surface().blit(left_mouse_text, (self.screen.get_w() * 0.43, height * 0.5))
        self.screen.get_surface().blit(right_mouse_text, (self.screen.get_w() * 0.43, height * 1.2))

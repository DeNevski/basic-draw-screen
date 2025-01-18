import pygame
import math
from src.screen.configs import BACKGROUND_COLOR

class Drawing:
    def __init__(self, screen):
        self.screen = screen
        self.size = 5
        self.color = 'black'
        self.last_pos_draw = None
        self.last_pos_erase = None

    def draw(self) -> None:
        """
        Desenha um círculo na posição do mouse com a cor e o tamanho selecionados.
        """

        mouse_pos = pygame.mouse.get_pos()

        if pygame.mouse.get_pressed(num_buttons=3)[0]:
            if self.last_pos_draw:
                # Calcula a distância entre a posição atual do mouse e a anterior
                distance = math.hypot(mouse_pos[0] - self.last_pos_draw[0], mouse_pos[1] - self.last_pos_draw[1])

                step = 2
                for i in range(0, int(distance), step):
                    x = self.last_pos_draw[0] + (mouse_pos[0] - self.last_pos_draw[0]) * i / distance
                    y = self.last_pos_draw[1] + (mouse_pos[1] - self.last_pos_draw[1]) * i / distance
                    
                    pygame.draw.circle(self.screen.get_surface(), self.color, (int(x), int(y)), self.size)
            
            self.last_pos_draw = mouse_pos
        else:
            self.last_pos_draw = None

    def erase(self) -> None:
        """
        Apaga uma área na tela na posição do mouse com o tamanho selecionado.
        """

        mouse_pos = pygame.mouse.get_pos()

        if pygame.mouse.get_pressed(num_buttons=3)[2]:
            if self.last_pos_erase:
                distance = math.hypot(mouse_pos[0] - self.last_pos_erase[0], mouse_pos[1] - self.last_pos_erase[1])

                step = 2
                for i in range(0, int(distance), step):
                    x = self.last_pos_erase[0] + (mouse_pos[0] - self.last_pos_erase[0]) * i / distance
                    y = self.last_pos_erase[1] + (mouse_pos[1] - self.last_pos_erase[1]) * i / distance

                    pygame.draw.circle(self.screen.get_surface(), BACKGROUND_COLOR, (int(x), int(y)), self.size)
            
            self.last_pos_erase = mouse_pos
        else:
            self.last_pos_erase = None

    def update_size(self, size: int) -> None:
        """
        Atualiza o tamanho do pincel.

        Args:
            size (int): O novo tamanho do pincel, que será usado para desenhar ou apagar.
        """

        self.size = size

    def update_color(self, color: str) -> None:
        """
        Atualiza a cor do pincel.

        Args:
            color (str): A nova cor do pincel.
        """
        
        self.color = color

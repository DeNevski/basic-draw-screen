import pygame
from pygame import Surface
from src.screen.configs import WIDTH, HEIGHT, BACKGROUND_COLOR
import sys

class Screen:
    def __init__(self) -> None:
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.time = pygame.time.Clock()
        self.background_color = self.screen.fill(BACKGROUND_COLOR)

    def close_window(self) -> None:
        """
        Este método percorre a fila de eventos do Pygame para verificar se há
        eventos de saída.
        """

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                pygame.quit()

    def update(self) -> None:
        """
        Atualiza a tela.
        """
        pygame.display.flip()

    def clock(self) -> None:
        """
        Controla a taxa de quadros por segundo (FPS).
        """
        
        self.time.tick(60)

    def get_surface(self) -> Surface:
        """
        Retorna a superfície da tela (screen) usada para renderizar o display.

        Returns:
            pygame.Surface: A superfície da tela para renderização.
        """

        return self.screen
    
    def get_w(self) -> int:
        """
        Retorna a largura da superfície da tela.

        Returns:
            int: A largura da tela em pixels.
        """

        return self.screen.get_width()
    
    def get_h(self) -> int:
        """
        Retorna a altura da superfície da tela.

        Returns:
            int: A altura da tela em pixels.
        """

        return self.screen.get_height()

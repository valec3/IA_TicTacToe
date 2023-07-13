# Copyright (c) 2023 Valec3
#
# Este archivo es parte del programa TIC TAC TOE.
# Juego de TIC TAC TOE  con Minimax
#
# Derechos de autor (c) 2023 Valec3
# Todos los derechos reservados.

import pygame
class Boton:
    """
    Clase que representa un botón en la pantalla.
    """

    def __init__(self, x: int, y: int, imagen: pygame.Surface,escala:int) -> None:
        """
        Constructor de la clase Boton.

        :param x: La posición en x del botón en la pantalla.
        :type x: int
        :param y: La posición en y del botón en la pantalla.
        :type y: int
        :param imagen: La imagen del botón.
        :type imagen: pygame.Surface
        """
        ancho = imagen.get_width()
        alto = imagen.get_height()
        self.imagen = pygame.transform.scale(imagen,(int(ancho*escala),int(alto*escala)))
        self.rect = self.imagen.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
    def dibujar(self, ventana: pygame.Surface) -> None:
        """
        Dibuja el botón en la ventana especificada.

        :param ventana: La superficie donde se dibujará el botón.
        :type ventana: pygame.Surface
        """
        ventana.blit(self.imagen, (self.rect.x, self.rect.y))
    
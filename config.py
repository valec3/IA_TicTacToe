import pygame

class Configuraciones:
    bg_image_load = pygame.image.load('img/bg.jpg')
    def __init__(self) -> None:
        # Screen settings
        self.ventana_width = 1200
        self.ventana_height = 800
        self.bg_imagen=pygame.transform.scale(self.bg_image_load,(self.ventana_width,self.ventana_height))
        self.bg_color=(28,180,156)
        
        # Caracteristicas Tablero
        self.sqr_size=self.ventana_height//4
        self.board_sz_w=self.sqr_size*3
        self.board_lx=(self.ventana_width-self.board_sz_w)/2
        self.board_dx=self.board_lx+self.board_sz_w
        self.board_ty=(self.ventana_height-self.board_sz_w)/2
        self.board_by=self.board_ty + self.board_sz_w
        self.board_color=(0,0,0)
        
        # 1200 - 900 = 300 / 2 
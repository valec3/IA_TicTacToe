class Ia_logic:
    """Clase para manejar la logica de la IA del juego
    """
    def __init__(self,player=2,level = 0):
        self.player=player
        self.level = level
    def move_rnd(self,board):
        cuad_vacio = board.get_empty()
    def eval(self,main_board):
        """Jugar segun el modo de dificultad

        Args:
            main_board (_type_): _description_
        """
        if self.level == 0:
            # Modo aleatorio 
            pass
        else:
            # minimax
            pass
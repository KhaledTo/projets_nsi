from const import ROWS, COLS
from square import Square


class Board:
    """ Cette classe permet de definir l'echiquier
    """
    def __init__(self):
        self.squares = [[None] * ROWS for col in range(COLS)]
        self._create()

    def _create(self):
        """ Methode privee pour ajouter les carres a l'echiquier
        """
        for row in ROWS:
            for col in COLS:
                self.squares[row][col] = Square(row, col)

    def _add_pieces(self, color):
        """ Methode privee pour ajouter des pieces

        Args:
            color (str): blanc ou noir
        """
        self.squares = [[]]

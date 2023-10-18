import math

class Piece:
    def __init__(self, name, color, value, texture, texture_rect=None):

        if color == 'white':
            self.dir = -1
        else:
            self.dir = 1
        # Utilisé par l'IA
        self.value = value * self.dir
        self.name = name
        self.color = color
        self.value = value
        self.texture = texture
        self.texture_rect = texture_rect
        self.set_texture()

    def set_texture(self):
        pass

class Pawn(Piece):
    def __init__(self, color):
        super().__init__('pawn', color, 1.0)


class Knight(Piece):
    def __init__(self, color):
        super().__init__('knight', color, 3.0)

class Bishop(Piece):
    def __init__(self, color):
        super().__init__('bishop', color, 3.1)

class Rook(Piece):
    def __init__(self, color):
        super().__init__('rook', color, 5.0)

class Queen(Piece):
    def __init__(self, color):
        super().__init__('bishop', color, 3.1)

class King(Piece):
    def __init__(self, color):
        super().__init__('king', color, math.inf)
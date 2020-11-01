from pgzero.actor import Actor 

class body(Actor):
    def __init__ (self, x, y, obrot, obraz):
        Actor.__init__(self, obraz)
        self.pos = (x, y)
        self.x = x
        self.y = y
        self.obraz = obraz
        self.size = (10, 10)
        self.obrot = obrot

    
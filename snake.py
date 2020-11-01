from body import body
from pgzero.clock import clock

class snake:
    def __init__(self, element, x, y, kierunek):
        self.snake_body = []
        self.speed_x = 1
        self.speed_y = 0
        self.pre = 0.2

        ex = x
        ey = y
        for i in range(0, element + 3) :
            if i == 0:
                obraz = 'glowa'
            else:
                obraz = 'ogon'
                if kierunek == 'lewo':
                    self.krweza = 'prawo'
                    ex -= 30

                elif kierunek == 'prawo':
                    ex += 30
                    self.krweza = 'lewo'

                elif kierunek == 'gora':
                    ey -= 30
                    self.krweza = 'dol'

                elif kierunek == 'dol':
                    ey += 30
                    self.krweza = 'gora'
            
                self.last_move = self.krweza

            self.snake_body.append(body(ex, ey, 'prawo', obraz))
        
    def rusz_sie(self):
        clock.schedule_interval(self.move, self.pre)
    
    def stop(self):
        clock.unschedule(self.move)

    def spowolnienie(self):
        clock.unschedule(self.move)
        self.pre -= 0.005
        clock.schedule_interval(self.move, self.pre)
            
    def draw(self):
        for r in self.snake_body[::-1]:
            r.draw()

    def update(self):
        pass
    
    def move(self):
        px = self.snake_body[0].x
        py = self.snake_body[0].y

        if self.krweza == 'lewo':
            px -= 30

        elif self.krweza == 'prawo':
            px += 30

        elif self.krweza == 'gora':
            py -= 30
        
        elif self.krweza == 'dol':
            py += 30

        for z in self.snake_body:
            tx = z.x
            ty = z.y
            
            z.x = px
            z.y = py

            px = tx
            py = ty   

        self.last_move = self.krweza

    def czy_gryze(self):
        gx = None
        gy = None

        for z in self.snake_body:
            if gx == None:
                gx = z.x
                gy = z.y
            else:
                if gx == z.x and gy == z.y:
                    return True
        
        return False
     

    def prawo(self):
        if self.last_move == 'lewo':
          return  
        self.krweza = 'prawo'
    
    def lewo(self):
        if self.last_move == 'prawo':
            return  
        self.krweza = 'lewo'

    def gora(self):
        if self.last_move == 'dol':
          return  
        self.krweza = 'gora'

    def dol(self):
        if self.last_move == 'gora':
          return  
        self.krweza = 'dol'

    def poz_glowy(self):
        glowa = self.snake_body[0]
        return (
            glowa.left, glowa.top, glowa.right, glowa.bottom
        )

    def istniejesz(self, x, y):

        for z in self.snake_body:
            if z.x == x and z.y == y:
                
                return True


        return False
        

    def zwieksz_sie(self):
        last = self.snake_body[-1]

        self.snake_body.append(body(last.x, last.y, 'prawo', last.image))


from pgzero.actor import Actor 
from pgzero.keyboard import keyboard
from pgzero.loaders import sounds  
from pgzero.clock import clock
from ludzik import ludzik
from pgzero.rect import Rect
from snake import snake
import random


class game:

#   KOLORY:
    color_ramka = (18, 122, 2)
    pole_gry_jasne = (114, 214, 89)
    kwadraty_planszy = (145, 252, 78)
    litery = (192, 192, 192)
    tlozmiennej = (255, 128, 0)

#   Zmienne:    
    punkty = 0
    minimum_czasu_znikania_kretow = 1
    maximum_czasu_znikania_kretow = 9
    minimum_czasu_pojawiania_kretow = 1
    maximum_czasu_pojawiania_kretow = 4
    
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.sekundy = 0
        self.minuty = 0

        self.ilosc_kretow = (1)
        self.kreciki = []
        # self.krecik = None

        self.l1 = ludzik()
        self.l1.x = 2
        self.l1.y = 0

        self.box = Rect((0, 0), (width - 1, height - 1))

        self.waz = snake(5, self.width // 2, 396, 'lewo')

        self.put_apple()

        clock.schedule_interval(self.czasObliczanie, 1)

        losowanie_pokaz = random.randrange(1, 9)
        print('sekundy:', losowanie_pokaz)
        clock.schedule_unique(self.put_krecik, losowanie_pokaz)

        # self.miejsce_krecik_x = None
        # self.miejsce_krecik_y = None



    def draw(self, screen):
        screen.clear()
        screen.fill(game.color_ramka)
        screen.draw.filled_rect(Rect((35, 80), (930, 690)), (game.pole_gry_jasne))
        for x in range (31):
            for y in range (23):
                if y %2 == 0 and x %2 == 0:
                    screen.draw.filled_rect(Rect((35 + 30 * x, 80 + 30 * y), (30, 30)), (game.kwadraty_planszy))
                
                elif y %2 == 1 and x %2 ==1:
                    screen.draw.filled_rect(Rect((35 + 30 * x, 80 + 30 * y), (30, 30)), (game.kwadraty_planszy))
        screen.draw.filled_rect(Rect((35, 20), (200 , 40)), (game.litery))
        screen.draw.filled_rect(Rect((150, 25), (80 , 30)), (game.tlozmiennej))
        screen.draw.text("Punkty:", (45, 25), fontname =  'orbitro', color="black")
        screen.draw.text(f'{self.punkty}', midright = (225, 40), fontname =  'orbitro', color="black")
        

        self.czas_rysowanie(screen)
        self.waz.draw()
        self.apple.draw()

        for kret in self.kreciki:
            kret.draw()
        

    def czas_rysowanie(self, screen):
        screen.draw.filled_rect(Rect((765, 20), (200 , 40)), (game.litery))
        screen.draw.filled_rect(Rect((867, 25), (93 , 30)), (game.tlozmiennej))
        screen.draw.text("Czas:", (775, 25), fontname =  'orbitro', color="black")
        screen.draw.text(f'{self.minuty}' , midright = (910, 40), fontname =  'orbitro', color="black")
        screen.draw.text(":", center = (913.5, 40), fontname =  'orbitro', color="black")
        screen.draw.text(f'{self.sekundy:02d}' , midleft = (917, 40), fontname =  'orbitro', color="black")

    def update(self):
        self.waz.update()
        
        #TODO: wywala sie szybka zmiana kierunku
        if keyboard.up or keyboard.w:
            self.waz.gora()

        elif keyboard.down or keyboard.s:
            self.waz.dol()

        elif keyboard.right or keyboard.d:
            self.waz.prawo()

        elif keyboard.left or keyboard.a:
            self.waz.lewo()

        pg = self.waz.poz_glowy()

        if pg[0] <= 30:
            return 'goto_end'

        if pg[1] <= 80:
            return 'goto_end'

        if pg[2] >= 35 + 930:
            return 'goto_end'

        if pg[3] >= 80 + 690:
            return 'goto_end'

        if self.waz.czy_gryze() == True:
            return 'goto_end'

        if self.waz.istniejesz(self.apple.x, self.apple.y) == True:
            self.punkty += 1
            
            self.put_apple()
            self.waz.zwieksz_sie()


            if self.punkty % 10 == 0:
                self.ilosc_kretow = self.ilosc_kretow * 2


        for x in self.kreciki:
            if self.waz.istniejesz(x.x, x.y) == True:
                self.punkty -= 1
                self.kreciki.remove(x)

                los3 = random.randrange(game.minimum_czasu_pojawiania_kretow, game.maximum_czasu_pojawiania_kretow)

                clock.schedule_unique(self.put_krecik, los3)

                break


    def czasObliczanie(self):
        self.sekundy += 1
        timer = [10, 20, 30, 40, 50, 60]

        for x in timer:
            if self.sekundy == x:
                self.waz.spowolnienie() 

        if self.sekundy == 60:
            self.sekundy = 00
            self.minuty += 1


    def put_apple(self):
        while True:
            miejsce_apple_x = random.randrange(50,35 + 930 - 15, 30)
            miejsce_apple_y = random.randrange(96, 80 + 690 - 15, 30)

            if self.waz.istniejesz(miejsce_apple_x, miejsce_apple_y) == True:
                pass

            else:
                break

        self.apple = Actor('apple',(miejsce_apple_x, miejsce_apple_y))

    def put_krecik(self):
        if len(self.kreciki) >= self.ilosc_kretow:
            return

        while True:
            miejsce_krecik_x = random.randrange(50,35 + 930 - 15, 30)
            miejsce_krecik_y = random.randrange(96, 80 + 690 - 15, 30)
          
            if self.waz.istniejesz(miejsce_krecik_x, miejsce_krecik_y) == True:
                pass

            else:
                break

        self.kreciki.append (Actor('krecik',(miejsce_krecik_x, miejsce_krecik_y)))

        if len(self.kreciki) < self.ilosc_kretow:
            los1 = random.randrange(1, 9)
            clock.schedule_unique(self.put_krecik, los1)

        los2 = random.randrange(1, 5)
        clock.schedule_unique(self.ukryj_krecik, los2)



    def ukryj_krecik(self):
        if len(self.kreciki) == 0:
            return
        
        del self.kreciki[0]

        if len(self.kreciki) > 0:
            kolejny_za = random.randrange(game.minimum_czasu_znikania_kretow, game.maximum_czasu_znikania_kretow)
            clock.schedule_unique(self.ukryj_krecik, kolejny_za)

        losowanie = random.randrange(1, 4)
        clock.schedule_unique(self.put_krecik, losowanie)
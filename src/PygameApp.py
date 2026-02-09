import pygame

class PygameApp:
    def __init__(self, w, h):
        pygame.init()
        self.screen = pygame.display.set_mode((w, h))
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = ""


    def events(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.mouseclicked = True
            else:
                self.mouseclicked = False

            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    self.escpressed = True 
                else:
                    self.escpressed = False

    def draw(self):
        self.screen.fill("white")
        pygame.display.flip()
        self.clock.tick(60) 

    def loop(self):
        while self.running:
            self.events()
            self.draw()

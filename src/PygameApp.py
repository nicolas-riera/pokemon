import pygame
import os

from src.assets_loading import BASE_DIR
from src.pokemon.Pokemon import Pokemon
from src.pokemon.Pokedex import Pokedex
from src.Menu import Menu

class PygameApp:
    def __init__(self, w, h):
        pygame.init()
        pygame.display.set_caption("Pokémon")
        pygame.display.set_icon(pygame.image.load(os.path.join(BASE_DIR, "..", "assets", "img", "logo.png")))
        self.screen = pygame.display.set_mode((w, h))
        self.clock = pygame.time.Clock()
        self.running = True
        self.pokemon_objects = []
        self.font = pygame.font.Font(os.path.join(BASE_DIR, "..", "assets", "font", "pokemon_generation_1.ttf"), 30)
        self.state = "menu"
        self.menu = Menu()

    def events(self):
        self.escpressed = False
        self.mouseclicked = False

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.mouseclicked = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.escpressed = True 

    def draw(self):
        self.screen.fill("white")
        if self.state == "menu":
            self.menu.menu_rendering(self.screen, self.font)
        if self.state == "pokedex":
            Pokedex.pokedex_rendering(self.screen)
        pygame.display.flip()
        self.clock.tick(60) 

    def logic(self):
        if self.state == "menu":
            self.state = self.menu.menu_logic(self.escpressed, self.mouseclicked, self.state)

    def loop(self):
        while self.running:
            self.events()
            self.draw()
            self.logic()

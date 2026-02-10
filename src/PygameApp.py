import pygame
import os
import json

from src.pokemon.Pokemon import Pokemon
from src.Menu import Menu

class PygameApp:
    def __init__(self, w, h):
        pygame.init()
        pygame.display.set_caption("Pokémon")
        # pygame.display.set_icon(pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__), "..", "assets", "img", "logo.png")))
        self.screen = pygame.display.set_mode((w, h))
        self.clock = pygame.time.Clock()
        self.running = True
        self.pokemon_objects = []
        self.font = pygame.font.Font(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "font", "pokemon_generation_1.ttf"), 30)
        self.state = "menu"
        self.menu = Menu()

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
        if self.state == "menu":
            self.menu.menu_rendering(self.screen, self.font)
        pygame.display.flip()
        self.clock.tick(60) 

    def logic(self):
        if self.state == "menu":
            self.state = self.menu.menu_logic(self.escpressed, self.mouseclicked, self.state)

    def load(self):
        with open('./data/pokedex.json', 'r') as file:
            self.pokedex_data = json.load(file)
        
        with open('./data/pokemon.json', 'r') as file:
            self.pokemon_data = json.load(file)

        for instance_key, instance_val in self.pokedex_data.items():
            target_id = instance_val["id"]

            if target_id in self.pokemon_data:
                pokemon_info = self.pokemon_data[target_id]

                p = Pokemon(pokemon_info["name"])
                p.set_types(pokemon_info["type"])
                p.set_attack(pokemon_info["attack"])
                p.set_defense(pokemon_info["defense"])
                p.set_hp(pokemon_info["hp"])
                self.pokemon_objects.append(p)

    def loop(self):
        while self.running:
            self.events()
            self.draw()
            self.logic()

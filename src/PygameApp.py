import pygame
import os
import json
from src.pokemon.Pokemon import Pokemon

from src.Menu import Menu

from src.pokemon import Pokedex

class PygameApp:
    def __init__(self, w, h):
        pygame.init()
        pygame.display.set_caption("Pokémon")
        # pygame.display.set_icon(pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__), "..", "assets", "img", "logo.png")))
        self.screen = pygame.display.set_mode((w, h))
        self.clock = pygame.time.Clock()
        self.running = True
        self.pokemons = ["Duduo", "Seel"]
        self.pokemon_objects = []
        self.font = pygame.font.Font(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "font", "pokemon_generation_1.ttf"), 30)
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
            self.pokedex.pokedex_rendering(self.screen)
        pygame.display.flip()
        self.clock.tick(60) 

    def logic(self):
        if self.state == "menu":
            self.state = self.menu.menu_logic(self.escpressed, self.mouseclicked, self.state)
        elif self.state == "pokedex": #created a pokedex GAMESTATE 
            self.state = self.menu.menu_logic(self.escpressed, self.mouseclicked, self.state)
        elif self.state == "add_pokemon": #created a add_pokemon GAMESTATE
            self.state = self.menu.menu_logic(self.escpressed, self.mouseclicked, self.state)
    @staticmethod #method dealing with the logic related to the class without accessing the clas
    def load_pokemons(pokemon_names): #is this useful ?
        pokemon_objects = []
        with open('./data/pokemon.json', 'r') as file:
        # base_dir = os.path.dirname(os.path.abspath(__file__))
        # json_path = os.path.join(base_dir, "..", "data", "pokemon.json")
        # with open(json_path, 'r') as file:
            pokemon_data = json.load(file) # open our JSON containing pokemons
        for name in pokemon_names:
            for id, data in pokemon_data.items():
                if data["name"] == name:
                    p = Pokemon(name)
                    p.types = data["type"]
                    p.attack = data["attack"]
                    p.defense = data["defense"]
                    p.hp = data["hp"]
                    pokemon_objects.append(p)
                    break
        return pokemon_objects
    def load(self):
        self.pokemon_objects = PygameApp.load_pokemons(self.pokemons)
        return self.pokemon_objects

    def loop(self):
        while self.running:
            self.events()
            self.draw()
            self.logic()

            print(self.pokemon_objects[0].name)

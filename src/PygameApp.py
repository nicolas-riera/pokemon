import pygame
import os

from src.assets_loading import BASE_DIR, TITLE_MUSIC, BATTLE_MUSIC
from src.pokemon.Pokemon import Pokemon
from src.pokemon.Pokedex import Pokedex
from src.Menu import Menu
from src.game.Combat import Combat
from src.screen_transition import screen_transition

MUSIC_END = pygame.USEREVENT + 1

class PygameApp:
    def __init__(self, w, h):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("Pokémon")
        pygame.display.set_icon(pygame.image.load(os.path.join(BASE_DIR, "..", "assets", "img", "logo.png")))
        self.screen = pygame.display.set_mode((w, h))
        self.clock = pygame.time.Clock()
        self.running = True
        self.pokemon_objects = []
        self.font = pygame.font.Font(os.path.join(BASE_DIR, "..", "assets", "font", "pokemon_generation_1.ttf"), 30), pygame.font.Font(os.path.join(BASE_DIR, "..", "assets", "font", "pokemon_generation_1.ttf"), 20)
        self.state = "menu"
        self.gamestates = ["game", "choose_action", "choose_attack_type", "message"]
        self.reset_all_class()
        pygame.mixer.music.set_endevent(MUSIC_END)

    def reset_all_class(self):
        self.menu = Menu()
        self.pokedex = Pokedex()
        self.combat = Combat()

    def events(self):
        self.escpressed = False
        self.mouseclicked_left = False
        self.mouseclicked_right = False

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.mouseclicked_left = True

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                self.mouseclicked_right = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.escpressed = True

            if self.state == "menu":
                if event.type == MUSIC_END:
                    pygame.mixer.music.pause()
                    pygame.mixer.music.unload()
                    pygame.mixer.music.load(TITLE_MUSIC)
                    pygame.mixer.music.play(-1)
            elif self.state in self.gamestates:
                if event.type == MUSIC_END:
                    pygame.mixer.music.pause()
                    pygame.mixer.music.unload()
                    pygame.mixer.music.load(BATTLE_MUSIC)
                    pygame.mixer.music.play(-1)

    def draw(self):
        self.screen.fill("white")
        if self.state == "menu":
            self.menu.menu_rendering(self.screen, self.font)
        if self.state == "pokedex":
            self.pokedex.draw_pokedex(self.screen, self.font[1])
        if self.state in self.gamestates:
            self.combat.draw(self.screen, self.font)

        pygame.display.flip()
        self.clock.tick(60)

    def logic(self):
        self.changed_state = False
        prev_state = self.state

        if self.state == "menu":
            self.state = self.menu.menu_logic(self.escpressed, self.mouseclicked_left, self.state)
        elif self.state in self.gamestates:
            ally = self.pokedex.pokedex_objects[self.pokedex.get_pokemon_id_in_use()]
            self.state = self.combat.logic(ally, self.pokedex, self.escpressed, self.mouseclicked_left)
        elif self.state == "pokedex":
            self.state = self.pokedex.pokedex_logic(self.escpressed, self.state, self.mouseclicked_left, self.mouseclicked_right)

        if prev_state != self.state and self.state not in self.gamestates[1:]:
            screen_transition(self.screen, self.clock, self.state)
            self.reset_all_class()
            self.changed_state = True

    def loop(self):
        while self.running:
            self.events()
            self.logic()
            if not self.changed_state:
                self.draw()
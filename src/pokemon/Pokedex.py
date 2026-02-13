import os
import pygame
import json

from src.assets_loading import POKEDEX_BACKGROUND, POKEMON_DATA, POKEMON_CENTER_MUSIC, SFX_SWAP, SFX_TINK
from src.pokemon.Pokemon import Pokemon
from src.pyinstaller.data_path import get_data_path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class Pokedex:
    def __init__(self): 

        '''
        Initialize Pokedex data and pagination setting
        '''
        self.pokedex_data = {} #dict to save our pokemons
        self.pokedex_objects = []
        self.page_index = 0
        self.pokemons_per_page = 4 # amount of pokemon per page to be changed later
        self.music = None
        self.font_path = os.path.join(BASE_DIR, "..", "..", "assets", "font", "pokemon_generation_1.ttf")

        # we load the data when creating the class to not do it again
        self.load_json()
        self.load_pokedex_objects()

    def pokedex_music(self):
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load(POKEMON_CENTER_MUSIC)
            pygame.mixer.music.play(-1)
        elif self.music != "pokedex":
            self.music = "pokedex"
            pygame.mixer.music.pause()
            pygame.mixer.music.unload()
            
    def load_json(self):
        with open(get_data_path("pokedex.json"), 'r') as file:
            self.pokedex_data = json.load(file)

    def write_json(self):
        with open(get_data_path("pokedex.json"), 'w') as file:
            json.dump(self.pokedex_data, file, indent=4)
        

    def load_pokedex_objects(self):
        self.pokedex_objects.clear() # clear the list to not load the pokemons twice 
        for instance_val in self.pokedex_data.values():
            target_id = instance_val["id"]

            if target_id in POKEMON_DATA:
                pokemon_info = POKEMON_DATA[target_id]

                p = Pokemon(pokemon_info["name"])
                p.set_types(pokemon_info["type"])
                p.set_attack(pokemon_info["attack"])
                p.set_defense(pokemon_info["defense"])
                p.set_hp(instance_val["hp"])
                p.set_level(instance_val["level"])
                p.set_xp(instance_val["xp"])
                self.pokedex_objects.append(p)

    def add_pokemon_to_pokedex(self, pokemon_id, hp, level, xp):
        """
        Method called to capture a pokemon and save it into the pokedex JSON
        Create a new entry for the captured pokemon using the next available index
        """
        next_index = str(len(self.pokedex_data)) # simply find the next next index for pagination purposes 

        new_pokemon = { #we init our pokemon as dict 
            "id": pokemon_id,
            "hp": hp,
            "level": level,
            "xp": xp
        }
        self.pokedex_data[next_index] = new_pokemon # set our new pokemon in the next index in pokemon data 

        self.write_json() # call function to dump new pokemon in json
        self.load_pokedex_objects() # actualize pokedex and clear 

    def draw_text_aligned(self, surface, text, font, color, container_rect, align="center", padding=(0,0)):
        """
        draw an aligned text according to the given rect
        align: "center", "topleft", "midleft", "midright"
        padding: tuple (x, y) to move our text
        """
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        if align == "center":
            text_rect.center = container_rect.center #align
        elif align == "midleft":
            text_rect.midleft = container_rect.midleft
            text_rect.x += padding[0] #add margin 
            text_rect.y += padding[1]
        elif align == "bottomright":
            text_rect.midright = container_rect.midright
            # text_rect.x -= padding[0]
            # text_rect.y += padding[1]

        elif align == "midtop":
            text_rect.midtop = container_rect.midtop
            text_rect.y += padding[1]
            # text_rect.x += padding[0]
        surface.blit(text_surface, text_rect)

    def draw_pokedex(self, screen, font):
        screen.blit(POKEDEX_BACKGROUND, (0, 0))
        
        # Create a Surface (width, height) and fill it instead of using the screen a surface later on
        container_height = 500
        container = pygame.Surface((630, container_height))

        beginning_page_index = self.page_index * self.pokemons_per_page # get the index of the first element and multiply it by the number of page to get the first item for example page two starts with the pokemon indexed at ten
        ending_page_index = beginning_page_index + self.pokemons_per_page
        pokemons_displayed = self.pokedex_objects [beginning_page_index:ending_page_index]
        
        # use a relative Y coordinate (starts at 0 inside the container)
        item_height = container_height / self.pokemons_per_page
        button_height = item_height - 10 
        
        # modular font size
        name_font_size = int(button_height * 0.30)
        stats_font_size = int(button_height * 0.17)
        # max function make sure that it never goes under 10 px
        # set font size to 25% of button height
        # if self.font_size != target_font_size:
        #     self.font_size = target_font_size
        #     self.font = pygame.font.Font(self.font_path, self.font_size)
        name_font =  pygame.font.Font(self.font_path, name_font_size)
        stats_font = pygame.font.Font(self.font_path, stats_font_size)
        relative_y = 0
        for p in pokemons_displayed:
            # Draw.rect(surface, color, (x position, y position, x width, y width))
            #     pygame.draw.rect(
            #     surface,
            #     (255, 0, 0),          # color
            #     pygame.Rect(50, 50, 200, 100),  # rect
            #     border_radius=20      # radius of the corners
            # )
            
            # draw on container using relative coordinates (x=0, y=relative_y) to make it modular
            pygame.draw.rect(container, (185, 185, 185), (0, relative_y, 630, button_height), border_radius = 10) 
            rect = pygame.Rect((0, relative_y, 630, button_height)) 
            name_pokemon = f"{p.get_name()}"
            type_pokemon = f"{p.get_types()}"
            stats_pokemon = f"ATT : {p.get_attack()} DEF : {p.get_defense()} HP : {p.get_hp()} LVL : {p.get_level()} XP :{p.get_xp()}"
            
            self.draw_text_aligned(container, name_pokemon, name_font, (0, 0, 0), rect, "midtop", padding=(0, 10))
            self.draw_text_aligned(container, type_pokemon, stats_font, (0, 0, 0), rect, "bottomright", padding= any)
            self.draw_text_aligned(container, stats_pokemon, stats_font, (0, 0, 0), rect, "midleft", padding=(10,20))

            # surface_text_name = font.render(name_pokemon, True, (0, 0, 0))
            # surface_text_type = font.render(type_poekmon, True, (0, 0, 0)) 
            # surface_text_stats = font.render(stats_pokemon, True, (0, 0, 0)) 
            # screen.blit(surface_text_name, (315, position_y))
            # screen.blit(surface_text_type, (90, position_y - 20))
            # screen.blit(surface_text_stats, (540, position_y - 20))


            relative_y += item_height # spacing between lines 
        
        # blit the container onto the screen at the specific position
        screen.blit(container, (85, 145))
        print(pygame.mouse.get_pos())

    def pokedex_logic(self, escpressed, state, mouseclicked):
        """
        Method managing pokedex inputs
        param escpressed : get escape input
        param state : get GAMESTATE
        """

        self.pokedex_music()

        if escpressed:
            pygame.mixer.music.pause()
            pygame.mixer.music.unload()
            pygame.mixer.Sound(SFX_TINK).play()
            self.music = None
            state = "menu"
        
        # recalculate the displayed items to check for collisions
        beginning_page_index = self.page_index * self.pokemons_per_page
        ending_page_index = beginning_page_index + self.pokemons_per_page
        pokemons_displayed = self.pokedex_objects[beginning_page_index:ending_page_index]

        container_height = 500
        item_height = container_height / self.pokemons_per_page
        button_height = item_height - 10
        position_y = 145
        hover = False
        
        for p in pokemons_displayed:
            # Create a Rect matching the one drawn in draw_pokedex
            button_rect = pygame.Rect(85, position_y, 630, button_height)
            if button_rect.collidepoint(pygame.mouse.get_pos()):
                if mouseclicked:
                    pygame.mixer.Sound(SFX_SWAP).play()
                    print(f"Clicked on {p.get_name()}")
                else:
                    hover = True
            position_y += item_height

        if hover:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)  
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        return state

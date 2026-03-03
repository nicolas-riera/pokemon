# Pokedex.py
import os
import pygame
import json

from src.assets_loading import POKEDEX_BACKGROUND, POKEMON_DATA, POKEMON_CENTER_MUSIC, SFX_SWAP, SFX_TINK, SFX_WITHDRAW_DEPOSIT, SFX_PRESS_AB
from src.pokemon.Pokemon import Pokemon
from src.pyinstaller.data_path import get_data_path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class Pokedex:
    def __init__(self): 

        '''
        Initialize Pokedex data and pagination setting
        '''
        self.pokedex_data = {} #dict to save our pokemons
        self.pokedex_objects = [] #list to save our objects
        self.page_index = 0
        self.pokemons_per_page = 4 # amount of pokemon per page, can be changed according to prefrences
        self.music = None
        self.font_path = os.path.join(BASE_DIR, "..", "..", "assets", "font", "pokemon_generation_1.ttf")
        # we load the data when creating the class to not do it again
        self.load_json()
        self.load_pokedex_objects()

    def get_pokemon_id_in_use(self):
        for id, values in self.pokedex_data.items():
            if values["in_use"] == True:
                return int(id)

    def pokedex_music(self, in_combat=False):
        if in_combat:
            return
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
        """
        Load and instantiate Pokemon objects from the pokedex data.
        """
        self.pokedex_objects.clear() # clear the list to not load the pokemons twice 
        for instance_val in self.pokedex_data.values():
            target_id = instance_val["id"]

            if target_id in POKEMON_DATA:
                pokemon_info = POKEMON_DATA[target_id]

                p = Pokemon(pokemon_info["name"])
                p.set_id(target_id)
                p.set_types(pokemon_info["type"])
                p.set_attack(pokemon_info["attack"])
                p.set_defense(pokemon_info["defense"])
                p.set_hp(instance_val["hp"])
                p.set_level(instance_val["level"])
                p.set_xp(instance_val["xp"])
                p.set_in_use(instance_val["in_use"])
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
            "xp": xp,
            "in_use": False
        }
        self.pokedex_data[next_index] = new_pokemon # set our new pokemon in the next index in pokemon data 

        self.write_json() # call function to dump new pokemon in json
        self.load_pokedex_objects() # actualize pokedex and clear 

    def draw_text_aligned(self, surface, text, font, color, container_rect, align="center", padding=(0,0), id = None):
        """
        draw an aligned text according to the given rect
        align: "center", "topleft", "midleft", "midright"
        padding: tuple (x, y) to move our text
        """
        ico = None
        if id:
            ico = pygame.image.load(os.path.join(BASE_DIR, "..", "..", "assets", "img", "pokemon_sprites", "icons", f"{id}.png"))
            ico = pygame.transform.scale(ico, (90, 90))
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        if align == "center":
            text_rect.center = container_rect.center #align
        elif align == "bottomleft":
            text_rect.bottomleft = container_rect.bottomleft
            text_rect.x += padding[0] #add margin 
            text_rect.y -= padding[1]
        elif align == "topright":
            text_rect.topright = container_rect.topright
            text_rect.x -= padding[0]
            text_rect.y += padding[1]

        elif align == "topleft":
            text_rect.topleft = container_rect.topleft
            text_rect.x += padding[0]
            text_rect.y += padding[1]
            if ico:
                surface.blit(ico, (text_rect.x,(text_rect.y - 30)))
                text_rect.x += ico.get_width() + 10
        surface.blit(text_surface, text_rect)

    def draw_pokedex(self, screen, font):
        screen.blit(POKEDEX_BACKGROUND, (0, 0))
        
        # Create a Surface and fill it instead of using the screen a surface later on
        container_height = 500
        container = pygame.Surface((630, container_height))

        beginning_page_index = self.page_index * self.pokemons_per_page # get the index of the first element and multiply it by the number of page to get the first item for example page two starts with the pokemon indexed at ten
        ending_page_index = beginning_page_index + self.pokemons_per_page
        pokemons_displayed = self.pokedex_objects [beginning_page_index:ending_page_index]
        
        # use a relative Y coordinate (starts at 0 inside the container)
        item_height = container_height / self.pokemons_per_page
        button_height = item_height - 10 
        
        # modular font size
        # set font size to x % of button height
        name_font_size = int(button_height * 0.30)
        stats_font_size = int(button_height * 0.17)

        name_font =  pygame.font.Font(self.font_path, name_font_size)
        stats_font = pygame.font.Font(self.font_path, stats_font_size)

        relative_y = 0

        # color change of the box depending on if hovered or clicked 
        for p in pokemons_displayed:
            
            color = (185, 185, 185)
            if p == self.hovered_pokemon:
                color = (94, 113, 106) 
            elif p.get_in_use():
                color = (56, 128, 114)

            # draw on container using relative coordinates (x=0, y=relative_y) to make it modular
            pygame.draw.rect(container, color, (0, relative_y, 630, button_height), border_radius = 10) 
            rect = pygame.Rect((0, relative_y, 630, button_height))
            
            name_pokemon = f"{p.get_name()}"
            type_pokemon = " / ".join(p.get_types()) #display the types without the brackets
            stats_pokemon = f"ATT : {p.get_attack()} DEF : {p.get_defense()} HP : {p.get_hp()} LVL : {p.get_level()} XP :{p.get_xp()}"
            
            self.draw_text_aligned(container, name_pokemon, name_font, (0, 0, 0), rect, "topleft", padding=(10, 10), id = p.get_id())
            self.draw_text_aligned(container, type_pokemon, stats_font, (0, 0, 0), rect, "topright", padding= (10,25))
            self.draw_text_aligned(container, stats_pokemon, stats_font, (0, 0, 0), rect, "bottomleft", padding=(10,10))

            relative_y += item_height # spacing between lines 
        
        # blit the container onto the screen at the specific position
        screen.blit(container, (85, 145))
        
        max_pages = max(0, (len(self.pokedex_objects) - 1) // self.pokemons_per_page) #calculate max pages

        pagination_font = pygame.font.Font(self.font_path, 15)

        # Dispaly previous button 
        if self.page_index > 0:
            prev_text = pagination_font.render("<", True, (200, 200, 200))
            screen.blit(prev_text, (648, 690))
            
        # Dispaly actual page number 
        page_text = pagination_font.render(f"Page {self.page_index + 1} / {max_pages + 1}", True, (0, 0, 0))
        screen.blit(page_text, (607, 64))

        # Display following page
        if self.page_index < max_pages:
            next_text = pagination_font.render(">", True, (200, 200, 200))
            screen.blit(next_text, (690, 690))
        back_font = pygame.font.Font(self.font_path, 12) 
        back_text = back_font.render("Escape", True, (250, 250, 250))
        screen.blit(back_text, (100, 690))
        print(pygame.mouse.get_pos())  # FOR DEBUG PURPOSE DO NOT DELETE 



    def pokedex_logic(self, escpressed, state, mouseclicked_left, mouseclicked_right, return_state="menu", in_combat=False):
        """
        Method managing pokedex inputs
        param escpressed : get escape input
        param state : get GAMESTATE
        """
        self.pokedex_music(in_combat=in_combat)

        if escpressed:
            if not in_combat:
                pygame.mixer.music.pause()
                pygame.mixer.music.unload()
                pygame.mixer.Sound(SFX_TINK).play()
                self.music = None
            state = return_state
        
        # recalculate the displayed items to check for collisions
        beginning_page_index = self.page_index * self.pokemons_per_page
        ending_page_index = beginning_page_index + self.pokemons_per_page
        pokemons_displayed = self.pokedex_objects[beginning_page_index:ending_page_index]

        container_height = 500
        item_height = container_height / self.pokemons_per_page
        button_height = item_height - 10
        position_y = 145
        hover = False
        self.hovered_pokemon = None
        
        for p in pokemons_displayed:
            # create a Rect matching the one drawn in draw_pokedex
            button_rect = pygame.Rect(85, position_y, 630, button_height)
            if button_rect.collidepoint(pygame.mouse.get_pos()):
                if mouseclicked_left:
                    pygame.mixer.Sound(SFX_SWAP).play()
                                        
                    was_in_use = p.get_in_use() #save the selected pokemon 

                    #go through every pokemon and put them as not used 
                    for pokemon_obj in self.pokedex_objects:
                        pokemon_obj.set_in_use(False)
                    for key in self.pokedex_data.keys():
                        self.pokedex_data[key]["in_use"] = False

                    # if no pokemon was set in use toggle in use
                    if not was_in_use:
                        p.set_in_use(True)
                        for key, val in self.pokedex_data.items():
                            if val["id"] == p.get_id():
                                self.pokedex_data[key]["in_use"] = True
                                break
                    self.write_json()
                elif mouseclicked_right:
                    print(f"Clicked on right {p.get_name()}")
                    pygame.mixer.Sound(SFX_WITHDRAW_DEPOSIT).play()
                    key_to_remove = None

                    for key, attributes in self.pokedex_data.items(): # iterate through both keys and values in pokedex data 
                        if attributes['id'] == p.get_id(): # if the id of pokemon we clicked on we save it 
                            key_to_remove = key
                            break
                    
                    if key_to_remove: # if an id we clicked on is true we delete the whole index 
                        del self.pokedex_data[key_to_remove]
                        temp_dict = {}
                        for i in range(int(key_to_remove)):
                            temp_dict[f"{i}"] = self.pokedex_data[f"{i}"]
                        for i in range(int(key_to_remove), (len(self.pokedex_data))):
                            temp_dict[f"{i}"] = self.pokedex_data[f"{i+1}"]
                        self.pokedex_data = temp_dict
                        # write save and dispaly
                        self.write_json()
                        self.load_pokedex_objects() 
                else:
                    hover = True
                    self.hovered_pokemon = p
            position_y += item_height


        max_pages = max(0, (len(self.pokedex_objects) - 1) // self.pokemons_per_page)
        
        #make rect for previous and next buttons 
        prev_rect = pygame.Rect(648, 690, 20, 40)
        next_rect = pygame.Rect(690, 690, 20, 40)
        #if button hover previous button
        if prev_rect.collidepoint(pygame.mouse.get_pos()) and self.page_index > 0:
            hover = True
            if mouseclicked_left:
                pygame.mixer.Sound(SFX_PRESS_AB).play() 
                self.page_index -= 1 #we go back 
                
        elif next_rect.collidepoint(pygame.mouse.get_pos()) and self.page_index < max_pages:
            hover = True
            if mouseclicked_left:
                pygame.mixer.Sound(SFX_PRESS_AB).play()
                self.page_index += 1 

        back_rect = pygame.Rect(100, 690, 50, 50)
        if back_rect.collidepoint(pygame.mouse.get_pos()):
            hover = True
            if mouseclicked_left:
                if not in_combat:
                    pygame.mixer.music.pause()
                    pygame.mixer.music.unload()
                    pygame.mixer.Sound(SFX_TINK).play()
                    self.music = None
                state = return_state

        if hover:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        return state
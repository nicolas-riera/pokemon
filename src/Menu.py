import pygame

from src.assets_loading import LOGO_TITLE_SCALED, LOGO_TITLE_RECT, CURSOR, INTRO_TITLE_MUSIC

class Menu:
    def __init__(self):
        self.__play_button = pygame.Rect((180, 405, 440, 75))
        self.__enemy_pokemon_button = pygame.Rect((180, 485, 440, 70))
        self.__pokedex_button = pygame.Rect((180, 560, 440, 75))

    @staticmethod
    def menu_intro_music():
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load(INTRO_TITLE_MUSIC)
            pygame.mixer.music.play()
            

    def menu_rendering(self, screen, font):

        screen.blit(LOGO_TITLE_SCALED, LOGO_TITLE_RECT)

        play_button_text = font[0].render("Play", True, (0, 0, 0))
        screen.blit(play_button_text, (355, 430))
        enemy_pokemon_button_text = font[0].render("Enemy Pokemon", True, (0, 0, 0))
        screen.blit(enemy_pokemon_button_text, (235, 500))
        pokedex_button_text = font[0].render("Pokedex", True, (0, 0, 0))
        screen.blit(pokedex_button_text, (307, 570))

        pygame.draw.line(screen, (0, 0, 0), (180, 400), (620, 400), width=5)
        pygame.draw.line(screen, (0, 0, 0), (180, 640), (620, 640), width=5)

        pygame.draw.line(screen, (0, 0, 0), (180, 400), (180, 640), width=5)
        pygame.draw.line(screen, (0, 0, 0), (620, 400), (620, 640), width=5)

        if self.__play_button.collidepoint(pygame.mouse.get_pos()):
            screen.blit(CURSOR, (190, 430)) 
        elif self.__enemy_pokemon_button.collidepoint(pygame.mouse.get_pos()):
            screen.blit(CURSOR, (190, 500)) 
        elif self.__pokedex_button.collidepoint(pygame.mouse.get_pos()):
            screen.blit(CURSOR, (190, 570))


    def menu_logic(self, escpressed, mouseclicked, state):

        self.menu_intro_music()

        if escpressed: 
            pygame.quit()
            raise SystemExit
        if self.__play_button.collidepoint(pygame.mouse.get_pos()) or self.__enemy_pokemon_button.collidepoint(pygame.mouse.get_pos()) or self.__pokedex_button.collidepoint(pygame.mouse.get_pos()):
            if mouseclicked:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                if self.__play_button.collidepoint(pygame.mouse.get_pos()):
                    state = "game"
                elif self.__enemy_pokemon_button.collidepoint(pygame.mouse.get_pos()):
                    state = "enemy_pokemon"
                else:
                    state = "pokedex"
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        return state
        
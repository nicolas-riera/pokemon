import pygame

from src.assets_loading import LOGO_TITLE_SCALED, LOGO_TITLE_RECT, CURSOR

class Menu:
    def __init__(self):
        self.__play_button = pygame.Rect((200, 405, 400, 75))
        self.__add_pokemon_button = pygame.Rect((200, 485, 400, 70))
        self.__pokedex_button = pygame.Rect((200, 560, 400, 75))

    def menu_rendering(self, screen, font):

        screen.blit(LOGO_TITLE_SCALED, LOGO_TITLE_RECT)

        play_button_text = font.render("Play", True, (0, 0, 0))
        screen.blit(play_button_text, (355, 430))
        add_pokemon_button_text = font.render("Add Pokemon", True, (0, 0, 0))
        screen.blit(add_pokemon_button_text, (260, 500))
        pokedex_button_text = font.render("Pokedex", True, (0, 0, 0))
        screen.blit(pokedex_button_text, (307, 570))

        pygame.draw.line(screen, (0, 0, 0), (200, 400), (600, 400), width=5)
        pygame.draw.line(screen, (0, 0, 0), (200, 640), (600, 640), width=5)

        pygame.draw.line(screen, (0, 0, 0), (200, 400), (200, 640), width=5)
        pygame.draw.line(screen, (0, 0, 0), (600, 400), (600, 640), width=5)

        if self.__play_button.collidepoint(pygame.mouse.get_pos()):
            screen.blit(CURSOR, (210, 430)) 
        elif self.__add_pokemon_button.collidepoint(pygame.mouse.get_pos()):
            screen.blit(CURSOR, (210, 500)) 
        elif self.__pokedex_button.collidepoint(pygame.mouse.get_pos()):
            screen.blit(CURSOR, (210, 570))


    def menu_logic(self, escpressed, mouseclicked):

        if escpressed:
            pygame.quit()
            raise SystemExit
        
        elif self.__play_button.collidepoint(pygame.mouse.get_pos()) or self.__add_pokemon_button.collidepoint(pygame.mouse.get_pos()) or self.__pokedex_button.collidepoint(pygame.mouse.get_pos()):
            if mouseclicked:
                if self.__play_button.collidepoint(pygame.mouse.get_pos()):
                    print("play")
                elif self.__add_pokemon_button.collidepoint(pygame.mouse.get_pos()):
                    print("add pokemon")
                else:
                    print("pokedex")
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        
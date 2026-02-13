from pygame import display
from time import sleep

def screen_transition(screen):
    screen.fill("white")
    display.flip()
    sleep(0.5)
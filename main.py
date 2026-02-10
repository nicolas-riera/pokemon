from src.PygameApp import PygameApp

def main():
    game = PygameApp(800, 800)
    game.load()
    game.loop()

if __name__ == "__main__":
    main()

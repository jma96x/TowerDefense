from .towergame import TowerGame

def start_game():
    game = TowerGame.create()
    game.loop()

if __name__ == "__main__":
    start_game()
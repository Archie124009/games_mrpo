import sys
import os

# Добавляем путь к директории src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from cli import greet_user, choose_game
from lcm import lcm_game
from geom_progression import progression_game
from engine import run_game

if __name__ == "__main__":
    name = greet_user()
    game_choice = choose_game()
    
    if game_choice == "lcm":
        run_game(name, lcm_game)
    elif game_choice == "progression":
        run_game(name, progression_game)

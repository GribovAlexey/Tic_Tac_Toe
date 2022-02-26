from bot_logic import *
from playground import playground


def game():
    field = playground
    game_continues = True
    while game_continues:
        field, game_continues = first_bot.turn_step(field)
        if not game_continues:
            break
        field, game_continues = second_bot.turn_step(field)


game()

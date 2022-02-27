from bot_logic import Bot
from playground import Field


def make_playground():
    field_height = int(input("Enter field height: "))
    field_width = int(input("Enter field width: "))
    playground = Field(field_height, field_width)
    playground.draw_field()
    return playground


def game():
    field = make_playground()
    victory_condition = int(
        input("Input required number of symbols in a row to win: "))

    bot_count = int(input("Input bot count: "))
    bots = []
    for i in range(bot_count):
        symbol = input(f"Input {i} bot symbol: ")
        bots.append(Bot(symbol, victory_condition=victory_condition))

    game_continues = True
    while game_continues:
        for bot in bots:
            field, game_continues = bot.turn_step(field)
            field.draw_field()

            if not game_continues:
                break


game()

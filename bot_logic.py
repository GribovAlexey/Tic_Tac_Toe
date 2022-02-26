from random import randint


class Bot:
    biggest_row = 0
    won = False

    def __init__(self, symb, closed, win=3):
        self.my_symb = symb
        self.close_pos_symbols = closed
        self.victory_condition = win
        self.name = "-".join((symb, "bot"))

    def check_line(self, playground, pos, direction, current_symbol_count=1):
        new_pos = list(map(lambda x, y: x + y, pos, direction))
        if new_pos[0] < 0 or new_pos[0] >= playground.height or \
                new_pos[1] < 0 or new_pos[1] >= playground.width or \
                playground.field[new_pos[0]][new_pos[1]] != self.my_symb:
            return current_symbol_count
        else:
            new_symbol_count = \
                self.check_line(playground, new_pos, direction,
                                current_symbol_count=current_symbol_count + 1)
        return new_symbol_count

    def game_end_condition_check(self, playground, point):
        left_right_way = [(0, -1), (0, 1)]
        up_down_way = [(-1, 0), (1, 0)]
        main_diagonal_way = [(-1, -1), (1, 1)]
        secondary_diagonal_way = [(1, -1), (-1, 1)]
        all_lines = []

        left_signs = self.check_line(playground, point, left_right_way[0])
        right_signs = self.check_line(playground, point, left_right_way[1])
        all_lines.append(left_signs + right_signs - 1)

        up_signs = self.check_line(playground, point, up_down_way[0])
        down_signs = self.check_line(playground, point, up_down_way[1])
        all_lines.append(up_signs + down_signs - 1)

        main_diagonal_left_part = self.check_line(playground, point,
                                                  main_diagonal_way[0])
        main_diagonal_right_part = self.check_line(playground, point,
                                                   main_diagonal_way[1])
        all_lines.append(main_diagonal_left_part + main_diagonal_right_part - 1)

        secondary_diagonal_left_part = self.check_line(playground, point,
                                                       secondary_diagonal_way[
                                                           0])
        secondary_diagonal_right_part = self.check_line(playground, point,
                                                        secondary_diagonal_way[
                                                            1])
        all_lines.append(secondary_diagonal_left_part + \
                         secondary_diagonal_right_part - 1)

        self.biggest_row = max(max(all_lines), self.biggest_row)
        if self.victory_condition <= self.biggest_row:
            print(self.name, "wins")
            return False
        stop_count = 0
        for row in playground.field:
            for elem in row:
                if elem in self.close_pos_symbols:
                    stop_count += 1
        if stop_count == playground.width * playground.height:
            print("Draw. No one wins.")
            return False
        return True

    def turn_step(self, playground):
        y_pos = randint(0, playground.height - 1)
        x_pos = randint(0, playground.width - 1)
        while playground.field[y_pos][x_pos] in self.close_pos_symbols:
            y_pos = randint(0, playground.height - 1)
            x_pos = randint(0, playground.width - 1)
        playground.field[y_pos][x_pos] = self.my_symb
        playground.draw_field()
        game_continues = self.game_end_condition_check(playground,
                                                       (y_pos, x_pos))
        return playground, game_continues


player1_symbol = input("Input first player symbol: ")
player2_symbol = input("Input second player symbol: ")

win_condition = int(input("Input required number of symbols in a row to win: "))

first_bot = Bot(player1_symbol, [player1_symbol, player2_symbol],
                win=win_condition)
second_bot = Bot(player2_symbol, [player1_symbol, player2_symbol],
                 win=win_condition)

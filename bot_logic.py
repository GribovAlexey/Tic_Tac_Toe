from random import randint


class Bot:
    def __init__(self, symb, victory_condition=3):
        self.my_symb = symb
        self.victory_condition = victory_condition
        self.name = "-".join((symb, "bot"))

    def check_direction(self, playground, pos, direction):
        """
        Function get playground, position of the placed symbol and
        direction to check.
        Return count of player symbols in this direction
        """
        count = 0
        new_pos = pos
        while 0 <= new_pos[0] < playground.height \
                and 0 <= new_pos[1] < playground.width \
                and playground[new_pos] == self.my_symb:
            count += 1
            new_pos = list(map(lambda x, y: x + y, new_pos, direction))
        return count

    def check_win(self, playground, point: tuple):
        """
        Function gets playground and position of the placed symbol.
        Returns True if player wins, otherwise returns False
        """
        all_lines = (
            ((0, -1), (0, 1)),  # left + right
            ((-1, 0), (1, 0)),  # up + down
            ((-1, -1), (1, 1)),  # main diagonal
            ((1, -1), (-1, 1)),  # secondary diagonal
        )

        for line in all_lines:
            p1 = self.check_direction(playground, point, line[0])
            p2 = self.check_direction(playground, point, line[1])
            if p1 + p2 - 1 >= self.victory_condition:
                return True
        return False

    def check_draw(self, playground):
        for row in playground.field:
            for elem in row:
                if elem is None:
                    return False
        return True

    def check_game_continues(self, playground, point):
        if self.check_win(playground, point):
            print(self.name, "wins")
            return False
        if self.check_draw(playground):
            print("Draw. No one wins.")
            return False
        return True

    def get_random_point(self, playground):
        y_pos = randint(0, playground.height - 1)
        x_pos = randint(0, playground.width - 1)
        while playground.field[y_pos][x_pos] is not None:
            y_pos = randint(0, playground.height - 1)
            x_pos = randint(0, playground.width - 1)
        return (y_pos, x_pos)

    def turn_step(self, playground):
        new_pos = self.get_random_point(playground)
        playground[new_pos] = self.my_symb
        game_continues = self.check_game_continues(playground, new_pos)
        return playground, game_continues

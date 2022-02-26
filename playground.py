class Field:
    field = []

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def draw_field(self):
        formatiser = f"%{self.width}s"
        for i in range(self.height):
            self.field.append([])
            for j in range(self.width):
                self.field[i].append(j + i * self.width)
                print(formatiser % self.field[i][j], end="")
            print()
        print("-"*self.width**2)
        return self.field


field_height = int(input("Enter field height: "))
field_width = int(input("Enter field width: "))
playground = Field(field_height, field_width)
playground.draw_field()

class Field:

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.field = []
        self.initiate_field()

    def initiate_field(self):
        for i in range(self.height):
            self.field.append([None for j in range(self.width)])

    def draw_field(self):
        formatiser = f"%{self.width}s"
        for i, row in enumerate(self.field):
            for j, elem in enumerate(row):
                draw_elem = elem if elem is not None else i * self.width + j
                print(formatiser % draw_elem, end="")
            print()
        print("-" * self.width ** 2)

    def __getitem__(self, point):
        return self.field[point[0]][point[1]]

    def __setitem__(self, point, value):
        self.field[point[0]][point[1]] = value

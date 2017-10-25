"""
A puzzle will have a collection of rows and a collection of columns.
Each collection should consist of an indexed vector
"""


class puzzle:
    def __init__(self):
        self.rows = []
        self.cols = []

    def add_row(self, color_vector):
        self.rows.append(color_vector)

    def add_col(self, color_vector):
        self.cols.append(color_vector)


class color_vector:
    def __init__(self):
        self.colors = []

    def add_color(self, color):
        self.colors.append(color)
        self.colors.sort(cmp=color.hex_value)


class color:
    def __init__(self, is_static, hex_value):
        self.is_static = is_static
        self.hex_value = hex_value


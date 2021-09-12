class Painting:
    museum = 'Louvre'

    def __init__(self, title, painter, year_of_creation):
        self.title = title
        self.painter = painter
        self.year_of_creation = year_of_creation

    def get_info(self):
        return '"{0}" by {1} ({2}) hangs in the {3}.'.format(self.title, self.painter, self.year_of_creation, Painting.museum)


input_title = input()
input_painter = input()
input_year_of_creation = input()
painting = Painting(input_title, input_painter, input_year_of_creation)
print(painting.get_info())

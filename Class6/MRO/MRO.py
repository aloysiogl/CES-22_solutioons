#!/usr/bin/python3


class Shape:
    geometric_type = 'Generic Shape'

    def area(self):
        raise Exception('Not implemented')

    def get_geometric_type(self):
        return self.geometric_type


class Plotter:

    def plot(self, ratio, topleft):

        print('Plotting at {}, ratio {}.'.format(topleft, ratio))


class Polygon(Shape, Plotter):
    geometric_type = 'Polygon'


class RegularPolygon(Polygon):
    geometric_type = 'Regular Polygon'

    def __init__(self, side):
        self.side = side


class RegularHexagon(RegularPolygon):
    geometric_type = 'Regular Hexagon'

    def area(self):
        return 'Hexagon area'


class Square(RegularPolygon):
    geometric_type = 'Square'

    def area(self):
        return 'Square area'


class PlotterBox(Square, Plotter):
    geometric_type = 'Plotter Box'


class ShapeSquareTest(Square, Shape):
    geometric_type = 'Random'


# Class example
print('Example1' + str(Square.__mro__))

# Extensions created

print('Example2' + str(PlotterBox.__mro__))

# Example3 cant be printed:
# class PlotterBox(Plotter, Square):
# TypeError: Cannot create a consistent method resolution
# order (MRO) for bases Plotter, Square

print('Example4' + str(ShapeSquareTest.__mro__))

# Example3 cant be printed:
# class ShapeSquareTest(Shape, Square):
# TypeError: Cannot create a consistent method resolution
# order (MRO) for bases Shape, Square




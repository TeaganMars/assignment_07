import utils


class Point(object):

    def __init__(self, x, y, mark={}):
        self.x = x
        self.y = y
        self.mark = mark

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x and self.y != other.y

    def __repr__(self):
        #return """{}, {}""".format(self.x, self.y)
        return "{0.__class__.__name__}(x={0.x}, y={0.y})".format(self)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __abs__(self):
        return Point(abs(self.x), abs(self.y))


class PointPattern(object):

    def __init__(self, x, y, mark={}):
        self.x = x
        self.y = y
        self.mark = mark

    def __eq__(self, other):
        return Point(self.x == other.x, self.y == other.y)





    def test_coincident(self, point_two):
        point_one = (self.x, self.y)
        return utils.check_coincident(point_one, point_two)

    def shift(self, verti, horiz):
        self.x += verti
        self.y += horiz
        return self.x, self.y

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def get_point(self):
        return self.x, self.y

    def get_mark(self):
        return self.mark


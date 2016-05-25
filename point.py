import utils


class Point(object):
    def __init__(self, x, y, mark={}):
        self.x = x
        self.y = y
        self.mark = mark

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


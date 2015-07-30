#!/usr/bin/env python3

class Building:
    def __init__(self, south, west, width_WE, width_NS, height=10):
        self.min_x = west
        self.max_x = west + width_WE
        self.min_y = south
        self.max_y = south + width_NS
        self.height = height

    def corners(self):
        return {'south-west': (self.min_y, self.min_x), 'north-west': (self.max_y, self.min_x), 'south-east': (self.min_y, self.max_x), 'north-east': (self.max_y, self.max_x)}

    def area(self):
        return (self.max_x - self.min_x) * (self.max_y - self.min_y)

    def volume(self):
        return self.area() * self.height

    def __repr__(self):
        return 'Building({south}, {west}, {width_we}, {width_ns}, {height})'.format(south=self.min_y, west=self.min_x, width_we=self.max_x - self.min_x, width_ns=self.max_y - self.min_y, height=self.height)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    def json_dict(d):
        return dict((k, list(v)) for k, v in d.items())

    b = Building(1, 2, 2, 3)
    b2 = Building(1, 2, 2, 3, 5)
    assert json_dict(b.corners()) == {'north-east': [4, 4], 'south-east': [1, 4],
                                      'south-west': [1, 2], 'north-west': [4, 2]}, "Corners"
    assert b.area() == 6, "Area"
    assert b.volume() == 60, "Volume"
    assert b2.volume() == 30, "Volume2"
    assert str(b) == "Building(1, 2, 2, 3, 10)", "String"

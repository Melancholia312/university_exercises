import math
import random


MAX_RANDINT = 25
MIN_RANDINT = 1


def make_random_line():
    while True:
        line = Line(Point(random.randint(MIN_RANDINT,MAX_RANDINT), random.randint(MIN_RANDINT,MAX_RANDINT)),
                    Point(random.randint(MIN_RANDINT,MAX_RANDINT), random.randint(MIN_RANDINT,MAX_RANDINT)))
        if line.match():
            return line


def make_random_triangle():
    while True:
        triangle = Triangle(Point(random.randint(MIN_RANDINT,MAX_RANDINT), random.randint(MIN_RANDINT,MAX_RANDINT)),
                            Point(random.randint(MIN_RANDINT,MAX_RANDINT), random.randint(MIN_RANDINT,MAX_RANDINT)),
                            Point(random.randint(MIN_RANDINT,MAX_RANDINT), random.randint(MIN_RANDINT,MAX_RANDINT)),
                            )
        if triangle.match():
            return triangle


def make_random_square():
    while True:
        point_1 = [random.randint(MIN_RANDINT,MAX_RANDINT),random.randint(MIN_RANDINT,MAX_RANDINT)]
        point_2 = [random.randint(MIN_RANDINT, MAX_RANDINT), random.randint(MIN_RANDINT, MAX_RANDINT)]
        point_3 = [random.randint(MIN_RANDINT, MAX_RANDINT), random.randint(MIN_RANDINT, MAX_RANDINT)]
        point_4 = [random.randint(MIN_RANDINT, MAX_RANDINT), random.randint(MIN_RANDINT, MAX_RANDINT)]
        if point_1 != point_2 and point_1 != point_3 and point_1 != point_4 \
                and point_2 != point_3 and point_2 != point_4 and point_3 != point_4:
            point_1 = Point(point_1[0], point_1[1])
            point_2 = Point(point_2[0], point_2[1])
            point_3 = Point(point_3[0], point_3[1])
            point_4 = Point(point_4[0], point_4[1])
            square = Square(point_1, point_2, point_3, point_4)
            if square.match():
                return square


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'x={self.x} y={self.y}'


class Line:

    def __init__(self, point_1, point_2):
        self.point_1 = point_1
        self.point_2 = point_2

    def length(self):
        return math.sqrt(
            ((self.point_2.x-self.point_1.x)**2) + ((self.point_2.y-self.point_1.y)**2)
        )

    def line_name(self):
        return f'{self.point_1}|{self.point_2} | {self.length()}'

    def match(self):
        return (self.point_1.x != self.point_2.x) and (self.point_1.y != self.point_2.y)


class Triangle:

    def __init__(self, point_1, point_2, point_3):
        self.side_1 = Line(point_1, point_2)
        self.side_2 = Line(point_2, point_3)
        self.side_3 = Line(point_3, point_1)

    def match(self):
        return self.side_1.length() + self.side_2.length() > self.side_3.length() \
               and self.side_1.length() + self.side_3.length() > self.side_2.length() \
               and self.side_2.length() + self.side_3.length() > self.side_1.length()

    def square(self):
        p = (self.side_1.length() + self.side_2.length() + self.side_3.length())/2
        return math.sqrt(p * (p-self.side_1.length()) * (p-self.side_2.length()) * (p-self.side_3.length()))

    def triangle_name(self):
        return f'({self.side_1.line_name()}) - ({self.side_2.line_name()}) - ({self.side_3.line_name()})'


class Square:

    def __init__(self, point_1, point_2, point_3, point_4):
        self.side_1 = Line(point_1, point_2)
        self.side_2 = Line(point_2, point_3)
        self.side_3 = Line(point_3, point_4)
        self.side_4 = Line(point_4, point_1)

    def match(self):
            return self.side_1.length() == self.side_2.length() \
                   and self.side_2.length() == self.side_3.length() \
                   and self.side_3.length() == self.side_4.length() \
                   and self.side_4.length() == self.side_1.length() \
                   and self.side_1.length() == self.side_3.length() \
                   and self.side_2.length() == self.side_4.length()

    def square(self):
        return self.side_1.length()**2

    def square_name(self):
        return f'({self.side_1.line_name()}) - ({self.side_2.line_name()}) ' \
               f'- ({self.side_3.line_name()}) - ({self.side_4.line_name()})'


def find_max_length(qnt_of_lines=5):
    rand_arr = {}
    for i in range(qnt_of_lines):
        random_line = make_random_line()
        rand_arr[random_line.line_name()] = random_line.length()

    for line in rand_arr:
        print(f'{line} | {rand_arr[line]}')
    print(max(rand_arr.values()))


def find_max_triangle_square(qnt_of_lines=5):
    rand_arr = {}
    for i in range(qnt_of_lines):
        random_triangle = make_random_triangle()
        rand_arr[random_triangle.triangle_name()] = random_triangle.square()

    for triangle in rand_arr:
        print(f'{triangle} | {rand_arr[triangle]}')
    print(max(rand_arr.values()))


def find_max_square_square(qnt_of_lines=5):
    rand_arr = {}
    for i in range(qnt_of_lines):
        random_square = make_random_square()
        rand_arr[random_square.square_name()] = random_square.square()

    for square in rand_arr:
        print(f'{square} | {rand_arr[square]}')
    print(max(rand_arr.values()))



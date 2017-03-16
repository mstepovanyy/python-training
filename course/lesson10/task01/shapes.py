#!/usr/bin/python3
"""
2.1   Shapes

Build a class hierarchy for a primitive graphic editor figures data model.
Two basic entities of a graphic editor are a Color and a Coordinates which are building blocks for all other entities.
Coordinates can be defined in several ways (Linear, Cyllindric, Spheric) through static methods.
A conversion logic between them is out of scope for this task,
for simplicity just store a coordinates type in a field.

There are several basic shapes:
a Point, a Line, a Circle, a Rectangle, and a Triangle - each defined by a different combination of
Color and Coordinates. A line can have a Pattern consisting of a list of (Color, length) tuples;
more complex shapes can be filled with a Color or not (be transparent) and each their border can still have a Pattern.

Within a course of this task no other methods than are necessary to create objects are required.
"""


class Color(object):
    pass

available_types = ["Linear", "Cyllindric", "Spheric"]


class Coordinate(object):
    type = "Linear"

    @staticmethod
    def set_coordinate(input_type):
        if input_type in available_types:
            Coordinate.type = input_type


class Point(object):

    def __init__(self, color, center):
        self.color = color
        self.center = center


class Line(object):

    def __init__(self, color, start, end):
        self.color = color
        self.start = start
        self.end = end


class Circle(Point):

    def __init__(self, color, center, radius):
        super().__init__(color, center)
        self.radius = radius


class Rectangle(object):

    def __init__(self, top, bottom, left, right):
        self.top = top
        self.bottom = bottom
        self.left = left
        self.right = right


class Triangle(object):

    def __init__(self, first, second, third):
        self.first = first
        self.second = second
        self.third = third


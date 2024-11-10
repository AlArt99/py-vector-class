from typing import Union
from math import sqrt, degrees, acos, cos, sin, radians


class Vector:

    def __init__(self, x: int | float, y: int | float) -> None:
        self.x = round(float(x), 2)
        self.y = round(float(y), 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(
            x=self.x + other.x,
            y=self.y + other.y
        )

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(
            x=self.x - other.x,
            y=self.y - other.y
        )

    def __mul__(self, other: Union["Vector", int, float]) -> (
            Union)["Vector", int, float]:

        if isinstance(other, (int, float)):
            return Vector(
                x=self.x * other,
                y=self.y * other
            )
        elif isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        else:
            raise TypeError("Operand must be a Vector instance or a number.")

    start_point = tuple()
    end_point = tuple()

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple[float, float], end_point: tuple[float, float]) -> "Vector":
        if len(start_point) < 2 or len(end_point) < 2:
            raise ValueError("Both start_point and end_point must have at least two elements.")

        x = end_point[0] - start_point[0]
        y = end_point[1] - start_point[1]

        return cls(x,y)

    def get_length(self) -> int | float:
        return sqrt((self.x ** 2) + (self.y ** 2))

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        return Vector(
            x=round(self.x / length, 2),
            y=round(self.y / length, 2)
        )

    def angle_between(self, other: "Vector") -> int :
        scalar_mult = (self.x * other.x) + (self.y * other.y)
        self_length = self.get_length()
        other_length = other.get_length()
        cos_a = scalar_mult / (self_length * other_length)
        result = degrees(acos(cos_a))
        return int(result) + (result > int(result))

    def get_angle(self) -> int:
        self_length = self.get_length()
        cos_a = self.y / self_length
        return int(degrees(acos(cos_a)))

    def rotate(self, degree: int) -> "Vector":
        rad_degree = radians(degree)
        a = (self.x * cos(rad_degree)) - (self.y * sin(rad_degree))
        b = (self.x * sin(rad_degree)) + (self.y * cos(rad_degree))
        return Vector(
            x=round(a, 2),
            y=round(b, 2)
        )
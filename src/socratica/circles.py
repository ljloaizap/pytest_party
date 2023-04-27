"""Placeholder module"""
from math import pi


def get_circle_area(radius):
    """Placeholder function"""
    if type(radius) not in [int, float]:
        raise TypeError("The radius must be a non-negative real value.")
    if radius < 0:
        raise ValueError("The radius cannot negative value.")
    return pi*(radius**2)


# # Testing
# radii = [2, 0, -3, 2 + 5j, True, "radius"]
# MSG = "Area of circles with r = {0} is {1}"

# for r in radii:
#     A = get_circle_area(r)
#     print(MSG.format(r, A))

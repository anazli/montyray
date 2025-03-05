import numpy as np

from montyray.math_tools.vector3d import Vector3D
from montyray.math_tools.vector2d import Vector2D
from montyray.math_tools.vector4d import Vector4D
from montyray.math_tools.point3d import Point3D


def dot(elem1, elem2):
    """dot product of two math entities"""
    if (
        (isinstance(elem1, Vector2D) and isinstance(elem2, Vector2D))
        or (isinstance(elem1, Vector3D) and isinstance(elem2, Vector3D))
        or (isinstance(elem1, Vector4D) and isinstance(elem2, Vector4D))
    ):
        return np.dot(elem1.coordinates, elem2.coordinates)
    else:
        raise TypeError("Cannot calculate the dot product of the given elements!")


def cross(elem1, elem2):
    """cross product of two math entities"""
    if isinstance(elem1, Vector2D) and isinstance(elem2, Vector2D):
        new_data = np.cross(elem1.coordinates, elem2.coordinates)
        ret = Vector2D()
        ret.coordinates = new_data
        return ret
    elif isinstance(elem1, Vector3D) and isinstance(elem2, Vector3D):
        new_data = np.cross(elem1.coordinates, elem2.coordinates)
        ret = Vector3D()
        ret.coordinates = new_data
        return ret
    elif isinstance(elem1, Vector4D) and isinstance(elem2, Vector4D):
        new_data = np.cross(elem1.coordinates, elem2.coordinates)
        ret = Vector4D()
        ret.coordinates = new_data
        return ret
    else:
        raise TypeError("Cannot calculate the cross product of the given elements!")

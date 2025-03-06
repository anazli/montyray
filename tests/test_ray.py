import unittest

import numpy as np

from raymann.math_tools.ray import Ray
from raymann.math_tools.vector3d import Vector3D
from raymann.math_tools.point3d import Point3D
from raymann.math_tools.math_utils import translation_matrix, scale_matrix
from raymann.transformation.transformer import Transformer


class TestRay(unittest.TestCase):

    def test_ray(self):
        o = Point3D(2, 3, 4)
        d = Vector3D(1, 0, 0)
        ray = Ray(origin=o, direction=d)

        self.assertEqual(o, ray.origin)
        self.assertEqual(d, ray.direction)

        self.assertEqual(o, ray.position(0))
        self.assertEqual(Point3D(3, 3, 4), ray.position(1))
        self.assertEqual(Point3D(1, 3, 4), ray.position(-1))
        self.assertEqual(Point3D(4.5, 3, 4), ray.position(2.5))

    def test_ray_translation(self):
        ray = Ray(origin=Point3D(1, 2, 3), direction=Vector3D(0, 1, 0))
        m = translation_matrix(3, 4, 5)
        t = Transformer(m.inverse)
        transformed_ray = t.world_to_obj_space(ray)

        self.assertEqual(Point3D(4, 6, 8), transformed_ray.origin)
        self.assertEqual(Vector3D(0, 1, 0), transformed_ray.direction)

    def test_ray_scaling(self):
        ray = Ray(origin=Point3D(1, 2, 3), direction=Vector3D(0, 1, 0))
        m = scale_matrix(2, 3, 4)
        t = Transformer(m.inverse)
        transformed_ray = t.world_to_obj_space(ray)

        self.assertEqual(Point3D(2, 6, 12), transformed_ray.origin)
        self.assertEqual(Vector3D(0, 3, 0), transformed_ray.direction)


if __name__ == "__main__":
    unittest.main()

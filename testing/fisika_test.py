import numpy as np
import unittest

from OpenSeries.fisika import kecepatan


class TestKecepatan(unittest.TestCase):
    def test_angka_valid(self):
        hasil = kecepatan(100.0, 10.0)
        self.assertEqual(hasil, 10.0)

    def test_angka_list(self):
        hasil = kecepatan([20, 30, 40], [20, 30, 40])
        self.assertEqual(hasil, [1.0, 1.0, 1.0])

    def test_numpy_list(self):
        hasil = kecepatan(np.array([20, 30, 40]), np.array([20, 30, 40]))
        self.assertEqual(hasil, [1.0, 1.0, 1.0])

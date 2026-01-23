import numpy as np
import unittest
from seabird_sampling.get_effort import get_effort


class Test_get_effort(unittest.TestCase):
    def setUp(self):
        """
        Crea variables que se usarán en las pruebas
        """
        self.data_in: list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.data_out: np.array = np.array([3, 6, 9])

    def test_get_effort(self):
        assert all([a == b for a, b in zip(get_effort(self.data_in), self.data_out)])


if __name__ == "__main__":
    unittest.main()

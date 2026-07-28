import unittest

from utils import classify


class TestInventory(unittest.TestCase):

    def test_hot(self):

        obj = {
            "temperature_c": 55,
            "color": "red",
            "shape": "cube"
        }

        self.assertEqual(classify(obj), "hot_bin")


    def test_red(self):

        obj = {
            "temperature_c": 20,
            "color": "red",
            "shape": "cube"
        }

        self.assertEqual(classify(obj), "red_bin")


if __name__ == "__main__":
    unittest.main()

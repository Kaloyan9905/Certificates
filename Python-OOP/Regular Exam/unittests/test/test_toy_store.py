import unittest
from unittests.toy_store import ToyStore


class ToyStoreTest(unittest.TestCase):
    def setUp(self) -> None:
        self.toy_shelf_obj = ToyStore()
        self.toy_shelf = {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }

    def test_init_method(self):
        self.assertEqual(None, self.toy_shelf["A"])
        self.assertEqual(None, self.toy_shelf["B"])
        self.assertEqual(None, self.toy_shelf["C"])
        self.assertEqual(None, self.toy_shelf["D"])
        self.assertEqual(None, self.toy_shelf["E"])
        self.assertEqual(None, self.toy_shelf["F"])
        self.assertEqual(None, self.toy_shelf["G"])

    def test_add_toy_method(self):
        result = self.toy_shelf_obj.add_toy("A", "Car")
        self.assertEqual(f"Toy:Car placed successfully!", result)
        self.assertEqual("Car", self.toy_shelf_obj.toy_shelf["A"])

        with self.assertRaises(Exception) as ex:
            self.toy_shelf_obj.add_toy("K", "Bear")
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            self.toy_shelf_obj.add_toy("A", "Car")
        self.assertEqual("Toy is already in shelf!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            self.toy_shelf_obj.add_toy("A", "Doll")
        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_remove_toy_method(self):
        self.toy_shelf_obj.add_toy("A", "Bear")
        result = self.toy_shelf_obj.remove_toy("A", "Bear")
        self.assertEqual(f"Remove toy:Bear successfully!", result)
        self.assertEqual(None, self.toy_shelf_obj.toy_shelf["A"])

        with self.assertRaises(Exception) as ex:
            self.toy_shelf_obj.remove_toy("L", "Dinosaur")
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

        self.toy_shelf_obj.add_toy("D", "Laptop")
        with self.assertRaises(Exception) as ex:
            self.toy_shelf_obj.remove_toy("D", "PC")
        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))


if __name__ == "__main__":
    unittest.main()
from unittest import TestCase

from project.plantation import Plantation

class PlantationTest(TestCase):
    def setUp(self):
        self.plantation = Plantation(2)

    def test_constructor(self):
        self.assertEqual(2, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test_size_is_negative_raises(self):
        with self.assertRaises(ValueError) as ex:
            Plantation(-1)
        self.assertEqual("Size must be positive number!", str(ex.exception))

    def test_hire_workers(self):
        self.assertEqual([], self.plantation.workers)
        self.assertEqual(0, len(self.plantation.workers))

        result = self.plantation.hire_worker("Test")

        self.assertEqual(["Test"], self.plantation.workers)
        self.assertEqual(1, len(self.plantation.workers))

        self.assertEqual(f"Test successfully hired.", result)

    def test_hire_worker_that_exists(self):
        self.plantation.hire_worker("Test")

        self.assertEqual(["Test"], self.plantation.workers)
        self.assertEqual(1, len(self.plantation.workers))

        with self.assertRaises(ValueError) as ex:
            self.plantation.hire_worker("Test")
        self.assertEqual("Worker already hired!", str(ex.exception))

    def test_length(self):
        pass

    def test_planting_worker_does_exist_raises(self):
        self.plantation.hire_worker("Test")

        with self.assertRaises(ValueError) as ex:
            self.plantation.planting("Not existing", "rose")
        self.assertEqual(f"Worker with name Not existing is not hired!", str(ex.exception))

    def test_planting_plantation_is_full_raises(self):
        pass

    def test_planting(self):
        self.plantation.hire_worker("Test")

        self.plantation.planting("Test", "Rose")

        self.assertEqual({"Test": ["Rose"]}, self.plantation.plants)




# import unittest
#
# from project.plantation import Plantation
#
#
# class TestPlantation(unittest.TestCase):
#     def setUp(self):
#         self.plantation = Plantation(5)
#
#     def test_initialization(self):
#         self.assertEqual(self.plantation.size, 5)
#         self.assertEqual(self.plantation.plants, {})
#         self.assertEqual(self.plantation.workers, [])
#
#     def test_size_setter_positive(self):
#         self.plantation.size = 10
#         self.assertEqual(self.plantation.size, 10)
#
#     def test_size_setter_negative(self):
#         with self.assertRaises(ValueError) as ex:
#             self.plantation.size = -1
#         self.assertEqual(str(ex.exception), "Size must be positive number!")
#
#     def test_hire_worker_success(self):
#         result = self.plantation.hire_worker("Alice")
#         self.assertEqual(result, "Alice successfully hired.")
#         self.assertIn("Alice", self.plantation.workers)
#
#     def test_hire_worker_already_hired(self):
#         self.plantation.hire_worker("Alice")
#         with self.assertRaises(ValueError) as ex:
#             self.plantation.hire_worker("Alice")
#         self.assertEqual(str(ex.exception), "Worker already hired!")
#
#     def test_len_no_plants(self):
#         self.assertEqual(len(self.plantation), 0)
#
#     def test_len_with_plants(self):
#         self.plantation.hire_worker("Alice")
#         self.plantation.planting("Alice", "Rose")
#         self.assertEqual(len(self.plantation), 1)
#
#     def test_planting_worker_not_hired(self):
#         with self.assertRaises(ValueError) as ex:
#             self.plantation.planting("Bob", "Rose")
#         self.assertEqual(str(ex.exception), "Worker with name Bob is not hired!")
#
#     def test_planting_success(self):
#         self.plantation.hire_worker("Alice")
#         result = self.plantation.planting("Alice", "Rose")
#         self.assertEqual(result, "Alice planted it's first Rose.")
#         self.assertIn("Alice", self.plantation.plants)
#         self.assertIn("Rose", self.plantation.plants["Alice"])
#
#     def test_planting_additional_plant(self):
#         self.plantation.hire_worker("Alice")
#         self.plantation.planting("Alice", "Rose")
#         result = self.plantation.planting("Alice", "Tulip")
#         self.assertEqual(result, "Alice planted Tulip.")
#         self.assertIn("Tulip", self.plantation.plants["Alice"])
#
#     def test_planting_plantation_full(self):
#         self.plantation = Plantation(1)
#         self.plantation.hire_worker("Alice")
#         self.plantation.planting("Alice", "Rose")
#         with self.assertRaises(ValueError) as ex:
#             self.plantation.planting("Alice", "Tulip")
#         self.assertEqual(str(ex.exception), "The plantation is full!")
#
#     def test_str_method(self):
#         self.plantation.hire_worker("Alice")
#         self.plantation.planting("Alice", "Rose")
#         expected_output = "Plantation size: 5\nAlice\nAlice planted: Rose"
#         self.assertEqual(str(self.plantation), expected_output)
#
#     def test_repr_method(self):
#         self.plantation.hire_worker("Alice")
#         expected_output = "Size: 5\nWorkers: Alice"
#         self.assertEqual(repr(self.plantation), expected_output)
#
if __name__ == "__main__":
    unittest.main()
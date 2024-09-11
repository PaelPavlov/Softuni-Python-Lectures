import unittest
from project.tennis_player import TennisPlayer


class TestTennisPlayer(unittest.TestCase):
    def setUp(self):
        self.player_1 = TennisPlayer("Dimitrov", 33, 3770)
        self.player_2 = TennisPlayer("Djokovic", 37, 8460)
        self.player_3 = TennisPlayer("Rune", 21, 2300)

    def test_correct_init(self):
        self.assertEqual("Dimitrov", self.player_1.name)
        self.assertEqual(33, self.player_1.age)
        self.assertEqual(3770, self.player_1.points)
        self.assertEqual([], self.player_1.wins)

    def test_shorter_name_should_raise_error(self):
        with self.assertRaises(ValueError) as e:
            TennisPlayer("Aa", 21, 3300)
        self.assertEqual("Name should be more than 2 symbols!", str(e.exception))

    def test_valid_age(self):
        with self.assertRaises(ValueError) as e:
            TennisPlayer("Asd", 13, 1400)
        self.assertEqual("Players must be at least 18 years of age!", str(e.exception))

    def test_add_new_win_not_existing_should_add(self):
        result = self.player_1.add_new_win("Brisbane 2024")
        self.assertEqual(["Brisbane 2024"], self.player_1.wins)
        self.assertIsNone(result)

    def test_add_new_win_existing_should_not_add(self):
        self.player_1.add_new_win("Brisbane 2024")
        result = self.player_1.add_new_win("Brisbane 2024")
        self.assertEqual(f"Brisbane 2024 has been already added to the list of wins!", result)

    def test_lt_should_return_first_player_is_better(self):
        result = self.player_1 < self.player_3
        self.assertEqual("Dimitrov is a better player than Rune", result)

    def test_lt_should_return_other_player_is_better(self):
        result = self.player_1 < self.player_2
        self.assertEqual("Djokovic is a top seeded player and he/she is better than Dimitrov", result)

    def test_str_no_wins(self):
        result = str(self.player_1)
        self.assertEqual("Tennis Player: Dimitrov\nAge: 33\nPoints: 3770.0\nTournaments won: ", result)

    def test_str_with_wins(self):
        self.player_1.add_new_win("Brisbane 2024")
        self.player_1.add_new_win("ATP 2034")
        result = str(self.player_1)
        self.assertEqual("Tennis Player: Dimitrov\nAge: 33\nPoints: 3770.0\nTournaments won: Brisbane 2024, ATP 2034", result)

if __name__ == "__main__":
    unittest.main()

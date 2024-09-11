from project.soccer_player import SoccerPlayer

import unittest

class TestSoccerPlayer(unittest.TestCase):
    def setUp(self):
        self.player1 = SoccerPlayer("Neymar", 32, 26, "Barcelona")
        self.player2 = SoccerPlayer("Kylian Mbappe", 25, 40, "PSG")

    def test_name_validation(self):
        with self.assertRaises(ValueError) as context:
            self.player1.name = "Ney"
        self.assertEqual(str(context.exception), "Name should be more than 5 symbols!")

    def test_age_validation(self):
        with self.assertRaises(ValueError) as context:
            self.player1.age = 15
        self.assertEqual(str(context.exception), "Players must be at least 16 years of age!")

    def test_goals_setter_positive(self):
        self.player1.goals = 50
        self.assertEqual(self.player1.goals, 50)

    def test_goals_setter_negative(self):
        self.player1.goals = -10
        self.assertEqual(self.player1.goals, 0)

    def test_team_validation(self):
        with self.assertRaises(ValueError) as context:
            self.player1.team = "Spartak Varna"
        self.assertEqual(
            str(context.exception),
            "Team must be one of the following: Barcelona, Real Madrid, Manchester United, Juventus, PSG!"
        )

    def test_change_team_success(self):
        result = self.player1.change_team("PSG")
        self.assertEqual(self.player1.team, "PSG")
        self.assertEqual(result, "Team successfully changed!")

    def test_change_team_failure(self):
        result = self.player1.change_team("Spartak Varna")
        self.assertEqual(result, "Invalid team name!")

    def test_add_new_achievement_first_time(self):
        result = self.player1.add_new_achievement("Golden Ball")
        self.assertEqual(self.player1.achievements["Golden Ball"], 1)
        self.assertEqual(result, "Golden Ball has been successfully added to the achievements collection!")

    def test_add_new_achievement_multiple_times(self):
        self.player1.add_new_achievement("Golden Ball")
        self.player1.add_new_achievement("Golden Ball")
        self.assertEqual(self.player1.achievements["Golden Ball"], 2)

    def test_less_than_operator(self):
        result = self.player1 < self.player2
        self.assertEqual(result, "Kylian Mbappe is a top goal scorer! S/he scored more than Neymar.")

        result = self.player2 < self.player1
        self.assertEqual(result, "Kylian Mbappe is a better goal scorer than Neymar.")

if __name__ == '__main__':
    unittest.main()

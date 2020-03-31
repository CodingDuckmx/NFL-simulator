from game import Game


import unittest
class TestGame(unittest.TestCase):

    def test_touchdown(self):
        game1 = Game(['Atlanta Falcons', 'Baltimore Ravens'])
        game1.touchdown(team='Baltimore Ravens',extra_point=2)
        self.assertEqual(game1.score, {'Atlanta Falcons':0, 'Baltimore Ravens':8} )

    def test_field_goal(self):
        game1 = Game(['Atlanta Falcons', 'Baltimore Ravens'])
        game1.field_goal(team='Atlanta Falcons')
        self.assertEqual(game1.score, {'Atlanta Falcons':3, 'Baltimore Ravens':0} )

    def test_safety(self):
        game1 = Game(['Atlanta Falcons', 'Baltimore Ravens'])
        game1.safety(team='Baltimore Ravens')
        self.assertEqual(game1.score, {'Atlanta Falcons':2, 'Baltimore Ravens':0} )

    def test_get_winning_team(self):
        game1 = Game(['Atlanta Falcons', 'Baltimore Ravens'])   
        game1.touchdown(team='Baltimore Ravens',extra_point=2)  
        winner = game1.get_winning_team()[0]
        self.assertTrue(winner == 'Baltimore Ravens')

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

if __name__ == '__main__':
    unittest.main()

import unittest
import game  # Assumes your main game logic is in hashGame.py

class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        self.tic_tac_toe = game.TicTacToe()

    def test_start(self):
        self.tic_tac_toe.start()
        self.assertTrue(self.tic_tac_toe.player_X)
        self.assertTrue(self.tic_tac_toe.game_active)

    def test_end_game(self):
        self.tic_tac_toe.end_game()
        self.assertFalse(self.tic_tac_toe.game_active)

    def test_switch_player(self):
        self.tic_tac_toe.start()
        self.tic_tac_toe.switch_player()
        self.assertFalse(self.tic_tac_toe.player_X)
        self.assertTrue(self.tic_tac_toe.player_O)

    def test_get_status(self):
        self.assertEqual(self.tic_tac_toe.get_status(), self.tic_tac_toe.game_active)

    def test_select_player_X(self):
        self.tic_tac_toe.select_player(1)
        self.assertTrue(self.tic_tac_toe.player_X)
        self.assertFalse(self.tic_tac_toe.player_O)

    def test_select_player_O(self):
        self.tic_tac_toe.select_player(2)
        self.assertFalse(self.tic_tac_toe.player_X)
        self.assertTrue(self.tic_tac_toe.player_O)

    def test_is_position_free(self):
        self.tic_tac_toe.board_positions[0] = True
        self.assertFalse(self.tic_tac_toe.is_position_free(0))
        self.assertTrue(self.tic_tac_toe.is_position_free(1))

    def test_select_position(self):
        self.tic_tac_toe.start()
        self.tic_tac_toe.select_position(1)
        self.assertTrue(self.tic_tac_toe.board_positions[1])
        self.assertTrue(self.tic_tac_toe.player_one_positions[1])
        self.assertFalse(self.tic_tac_toe.player_two_positions[1])

    def test_check_win_possibility(self):
        self.tic_tac_toe.start()
        self.tic_tac_toe.select_position(0)
        self.tic_tac_toe.select_position(1)
        self.tic_tac_toe.select_position(2)
        self.assertTrue(self.tic_tac_toe.check_win_possibility([0, 1, 2]))

    def test_check_all_win_possibilities(self):
        self.tic_tac_toe.start()
        self.tic_tac_toe.select_position(6)
        self.tic_tac_toe.select_position(7)
        self.tic_tac_toe.select_position(8)
        self.assertTrue(self.tic_tac_toe.check_all_win_possibilities())
        self.tic_tac_toe.clear_board()
        self.tic_tac_toe.select_position(2)
        self.tic_tac_toe.select_position(5)
        self.tic_tac_toe.select_position(1)
        self.assertFalse(self.tic_tac_toe.check_all_win_possibilities())

    def test_clear_board(self):
        self.tic_tac_toe.select_position(1)
        self.tic_tac_toe.clear_board()
        self.assertFalse(self.tic_tac_toe.board_positions[1])

    def test_is_draw(self):
        for i in range(9):
            self.tic_tac_toe.select_position(i)
        self.assertTrue(self.tic_tac_toe.is_draw())
        self.tic_tac_toe.clear_board()
        self.assertFalse(self.tic_tac_toe.is_draw())

    def test_not_first_move(self):
        self.tic_tac_toe.select_position(1)
        self.assertTrue(self.tic_tac_toe.not_first_move())
        self.tic_tac_toe.clear_board()
        self.assertFalse(self.tic_tac_toe.not_first_move())


if __name__ == '__main__':
    unittest.main()

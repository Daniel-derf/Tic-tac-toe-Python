import unittest
import game  # Assumes your main game code is saved in hashGame.py
from unittest.mock import patch


class SupportMethods():
    def __init__(self):
        self.terminal_tic_tac_toe = game.TerminalTicTacToe()

    def force_draw(self):
        self.terminal_tic_tac_toe.start()
        for i in [0, 2, 5, 6, 7]:
            self.terminal_tic_tac_toe.select_position(i)
        self.terminal_tic_tac_toe.switch_player()
        for i in [1, 3, 4, 8]:
            self.terminal_tic_tac_toe.select_position(i)

    def make_player_X_win(self):
        self.terminal_tic_tac_toe.start()
        for i in [0, 1, 2]:
            self.terminal_tic_tac_toe.select_position(i)

    def make_player_O_win(self):
        for i in [0, 1, 2]:
            self.terminal_tic_tac_toe.select_position(i)


class TestTerminalTicTacToe(unittest.TestCase, SupportMethods):
    def setUp(self):
        self.terminal_tic_tac_toe = game.TerminalTicTacToe()

    def test_check_draw(self):
        self.force_draw()
        self.assertTrue(self.terminal_tic_tac_toe.check_draw())
        self.terminal_tic_tac_toe.clear_board()
        self.assertFalse(self.terminal_tic_tac_toe.check_draw())

    def test_check_winner(self):
        self.make_player_X_win()
        self.assertTrue(self.terminal_tic_tac_toe.check_winner())
        self.terminal_tic_tac_toe.clear_board()
        self.assertFalse(self.terminal_tic_tac_toe.check_winner())
        self.make_player_O_win()
        self.assertTrue(self.terminal_tic_tac_toe.check_winner())

    def test_game_ended(self):
        self.force_draw()
        self.assertTrue(self.terminal_tic_tac_toe.game_ended())
        self.terminal_tic_tac_toe.clear_board()
        self.assertFalse(self.terminal_tic_tac_toe.game_ended())
        self.make_player_X_win()
        self.assertTrue(self.terminal_tic_tac_toe.game_ended())

    def test_mark_visual_board(self):
        self.terminal_tic_tac_toe.start()
        self.terminal_tic_tac_toe.mark_visual_board(0)
        self.assertEqual(self.terminal_tic_tac_toe.visual_board[0], 'X')
        self.terminal_tic_tac_toe.switch_player()
        self.terminal_tic_tac_toe.mark_visual_board(1)
        self.assertEqual(self.terminal_tic_tac_toe.visual_board[1], 'O')

    def test_validate_position_not_taken(self):
        self.terminal_tic_tac_toe.move = 0
        self.assertTrue(self.terminal_tic_tac_toe.validate_position_not_taken())
        self.terminal_tic_tac_toe.make_move()
        with self.assertRaises(ValueError):
            self.terminal_tic_tac_toe.validate_position_not_taken()

    def test_validate_position_range(self):
        self.terminal_tic_tac_toe.move = 0
        self.assertTrue(self.terminal_tic_tac_toe.validate_position_range())
        self.terminal_tic_tac_toe.move = 10
        with self.assertRaises(ValueError):
            self.terminal_tic_tac_toe.validate_position_range()

    def test_display_current_player(self):
        self.terminal_tic_tac_toe.start()

        with patch('builtins.print') as mock_print:
            self.terminal_tic_tac_toe.display_current_player()
            mock_print.assert_called_with("Player ONE")

        self.terminal_tic_tac_toe.switch_player()

        with patch('builtins.print') as mock_print:
            self.terminal_tic_tac_toe.display_current_player()
            mock_print.assert_called_with("Player TWO")

    @patch('builtins.input', side_effect=['5'])
    def test_ask_for_move_and_validate(self, mock_input):
        self.assertTrue(self.terminal_tic_tac_toe.ask_for_move_and_validate())


if __name__ == '__main__':
    unittest.main()

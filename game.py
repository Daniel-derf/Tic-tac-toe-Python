class TicTacToe:
    def __init__(self):
        self.player_one_positions = [False] * 9
        self.player_two_positions = [False] * 9
        self.board_positions = [False] * 9
        self.player_X = False
        self.player_O = False
        self.game_active = False

    def start(self):
        self.player_X = True
        self.game_active = True

    def end_game(self):
        self.game_active = False

    def switch_player(self):
        if self.player_X:
            self.player_X = False
            self.player_O = True
        else:
            self.player_X = True
            self.player_O = False

    def get_status(self):
        return self.game_active

    def show_board(self):
        print('_' * 2 + '|' + '_' * 2 + '|' + '_' * 2 + '\n' +
              '_' * 2 + '|' + '_' * 2 + '|' + '_' * 2 + '\n' +
              ' ' * 2 + '|' + ' ' * 2 + '|' + ' ' * 2)

    def select_player(self, player_number):
        if player_number == 1:
            self.player_X = True
        else:
            self.player_O = True

    def is_position_free(self, position):
        return self.board_positions[position] is False

    def select_position(self, position):
        if self.player_X:
            self.player_one_positions[position] = True
        else:
            self.player_two_positions[position] = True
        self.board_positions[position] = True

    def check_win_possibility(self, win_positions):
        return all(self.player_one_positions[pos] for pos in win_positions) or \
               all(self.player_two_positions[pos] for pos in win_positions)

    def check_all_win_possibilities(self):
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for combination in win_combinations:
            if self.check_win_possibility(combination):
                return True
        return False

    def clear_board(self):
        self.player_one_positions = [False] * 9
        self.player_two_positions = [False] * 9
        self.board_positions = [False] * 9

    def is_draw(self):
        return not False in self.board_positions

    def not_first_move(self):
        return True in self.board_positions


class TerminalTicTacToe(TicTacToe):
    def __init__(self):
        super().__init__()
        self.visual_board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.move = -1
        self.position_is_free = True

    def play(self):
        self.start()
        while self.get_status():
            self.continue_game()
            self.game_ended()

    def continue_game(self):
        if self.not_first_move():
            self.switch_player()
        self.choose_move()

    def choose_move(self):
        self.display_board()
        self.display_current_player()

        valid_move = self.ask_for_move_and_validate()
        if valid_move:
            self.make_move()
        else:
            self.choose_move()

    def display_board(self):
        print(self.visual_board[0:3])
        print(self.visual_board[3:6])
        print(self.visual_board[6:])

    def display_current_player(self):
        if self.player_X:
            print('Player ONE')
        else:
            print('Player TWO')

    def ask_for_move_and_validate(self):
        try:
            self.move = int(input('Enter the position to be filled (1-9):\n'))
            self.move -= 1
            self.validate_position_range()
            self.validate_position_not_taken()
            return True
        except ValueError:
            if self.position_is_free:
                print('Invalid move! Select an integer between 1 and 9.')
            else:
                print('Board position already taken, try again!')
            return False

    def validate_position_range(self):
        if 0 <= self.move < 9:
            return True
        raise ValueError()

    def validate_position_not_taken(self):
        if self.is_position_free(self.move):
            return True
        self.position_is_free = False
        raise ValueError()

    def make_move(self):
        self.select_position(self.move)
        self.mark_visual_board(self.move)

    def mark_visual_board(self, position):
        if self.player_X:
            self.visual_board[position] = 'X'
        else:
            self.visual_board[position] = 'O'

    def game_ended(self):
        if self.check_winner() or self.check_draw():
            self.end_game()
            return True

    def check_winner(self):
        if self.check_all_win_possibilities():
            if self.player_X:
                print('Player ONE wins!')
            else:
                print('Player TWO wins!')
            return True
        else:
            return False

    def check_draw(self):
        if self.is_draw():
            print('It\'s a draw!')
            return True


def game():
    first_game = TerminalTicTacToe()
    first_game.play()

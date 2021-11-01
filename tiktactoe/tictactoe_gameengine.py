class TictactoeGameEngine:
    def __init__(self):
        self.board = list(['.'] * 9) # ['.', '.', '.', '.', '.', '.', '.', '.', '.']
        self.turn = 'X'

    def show_board(self):  # 김유임 : 우리 조
        # print('  '.join(self.board[0:3]))  # '  '.join(['.', '.', '.'])
        # print('  '.join(self.board[3:6]))
        # print('  '.join(self.board[6:9]))

        for i, v in enumerate(self.board):
            print(v + '  ', end='')
            if i % 3 == 2:
                print()

    def set(self, row, cal):
        # self.board에 self.turn
        # input -> 자리 -> output : row, cal -> 자리 -> index
        # row, cal -> index
        index = (row - 1) * 3 + (cal - 1)
        self.board[index] = self.turn

    def position_to_index(self, row, cal):
        return (row - 1) * 3 + (cal - 1)

    def set_winner(self):
        # 가로 - 3줄
        for row in range(1, 3 + 1):
            if self.board[self.position_to_index(row, 1)] \
                    == self.board[self.position_to_index(row, 2)] \
                    == self.board[self.position_to_index(row, 3)] \
                    == self.turn:
                return '-'

        # 세로 | 3줄
        for cal in range(1, 3 + 1):
            if self.board[self.position_to_index(1, cal)] \
                    == self.board[self.position_to_index(2, cal)] \
                    == self.board[self.position_to_index(1, cal)] \
                    == self.turn:
                return '|'

        # 대각선 / 1줄
        if self.board[self.position_to_index(1, 3)] \
                == self.board[self.position_to_index(2, 2)] \
                == self.board[self.position_to_index(1, 1)] \
                == self.turn:
            return '\''

        # 대각선 \ 1줄
        if self.board[self.position_to_index(1, 1)] \
                == self.board[self.position_to_index(2, 2)] \
                == self.board[self.position_to_index(3, 3)] \
                == self.turn:
            return '/'

        # 가로 - 3줄
        # 세로 | 3줄
        # 대각선 / or \ 2줄
        # 무승부 : 위의 조건 통과 or 놓을 자리가 없음(self.board에 빈칸이 없음 or self.board에 '.'가 없음)
        # - 3줄 : 1,2,3 | 4,5,6 | 7,8,9

        # - 3줄 : 1,2,3 | 4,5,6 | 7,8,9
        for i in range(0, 7):
            if i == 0 or i == 3 or i == 6:
                if self.board[i] == self.board[i + 1] == self.board[i + 2]:
                    print("-")
        # | 3줄 1,4,7 | 2,5,8 | 3,6,9
        for i in range(0, 3):
            if i == 0 or i == 1 or i == 2:
                if self.board[i] == self.board[i + 3] == self.board[i + 6]:
                    print("|")

        # /
        if self.board[2] == 'X' and self.board[4] == 'X' and self.board[6] == 'X':
            return print('X 승리')
        # \
        if self.board[0] == 'X' and self.board[4] == 'X' and self.board[8] == 'X':
            return print('X 승리')

        # 끝나는 경우 : 무승부(승자가 없는 상태로 놓을 자리가 없음), 승자 결정(승자가 있음)
        if self.board[0] != '.' and self.board[1] != '.' and self.board[2] != '.' and \
                self.board[3] != '.' and self.board[4] != '.' and self.board[5] != '.' and \
                self.board[6] != '.' and self.board[7] != '.' and self.board[8] != '.':
            return print('무승부')

    def change_turn(self):
        pass

if __name__ == '__main__':
    game_engine = TictactoeGameEngine()
    game_engine.show_board()  # ...\n...\n...
    print()
    game_engine.set(2, 2)
    game_engine.show_board()  # ['.', '.', '.', '.', 'X', '.', '.', '.', '.']
    print()
    game_engine.set(2, 1)
    game_engine.set(2, 3)
    game_engine.show_board()  # ['.', '.', '.', 'X', 'X', 'X', '.', '.', '.']
    print()
    game_engine.board = ['.', '.', '.', 'X', 'X', 'X', '.', '.', '.']
    game_engine.show_board()
    game_engine.set_winner()  # '-' => 'X'
    game_engine.change_turn()
    # print(game_engine.turn)  # 'O'
    # game_engine.change_turn()
    # print(game_engine.turn)  # 'X'
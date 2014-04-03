import sys


class Board:
    def __init__(self, size):
        self.size = size
        self.reset()

    def reset(self):
        self.table = [['-'] * self.size] * self.size
        for i in range(self.size): self.table[i] = self.table[i] + []
        self.turn = 0
        self.winner = None
        self.move = 0

    def play(self, r, c):
        if r >= self.size or c >= self.size or self.table[r][c] != '-' or not self.not_over():
            return False
        else:
            self.table[r][c] = 'X' if self.turn == 0 else 'O'
            self.turn = 1 - self.turn
            self.check_for(r, c)
            self.move += 1
            return True

    def print_table(self):
        for row in self.table:
            for c in row:
                sys.stdout.write(c)
            print

    def not_over(self):
        return self.winner is None

    def check_for(self, r, c):
        if not self.not_over(): return;
        mark = self.table[r][c];

        for x in range(self.size):
            if self.table[r][x] != mark: break
            if x == self.size - 1: self.winner = 1 - self.turn; return

        for y in range(self.size):
            if self.table[y][c] != mark: break
            if y == self.size - 1: self.winner = 1 - self.turn; return

        if r == c:
            for d in range(self.size):
                if self.table[d][d] != mark: break
                if d == self.size - 1: self.winner = 1 - self.turn; return

        for a in range(self.size):
            if self.table[a][self.size - a - 1] != mark: break
            if a == self.size - 1: self.winner = 1 - self.turn; return

        if self.move == (self.size ** 2) - 1: self.winner = -1
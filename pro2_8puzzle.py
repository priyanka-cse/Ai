import random
import itertools
import collections

class Node:
    def __init__(self, puzzle, parent=None, action=None):
        self.puzzle = puzzle
        self.parent = parent
        self.action = action

    @property
    def state(self):
        return str(self)

    @property 
    def path(self):
        node, p = self, []
        while node:
            p.append(node)
            node = node.parent
        yield from reversed(p)

    @property
    def solved(self):
        return self.puzzle.solved

    @property
    def actions(self):
        return self.puzzle.actions

    def __str__(self):
        return str(self.puzzle)

class Solver:
    
    def __init__(self, start):
        self.start = start

    def solve(self):
       
        queue = collections.deque([Node(self.start)])
        seen  = set()
        seen.add(queue[0].state)
        while queue:
            node = queue.pop()
            if node.solved:
                return node.path

            for move, action in node.actions:
                child = Node(move(), node, action)

                if child.state not in seen:
                    queue.appendleft(child)
                    seen.add(child.state)

class Puzzle:
    
    def __init__(self, board):
        self.width = len(board[0])
        self.board = board

    @property
    def solved(self):
       
        N = self.width * self.width
        return str(self) == ''.join(map(str, range(1,N))) + '0'

    @property 
    def actions(self):
        
        def create_move(at, to):
            return lambda: self._move(at, to)

        moves = []
        for i, j in itertools.product(range(self.width),
                                      range(self.width)):
            direcs = {'R':(i, j-1),
                      'L':(i, j+1),
                      'D':(i-1, j),
                      'U':(i+1, j)}

            for action, (r, c) in direcs.items():
                if r >= 0 and c >= 0 and r < self.width and c < self.width and \
                   self.board[r][c] == 0:
                    move = create_move((i,j), (r,c)), action
                    moves.append(move)
        return moves

    def shuffle(self):
       
        puzzle = self
        for _ in range(1000):
            puzzle = random.choice(puzzle.actions)[0]()
        return puzzle

    def copy(self):
        
        board = []
        for row in self.board:
            board.append([x for x in row])
        return Puzzle(board)

    def _move(self, at, to):
        
        copy = self.copy()
        i, j = at
        r, c = to
        copy.board[i][j], copy.board[r][c] = copy.board[r][c], copy.board[i][j]
        return copy

    def pprint(self):
        for row in self.board:
            print(row)
        print()

    def __str__(self):
        return ''.join(map(str, self))

    def __iter__(self):
        for row in self.board:
            yield from row

    
board = [[1,2,3],[4,0,6],[7,5,8]]

puzzle = Puzzle(board)
puzzle = puzzle.shuffle()
s = Solver(puzzle)
p = s.solve()

for node in p:
    print(node.action)
    node.puzzle.pprint()

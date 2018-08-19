# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat:
    """ A rat caught in a maze. """

    # Write your Rat methods here.
    def __init__(self, symbol, row, col):
        """(Rat, str, int, int) -> NoneType

        Initialise a Rat

        >>> rat = Rat('P', 2, 3)
        >>> rat.symbol
        'P'
        >>> rat.row
        2
        >>> rat.col
        3
        >>> rat.num_sprouts_eaten
        0
        """

        self.symbol = symbol
        self.row = row
        self.col = col
        self.num_sprouts_eaten = 0

    def set_location(self, row, col):
        """(Rat, int, int) -> NoneType

        Set a Rat's location (row and column index)

        >>> rat = Rat('P', 4, 5)
        >>> rat.set_location(7, 8)
        >>> rat.row
        7
        >>> rat.col
        8
        """

        self.row = row
        self.col = col

    def eat_sprout(self):
        """(Rat) -> NoneType

        Increment number of sprouts eaten by 1

        >>> rat = Rat('P', 3, 4)
        >>> rat.num_sprouts_eaten
        0
        >>> rat.eat_sprout()
        >>> rat.num_sprouts_eaten
        1
        """

        self.num_sprouts_eaten += 1

    def __str__(self):
        """(Rat) -> str

        Pretty print a Rat

        >>> rat = Rat('S', 2, 3)
        >>> print(rat)
        S at (2, 3) ate 0 sprouts.
        >>> rat.eat_sprout()
        >>> rat.eat_sprout()
        >>> print(rat)
        S at (2, 3) ate 2 sprouts.
        """

        result = self.symbol + ' at (' + str(self.row) + ', ' + str(self.col) + \
                ') ate ' + str(self.num_sprouts_eaten) + ' sprouts.'

        return result


class Maze:
    """ A 2D maze. """

    # Write your Maze methods here.
    def __init__(self, maze, rat_1, rat_2):
        """(Maze, list of list of str, Rat, Rat) -> NoneType

        Initialize the maze's four instance variables:
        maze - contents of maze (walls, sprouts etc)
        rat_1 - first rat
        rat_2 - second rat
        num_sprouts_left - number of uneaten sprouts

        >>> maze = Maze([['#','#','#'],\
                         ['#','.','#'],\
                         ['#','@','#'],\
                         ['#','#','#']],\
                         Rat('J', 1, 1),\
                         Rat('G', 2, 1))
        >>> maze.maze[0][1]
        '#'
        >>> maze.maze[2][1]
        '@'
        >>> maze.rat_1.row
        1
        >>> maze.num_sprouts_left
        1
        """

        self.maze = maze
        self.rat_1 = rat_1
        self.rat_2 = rat_2
        self.num_sprouts_left = 0

        for item in sum(self.maze, []):
            if item == SPROUT:
                self.num_sprouts_left += 1

    def is_wall(self, row, col):
        """(Maze, int, int) -> bool

        Return True if and only if there is a wall at the given
        row and column of the maze

        >>> maze = Maze([['#','#','#'],\
                         ['#','.','#'],\
                         ['#','@','#'],\
                         ['#','#','#']],\
                         Rat('J', 1, 1),\
                         Rat('G', 2, 1))
        >>> maze.is_wall(0, 0)
        True
        >>> maze.is_wall(1, 1)
        False
        >>> maze.is_wall(2, 1)
        False
        """

        return self.maze[row][col] == WALL

    def get_character(self, row, col):
        """(Maze, int, int) -> str

        Return the character in the maze at the given row (row) and 
        column (col). If there's a rat at that location, return its character.

        >>> maze = Maze([['#','#','#'],\
                         ['#','.','#'],\
                         ['#','@','#'],\
                         ['#','#','#']],\
                         Rat('J', 1, 1),\
                         Rat('G', 2, 1))
        >>> maze.get_character(1, 0)
        '#'
        >>> maze.get_character(2, 1)
        'G'
        """

        if self.rat_1.row == row and self.rat_1.col == col:
            return self.rat_1.symbol
        elif self.rat_2.row == row and self.rat_2.col == col:
            return self.rat_2.symbol
        else:
            return self.maze[row][col]

    def move(self, rat, vert, horiz):
        """(Maze, Rat, int, int) -> bool

        Move Rat in Maze in the vertical direction given by vert and the
        horizontal direction given by horiz, unless there is a wall in the way.
        If Rat encounters a Brussels sprout, it eats it and the number of
        sprouts in Maze decremented accordingly.

        >>> rat_1 = Rat('J', 1, 1)
        >>> rat_2 = Rat('G', 2, 1)
        >>> maze = Maze([['#','#','#'],\
                         ['#','.','#'],\
                         ['#','@','#'],\
                         ['#','#','#']],\
                         rat_1,\
                         rat_2)
        >>> rat_1.num_sprouts_eaten
        0
        >>> maze.move(rat_1, DOWN, NO_CHANGE)
        True
        >>> rat_1.num_sprouts_eaten
        1
        >>> maze.num_sprouts_left
        0
        """

        new_row = rat.row + vert
        new_col = rat.col + horiz
        if self.is_wall(new_row, new_col):
            return False
        else:
            rat.set_location(new_row, new_col)
            if self.maze[new_row][new_col] == SPROUT:
                rat.eat_sprout()
                self.maze[new_row][new_col] = HALL
                self.num_sprouts_left -= 1
            return True

    def __str__(self):
        """(Maze) -> str

        Return string representation of maze, e.g.
        >>> rat_1 = Rat('J', 1, 1)
        >>> rat_2 = Rat('G', 2, 1)
        >>> maze = Maze([['#','#','#','#'],\
                         ['#','.','.','#'],\
                         ['#','.','@','#'],\
                         ['#','#','#','#']],\
                         rat_1,\
                         rat_2)
        >>> print(maze)
        ####
        #J.#
        #G@#
        ####
        J at (1, 1) ate 0 sprouts.
        G at (2, 1) ate 0 sprouts.
        """

        result = ''
        for row in range(len(self.maze)):
            for col in range(len(self.maze[row])):
                result += self.get_character(row, col)
            result += '\n'
        result += self.rat_1.__str__()
        result += '\n'
        result += self.rat_2.__str__()

        return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()

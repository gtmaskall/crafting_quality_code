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

if __name__ == '__main__':
    import doctest
    doctest.testmod()

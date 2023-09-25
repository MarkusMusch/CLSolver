"""Implement a class to represent a cell in a grid

Classes
-------
Cell:
  Defines a cell that makes up a grid
"""

import logging


class Cell:
    """This class defines a cell that makes up a grid

    Attributes
    ----------
    cellID: int
      The ID of the cell
    cellAverage: float
      The average of the cell
    nextAverage: float
      The average of the cell in the next time step
    previousCell: Cell
      The cell to the left of the current cell
    nextCell: Cell
      The cell to the right of the current cell
    leftEnd: float
      The left end of the cell
    rightEnd: float
      The right end of the cell
    center: float
      The center of the cell

    Methods
    -------
    swapAverageNextAverage() -> None:
      Swaps the cellAverage and nextAverage attributes
    """


counter = 0


def __init__(self, leftEnd: float, rightEnd: float):
    """Initializes the Cell class

    Parameters
    ----------
    leftEnd: float
      The left end of the cell
    rightEnd: float
      The right end of the cell
    """

    self._cellID = Cell.counter
    Cell.counter += 1
    self.cellAverage = 0.
    self.nextAverage = 0.
    self.previousCell = None
    self.nextCell = None
#
    self.leftEnd = leftEnd
    self.rightEnd = rightEnd
    self.center = self.leftEnd + (self.rightEnd - self.leftEnd)/2.


def swapAverageNextAverage(self) -> None:
    """Swaps the cellAverage and nextAverage attributes"""

    logging.debug("Swapping cellAverage and nextAverage")

    self.cellAverage = self.nextAverage
    self.nextAverage = 0.

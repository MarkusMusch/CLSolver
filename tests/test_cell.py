from ..src.cell import Cell


def test_swap_average_trivial():
    """Test the swapping of the current and the next average values"""

    cell = Cell(0, 1)

    assert cell.cellAverage == 0
    assert cell.nextAverage == 0

    cell.swapAverageNextAverage()

    assert cell.cellAverage == 0
    assert cell.nextAverage == 0


def test_swap_average():
    """Test the swapping of the current and the next average values"""

    cell = Cell(0, 1)

    assert cell.cellAverage == 0
    assert cell.nextAverage == 0

    cell.cellAverage = 1
    cell.nextAverage = 2

    assert cell.cellAverage == 1
    assert cell.nextAverage == 2

    cell.swapAverageNextAverage()

    assert cell.cellAverage == 2
    assert cell.nextAverage == 0

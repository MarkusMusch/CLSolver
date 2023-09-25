"""Main entry point for the application."""

import logging

from src.cell import Cell

logging.basicConfig(
    level=logging.DEBUG,  # Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

cell = Cell(0., 1.)

cell.swapAverageNextAverage()

"""
Optimiser base class

All optimiser classes should inherit from this class
"""
from abc import ABCMeta, abstractmethod
import numpy as np

class Optimiser(object):
    """
    :param y: The function to optimise
    :param x0: The starting position for the algorithm
    :param precision: The precision to calculate the minimum to
    :param steps: The max number of iterations of the algorithm to run
    """
    __metaclass__ = ABCMeta

    def __init__(self, y, x0, precision=1e-4, steps=10000):
        self.y = y
        self.xn = x0
        self.xn_1 = x0
        self.precision = precision
        self.steps = steps

    @abstractmethod
    def step(self):
        """Runs one iteration of the algorithm"""
        return

    def optimise(self):
        """Runs :func:`step` the specified number of times"""
        i = 0
        self.step()
        step_size = np.linalg.norm(self.xn - self.xn_1)
        while step_size > self.precision and i < self.steps:
            self.step()
            step_size = np.linalg.norm(self.xn - self.xn_1)
            i += 1
        return self.xn

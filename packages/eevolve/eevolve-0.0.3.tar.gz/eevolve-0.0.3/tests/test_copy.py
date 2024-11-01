import copy

import numpy
import pygame.transform

import eevolve
from eevolve import Brain

game = eevolve.Game((128, 72), (1280, 720), "Test Window",
                    numpy.full((128, 72, 3), (123, 123, 123)), 5)


def test() -> None:
    agent = eevolve.Agent((1, 1), (0, 0), "Agent",
                          numpy.full((1, 1, 3), (123, 123, 123)), Brain([]))


if __name__ == '__main__':
    test()

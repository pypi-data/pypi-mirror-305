import numpy

import eevolve

game = eevolve.Game((128, 72), (1280, 720), "Test Window",
                    numpy.full((128, 72, 3), (123, 123, 123)), 5)


def test() -> None:
    copies = 100
    game.add_agents(copies,
                    eevolve.AgentGenerator.default(game, copies),
                    eevolve.PositionGenerator.even(game, copies))
    game.run()


if __name__ == '__main__':
    test()

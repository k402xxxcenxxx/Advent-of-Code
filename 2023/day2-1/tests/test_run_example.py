from src.solver import solver

import os


def test_run_example():
    with open(os.path.join(os.path.dirname(__file__), "expected_result.txt"), "r") as fd:
        expected_result = int(fd.read())

    res = solver(os.path.join(os.path.dirname(__file__), "example.txt"), r=12, g=13, b=14)

    assert res == expected_result

import pythonworkflow


def test_a():
    assert pythonworkflow.tested_function(1, 1) == 12


def test_b():
    assert pythonworkflow.tested_function(1, 2) == 42

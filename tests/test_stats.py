from agent.stats import median


def test_median_even_length():
    assert median([10, 20, 30, 40]) == 25.0
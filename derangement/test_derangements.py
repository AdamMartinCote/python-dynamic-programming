import pytest

from derangement.derangement import (
    count_derangements,
    count_derangements_topdown,
    count_derangements_topdown2,
    count_derangements_topdown3,
    count_derangements_topdown4,
    count_derangements_bottomup,
    count_derangements_memory_optimized,
)


funcs = [
    count_derangements,
    count_derangements_topdown,
    count_derangements_topdown2,
    count_derangements_topdown3,
    count_derangements_topdown4,
    count_derangements_bottomup,
    count_derangements_memory_optimized,
]


@pytest.mark.parametrize("func", funcs)
@pytest.mark.parametrize(
    "n,expected",
    (
        (1, 0),
        (2, 1),
        (3, 2),
        (4, 9),
        (5, 44),
        (6, 265),
        (7, 1854),
        (8, 14833),
        (9, 133496),
    ),
)
def test_derangements(n, expected, benchmark, func) -> None:
    got = func(n)
    assert got == expected


@pytest.mark.parametrize("func", funcs)
@pytest.mark.benchmark
def test_derangement_performance(benchmark, func):
    n = 9
    got = benchmark(func, n)
    assert got == 133496

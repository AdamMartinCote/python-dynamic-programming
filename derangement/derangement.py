from array import array


def count_derangements(n: int):
    """
    Brute force recursion

    avg 113 kOps/s
    """
    if n == 1:
        return 0
    if n == 2:
        return 1
    return (
        # Derangements for the first element
        (n - 1)
        * (
            # Case where we didn't swap with the second element
            count_derangements(n - 1)
            +
            # Case where we swapped with the second element
            count_derangements(n - 2)
        )
    )


def count_derangements_topdown(n: int, memo=None):
    """count derangements topdown initial

    memoization implemented with a hashmap passed as argument
    This implementation performs worst than the brute force one with 68 kOps/s
    Hashmaps seem bad for memoization
    """
    if not memo:
        memo = {}
    if n == 1 or n == 0:
        return 0
    if n == 2:
        return 1
    if n not in memo:
        memo[n] = (n - 1) * (
            count_derangements_topdown(n - 1, memo)
            + count_derangements_topdown(n - 2, memo)
        )
    return memo[n]


def count_derangements_topdown2(n: int, sub_solutions=None):
    """count derangements topdown 2

    Memoization implemented with a list passed as parameter
    This provides a marginal improvement of 3x the brute force approach with 315 kOps/s
    """
    if not sub_solutions:
        sub_solutions = [-1] * (n + 1)
    if n == 1:
        return 0
    if n == 2:
        return 1
    if sub_solutions[n] == -1:
        sub_solutions[n] = (n - 1) * (
            count_derangements_topdown2(n - 1, sub_solutions)
            + count_derangements_topdown2(n - 2, sub_solutions)
        )
    return sub_solutions[n]


max_size = 64
memo = [-1] * max_size


def count_derangements_topdown3(n: int) -> int:
    """Count derangements topdown 3

    memoization is implemented with a list in the global namespace
    This is the most performant approach with 8122 kOps/s (25 faster than the
    hashmap-based memoization
    """
    if (res := memo[n]) != -1:
        return res
    if n <= 1:
        return 0
    if n == 2:
        return 1
    derangements = (n - 1) * (
        count_derangements_topdown3(n - 2) + count_derangements_topdown3(n - 1)
    )
    memo[n] = derangements
    return derangements


memo4 = array("I", [0] * max_size)


def count_derangements_topdown4(n: int) -> int:
    """Count derangements topdown 4

    Here, using a C array to implement the memoization does not improve the previous on
    the list-based version. The performance is a bit worst with 6388 kOps/s
    """
    if (res := memo4[n]) != 0:
        return res
    if n <= 1:
        return 0
    if n == 2:
        return 1
    derangements = (n - 1) * (
        count_derangements_topdown3(n - 2) + count_derangements_topdown3(n - 1)
    )
    memo4[n] = derangements
    return derangements


bottomup_memo = [-1] * max_size


def count_derangements_bottomup(n: int) -> int:
    # bottomup_memo[0] = 0
    # bottomup_memo[1] = 0
    # bottomup_memo[2] = 1
    for i in range(1, n + 1):
        if i == 1:
            bottomup_memo[i] = 0
        elif i == 2:
            bottomup_memo[i] = 1
        else:
            bottomup_memo[i] = (i - 1) * (bottomup_memo[i - 1] + bottomup_memo[i - 2])
    return bottomup_memo[n]


def count_derangements_memory_optimized(n: int) -> int:
    min_2, min_1, sln = 0, 1, 0
    for i in range(1, n + 1):
        match i:
            case 1:
                sln = 0
            case 2:
                sln = 1
            case _:
                sln = (i - 1) * (min_2 + min_1)
        # Rotate
        min_2, min_1 = min_1, sln

    return sln


if __name__ == "__main__":
    for i in range(1, 60):
        print(f"[{i}]: ", count_derangements_bottomup(i))

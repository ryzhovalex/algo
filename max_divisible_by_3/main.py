"""
Finds the highest sum of any 3 numbers from given set divisible by 3 without
a remainder.

Input data spec:
- each number on a new line
- first number on the first line is the amount of numbers in the set

Ref: https://inf-ege.sdamgia.ru/problem?id=35485
"""

from pathlib import Path


def main():
    print(_calculate(Path("data/a.txt")))
    print(_calculate(Path("data/b.txt")))


def _calculate(filepath: Path) -> int:
    with open(filepath) as file:
        # discard first number as an amount of entries
        file.readline()

        numbers: list[int] = list(map(int, file.readlines()))
        numbers.sort()

        # the sum will be divisible by 3 only in these four cases below
        case_1: list[int] = [x for x in numbers if x % 3 == 0][-3:]
        case_2: list[int] = [x for x in numbers if x % 3 == 1][-3:]
        case_3: list[int] = [x for x in numbers if x % 3 == 2][-3:]
        case_4: list[int] = [case_1[-1], case_2[-1], case_3[-1]]

        return max(sum(case_1), sum(case_2), sum(case_3), sum(case_4))


if __name__ == "__main__":
    main()

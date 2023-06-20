from adventcode2015_day1_refactor import count_santa_floor_and_basement_index

part1_test_cases: list[dict[str: str, str: int]] = [
    {'input': '(((())))()()()', 'expected': 0},
    {'input': '(((', 'expected': 3},
    {'input': ')))', 'expected': -3},
    {'input': '()()())', 'expected': -1},
    {'input': '(())(())())))))(', 'expected': -4},
]

part2_test_cases: list[dict[str: str, str: int or None]] = [
    {'input': '())', 'expected': 3},
    {'input': '((())))', 'expected': 7},
    {'input': '((()))()((())))', 'expected': 15},
    {'input': '(', 'expected': None},
    {'input': ')((())))()()()', 'expected': 1},
]


def test_day1_functions():
    for test_case in part1_test_cases:
        assert count_santa_floor_and_basement_index(test_case['input'])[0] == test_case['expected']
    for test_case in part2_test_cases:
        assert count_santa_floor_and_basement_index(test_case['input'])[1] == test_case['expected']


if __name__ == '__main__':
    print(test_day1_functions())

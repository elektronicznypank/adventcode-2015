from adventcode2015_day1 import count_first_character_to_basement, count_santa_floor

part1_test_cases: list[dict] = [
    {'input': '(((())))()()()', 'expected': 0},
    {'input': '(((', 'expected': 3},
    {'input': ')))', 'expected': -3},
    {'input': '()()())', 'expected': -1},
    {'input': '(())(())())))))(', 'expected': -4},
]

part2_test_cases: list[dict] = [
    {'input': '())', 'expected': 3},
    {'input': '((())))', 'expected': 7},
    {'input': '((()))()((())))', 'expected': 15},
    {'input': '(', 'expected': None},
    {'input': ')((())))()()()', 'expected': 1},
]


def test_day1_functions():
    for test_case in part1_test_cases:
        assert count_santa_floor(test_case['input']) == test_case['expected']
    for test_case in part2_test_cases:
        assert count_first_character_to_basement(test_case['input']) == test_case['expected']


if __name__ == '__main__':
    print(test_day1_functions())

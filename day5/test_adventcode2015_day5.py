from adventcode2015_day5 import check_if_nice, check_if_nice_2

test_cases_part1: list[dict[str, bool]] = [
    {'input': 'axa', 'expected': False},
    {'input': 'ugknbfddgicrmopn', 'expected': True},
    {'input': 'aabbccdd', 'expected': False},
    {'input': 'adbddcyui', 'expected': True},
    {'input': 'xazeabgov', 'expected': False}
]

test_cases_part2: list[dict[str, bool]] = [
    {'input': 'aaa', 'expected': False},
    {'input': 'qjhvhtzxzqqjkmpb', 'expected': True},
    {'input': 'xxyxx', 'expected': True},
    {'input': 'uurcxstgmygtbstg', 'expected': False},
    {'input': 'ieodomkazucvgmuy', 'expected': False}
]


def test_day5_functions():
    print('\nTest of the first function:')
    for test_case in test_cases_part1:
        print(f'Testing: {test_case["input"]}, expected: {test_case["expected"]}...')
        assert check_if_nice(test_case['input']) == test_case['expected']
        print('Passed!')
    print('\nTest of the second function:')
    for test_case in test_cases_part2:
        print(f'Testing: {test_case["input"]}, expected: {test_case["expected"]}...')
        assert check_if_nice_2(test_case['input']) == test_case['expected']
        print('Passed!')


if __name__ == '__main__':
    test_day5_functions()

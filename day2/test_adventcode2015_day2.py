from adventcode2015_day2 import count_wrapping_paper_and_ribbon

test_cases_paper: list[dict[str: list, str: int]] = [
    {'input': ['1x1x10'], 'expected': 43},
    {'input': ['2x3x4'], 'expected': 58},
    {'input': ['1x1x2'], 'expected': 11},
    {'input': ['1x2x1'], 'expected': 11},
    {'input': ['2x1x1'], 'expected': 11},
    {'input': ['21x56x49'], 'expected': 10927}
]

test_cases_ribbon: list[dict[str: list, str: int]] = [
    {'input': ['2x3x4'], 'expected': 34},
    {'input': ['1x1x10'], 'expected': 14},
    {'input': ['1x10x1'], 'expected': 14},
    {'input': ['7x16x11'], 'expected': 1268},
    {'input': ['10x10x10'], 'expected': 1040},
    {'input': ['1x1x1'], 'expected': 5}
]


def test_day2_functions():
    for test_case in test_cases_paper:
        assert count_wrapping_paper_and_ribbon(test_case['input'])[0] == test_case['expected']
    for test_case in test_cases_ribbon:
        assert count_wrapping_paper_and_ribbon(test_case['input'])[1] == test_case['expected']


if __name__ == '__main__':
    print(test_day2_functions())

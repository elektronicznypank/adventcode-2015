# This script is to be run with pytest

from adventcode2015_day2_part1 import count_paper_dimension

test_cases: list[dict: str: list] = [
    {
        'input1': ['1x1x10'],
        'input2': ['2x3x4'],
        'input3': ['1x1x2'],
        'input4': ['1x2x1'],
        'input5': ['2x1x1'],
        'input6': ['1x1x1'],
        'input7': ['21x56x49']
    },
    {
        'input1_expected': 43,
        'input2_expected': 58,
        'input3_expected': 11,
        'input4_expected': 11,
        'input5_expected': 11,
        'input6_expected': 7,
        'input7_expected': 10927

    }
]


def test_count_paper_dimension():
    assert count_paper_dimension(test_cases[0]['input1']) == test_cases[1]['input1_expected']
    assert count_paper_dimension(test_cases[0]['input2']) == test_cases[1]['input2_expected']
    assert count_paper_dimension(test_cases[0]['input3']) == test_cases[1]['input3_expected']
    assert count_paper_dimension(test_cases[0]['input4']) == test_cases[1]['input4_expected']
    assert count_paper_dimension(test_cases[0]['input5']) == test_cases[1]['input5_expected']
    assert count_paper_dimension(test_cases[0]['input6']) == test_cases[1]['input6_expected']
    assert count_paper_dimension(test_cases[0]['input7']) == test_cases[1]['input7_expected']


if __name__ == '__main__':
    print(test_count_paper_dimension())

# This script is to be run with pytest

from adventcode2015_day2_part2 import count_ribbon_dimension

results_and_dimensions: dict[int] = {
    34: ['2x3x4'],
    14: [['1x1x10'], ['1x10x1']],
    1268: ['7x16x11'],
    1040: ['10x10x10'],
    5: ['1x1x1'],
}


def test_count_ribbon_dimension():
    assert count_ribbon_dimension(results_and_dimensions[34]) == 34
    assert count_ribbon_dimension(results_and_dimensions[14][0]) == 14
    assert count_ribbon_dimension(results_and_dimensions[14][1]) == 14
    assert count_ribbon_dimension(results_and_dimensions[1268]) == 1268
    assert count_ribbon_dimension(results_and_dimensions[1040]) == 1040
    assert count_ribbon_dimension(results_and_dimensions[5]) == 5


if __name__ == '__main__':
    print(test_count_ribbon_dimension())

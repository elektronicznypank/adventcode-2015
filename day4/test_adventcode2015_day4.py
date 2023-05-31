from adventcode2015_day4 import find_md5_hash_starting_with_zeroes

test_cases = [
    {'input': 'gfhrcops', 'expected_five_zeroes': '36712', 'expected_six_zeroes': '10927261'},
    {'input': 'ouqwbkoq', 'expected_five_zeroes': '819576', 'expected_six_zeroes': '30261423'},
    {'input': '54372648', 'expected_five_zeroes': '534513', 'expected_six_zeroes': '13094353'},
    {'input': '00000000', 'expected_five_zeroes': '782385', 'expected_six_zeroes': '1608317'},
    {'input': 'b3k9s6v1', 'expected_five_zeroes': '327482', 'expected_six_zeroes': '39855305'}
]


def test_day4_function():
    for test_case in test_cases:
        five_zeroes, six_zeroes = find_md5_hash_starting_with_zeroes(test_case['input'])
        five_zeroes = five_zeroes.replace(test_case['input'], '')
        six_zeroes = six_zeroes.replace(test_case['input'], '')
        assert five_zeroes, six_zeroes == (test_case['expected_five_zeroes'], test_case['expected_six_zeroes'])


if __name__ == '__main__':
    print(test_day4_function())

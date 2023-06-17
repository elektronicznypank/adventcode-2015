from adventcode2015_day3 import count_gifted_houses_by_santa_and_robot

test_cases: list[dict[str, int, int]] = [
    {'input': '^^^<', 'santa_result': 5, 'santa_and_robot_result': 4},
    {'input': '^^^', 'santa_result': 4, 'santa_and_robot_result': 3},
    {'input': '<>^v', 'santa_result': 3, 'santa_and_robot_result': 5},
    {'input': 'vvv^^^', 'santa_result': 4, 'santa_and_robot_result': 4},
    {'input': '>><v^', 'santa_result': 4, 'santa_and_robot_result': 4},
]


def test_day3_function():
    for index, test_case in enumerate(test_cases):
        gifted_houses_santa_alone, gifted_houses_santa_and_robot = count_gifted_houses_by_santa_and_robot(test_case['input'])
        print(f'Testing test case nr {index + 1}...')
        assert gifted_houses_santa_alone == test_case['santa_result']
        print('First assertion passed.')
        assert gifted_houses_santa_and_robot == test_case['santa_and_robot_result']
        print('Second assertion passed.')
        print()
    print('All tests passed.')


if __name__ == '__main__':
    test_day3_function()

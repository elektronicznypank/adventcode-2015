# this script runs faster with pypy if large arrays are used

import re

# getting a list of instructions and coordinates from external file
with open('input.txt') as data:
    instructions = data.readlines()


def create_array(amount_of_rows: int, amount_of_columns: int, array_element=0) -> list:
    """
    This function returns an array that contains repeated, specified element.
    :param amount_of_rows: how many rows should an array have
    :param amount_of_columns: how many columns should and array have
    :param array_element: what element should array contain, default is 0
    """
    the_array = [[array_element for _ in range(amount_of_columns)] for _ in range(amount_of_rows)]
    return the_array if amount_of_rows != 0 and amount_of_columns != 0 else []


def parse_numbers_from_string(input_string: str) -> list:
    parsed_list = re.findall(r'\d+', input_string)
    return [int(x) for x in parsed_list]


def turn_on_light(input_number: int) -> int:
    return 1 if input_number == 0 else input_number


def turn_off_light(input_number: int) -> int:
    return 0 if input_number == 1 else input_number


def toggle_light(input_number: int) -> int:
    return 1 if input_number == 0 else 0


def check_how_many_lights_are_on(instruction_data: list, array_rows: int, array_columns: int) -> int:

    lights_array = create_array(array_rows, array_columns)

    for instruction in instruction_data:
        y1, x1, y2, x2 = parse_numbers_from_string(instruction)
        for row_index in range(x1, x2 + 1):
            for column_index in range(y1, y2 + 1):
                if 'turn on' in instruction:
                    lights_array[row_index][column_index] = turn_on_light(lights_array[row_index][column_index])
                elif 'turn off' in instruction:
                    lights_array[row_index][column_index] = turn_off_light(lights_array[row_index][column_index])
                else:
                    lights_array[row_index][column_index] = toggle_light(lights_array[row_index][column_index])

    lights_on_counter = 0

    for row in lights_array:
        lights_on_counter += row.count(1)

    return lights_on_counter


if __name__ == '__main__':
    print(f'There are {check_how_many_lights_are_on(instructions, 1000, 1000)} lights on'
          f'after executing all instructions.')


# tests
def test_create_array():
    assert create_array(1, 2, 1) == [[1, 1]]
    assert create_array(3, 3) == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    assert create_array(0, 0) == []
    assert create_array(3, 0, 4) == []


def test_parse_numbers_from_string():
    assert parse_numbers_from_string('what 111\n\t100$#$@$@#$@$#200ddd0OOOOOOOO') == [111, 100, 200, 0]
    assert parse_numbers_from_string('aaa 134 bbb 123ccc54 ddd   987  e f g') == [134, 123, 54, 987]


def test_turn_on_lights():
    assert turn_on_light(0) == 1
    assert turn_on_light(1) == 1


def test_turn_off_lights():
    assert turn_off_light(1) == 0
    assert turn_off_light(0) == 0


def test_toggle_lights():
    assert toggle_light(0) == 1
    assert toggle_light(1) == 0


def test_check_how_many_lights_are_on():
    assert check_how_many_lights_are_on(['turn on 0, 0, 0, 9'], 10, 10) == 10
    assert check_how_many_lights_are_on(['turn on 0, 0, 9, 0'], 10, 10) == 10
    assert check_how_many_lights_are_on(['toggle 0, 0, 9, 0', 'toggle 0, 0, 9, 0'], 10, 10) == 0
    assert check_how_many_lights_are_on(['turn off 0, 0, 9, 9', 'toggle 0, 0, 9, 9'], 10, 10) == 100
    assert check_how_many_lights_are_on(['turn on 0, 0, 4, 4', 'toggle 2, 2, 2, 2'], 5, 5) == 24

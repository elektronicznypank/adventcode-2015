with open('input.txt', 'r') as floors:
    visited_floors: str = floors.readline()

# part 1


def count_santa_floor(floors_input: str, opened_brackets: int = 0, closed_brackets: int = 0) -> int:
    for i in floors_input:
        if i == '(':
            opened_brackets += 1
        elif i == ')':
            closed_brackets += 1
    return opened_brackets - closed_brackets


# part 2


def count_first_character_to_basement(floors_input: str, floor_index: int = 0, floor: int = 0) -> int or None:
    try:
        while floor > -1:
            if floors_input[floor_index] == '(':
                floor += 1
            elif floors_input[floor_index] == ')':
                floor -= 1
            floor_index += 1
    except IndexError:
        print('Santa will never enter the basement.')
        return None
    return floor_index


if __name__ == '__main__':
    print(f'The instructions take Santa to floor {count_santa_floor(visited_floors)}.')
    print(f'The position of the character taking Santa to the basement '
          f'is {count_first_character_to_basement(visited_floors)}.')

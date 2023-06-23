with open('input.txt', 'r') as floors:
    visited_floors: str = floors.readline().strip()


def count_by_character(input_character: str):

    counter = 0
    match input_character:
        case '(':
            counter += 1
        case ')':
            counter -= 1
    return counter


def count_santa_floor_and_basement_index(floors_input: str, target_floor: int = -1) -> tuple[int, int]:

    brackets_counter: int = 0
    basement_index: None = None

    for floor_index, floor in enumerate(floors_input):

        brackets_counter += count_by_character(floor)

        if brackets_counter == target_floor and basement_index is None:
            basement_index: int = floor_index + 1

    if basement_index is None:
        raise Exception('Santa would never enter the target floor.')

    return brackets_counter, basement_index


if __name__ == '__main__':
    final_floor, basement_floor_index = count_santa_floor_and_basement_index(visited_floors)
    print(f'The instructions take Santa to floor {final_floor} and the position of the first character '
          f'taking Santa to the target floor is {basement_floor_index}.')

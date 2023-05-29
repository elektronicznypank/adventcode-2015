with open('input.txt', 'r') as floors:
    visited_floors: str = floors.readline()


def count_santa_floor_and_basement_index(floors_input: str) -> tuple[int, int or None]:

    opened_brackets: int = 0
    closed_brackets: int = 0
    basement_index: None = None
    is_basement_floor_found: bool = False

    for floor_index, floor in enumerate(floors_input):

        if floor == '(':
            opened_brackets += 1

        elif floor == ')':
            closed_brackets += 1

        if opened_brackets - closed_brackets == -1:
            if not is_basement_floor_found:

                basement_index: int = floor_index + 1
                is_basement_floor_found: bool = True

    return opened_brackets - closed_brackets, basement_index


if __name__ == '__main__':
    print(f'The instructions take Santa to floor {count_santa_floor_and_basement_index(visited_floors)[0]} '
          f'and the position of the first character taking Santa to the basement is '
          f'{count_santa_floor_and_basement_index(visited_floors)[1]}.')

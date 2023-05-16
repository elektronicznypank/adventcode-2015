with open('input.txt', 'r') as floors:
    searched_floor: str = floors.readline()

def floor_counter(some_string: str):
    how_many_opened: int = some_string.count('(')
    how_many_closed: int = some_string.count(')')
    return f'Instructions take Santa to floor {how_many_opened - how_many_closed}.'


def first_character_to_basement_while_loop(some_string: str):
    floor_index: int = 0
    floor: int = 0
    while floor > -1:
        if some_string[floor_index] == '(':
            floor += 1
        elif some_string[floor_index] == ')':
            floor -= 1
        floor_index += 1
    return f'First character that makes Santa enter the basement: {floor_index}.'


def first_character_to_basement_for_loop(some_string: str):
    starting_point: int = 0
    floor: int = 0
    for i in range(len(some_string)):
        if starting_point == -1:
            floor = i
            break
        if some_string[i] == '(':
            starting_point += 1
        elif some_string[i] == ')':
            starting_point -= 1
    return f'First character that makes Santa enter the basement: {floor}.'


if __name__ == '__main__':
    print(floor_counter(searched_floor))
    print(first_character_to_basement_while_loop(searched_floor))
    print(first_character_to_basement_for_loop(searched_floor))

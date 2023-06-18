with open('input.txt') as houses:
    houses_directions: str = houses.readline()


def count_gifted_houses_by_santa(houses_input: str) -> int:
    houses_coordinates_santa_alone: list = [0, 0]
    houses_coordinates_matrix_santa: set = {(0, 0)}

    for i in houses_input:
        move_coordinates(houses_coordinates_santa_alone, i)

        houses_coordinates_matrix_santa.add(tuple(houses_coordinates_santa_alone))

    return len(houses_coordinates_matrix_santa)


def move_coordinates(coordinates, insturction):

    match insturction:
        case '^':
            coordinates[0] += 1
        case 'v':
            coordinates[0] -= 1
        case '>':
            coordinates[1] += 1
        case '<':
            coordinates[1] -= 1


def count_gifted_houses_by_santa_and_robot(houses_input: str) -> int:

    houses_coordinates_santa: list = [0, 0]
    houses_coordinates_robot: list = [0, 0]
    houses_coordinates_matrix_santa_and_robot: set = {(0, 0)}

    for j, k in enumerate(houses_input):
        if j % 2 == 0:
            move_coordinates(houses_coordinates_santa, k)
        else:
            move_coordinates(houses_coordinates_robot, k)

        houses_coordinates_matrix_santa_and_robot.add(tuple(houses_coordinates_santa))
        houses_coordinates_matrix_santa_and_robot.add(tuple(houses_coordinates_robot))

    return len(houses_coordinates_matrix_santa_and_robot)


if __name__ == '__main__':
    print(f'Santa left at least one present in {count_gifted_houses_by_santa(houses_directions)} houses.')
    print(f'Santa and robot left at least one present in '
          f'{count_gifted_houses_by_santa_and_robot(houses_directions)} houses.')

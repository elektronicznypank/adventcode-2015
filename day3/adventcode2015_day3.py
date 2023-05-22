with open('input.txt') as houses:
    houses_directions: str = houses.readline()

# part 1


def count_gifted_houses_by_santa(houses_input: str) -> int:

    houses_coordinates_santa_alone: list = [0, 0]
    houses_coordinates_matrix_santa: set = {(0, 0)}

    for i in houses_input:
        houses_coordinates_santa_alone = list(houses_coordinates_santa_alone)
        if i == '^':
            houses_coordinates_santa_alone[0] += 1
        elif i == 'v':
            houses_coordinates_santa_alone[0] -= 1
        elif i == '>':
            houses_coordinates_santa_alone[1] += 1
        elif i == '<':
            houses_coordinates_santa_alone[1] -= 1

        houses_coordinates_santa_alone: tuple = tuple(houses_coordinates_santa_alone)
        houses_coordinates_matrix_santa.add(houses_coordinates_santa_alone)

    return len(houses_coordinates_matrix_santa)


# part 2


def count_gifted_houses_by_santa_and_robot(houses_input: str) -> int:

    houses_coordinates_santa: list = [0, 0]
    houses_coordinates_robot: list = [0, 0]
    houses_coordinates_matrix_santa_and_robot: set = {(0, 0)}

    for j, k in enumerate(houses_input):

        houses_coordinates_santa: list = list(houses_coordinates_santa)
        houses_coordinates_robot: list = list(houses_coordinates_robot)

        if j % 2 == 0:
            if k == '^':
                houses_coordinates_santa[0] += 1
            elif k == 'v':
                houses_coordinates_santa[0] -= 1
            elif k == '>':
                houses_coordinates_santa[1] += 1
            elif k == '<':
                houses_coordinates_santa[1] -= 1
        else:
            if k == '^':
                houses_coordinates_robot[0] += 1
            elif k == 'v':
                houses_coordinates_robot[0] -= 1
            elif k == '>':
                houses_coordinates_robot[1] += 1
            elif k == '<':
                houses_coordinates_robot[1] -= 1

        houses_coordinates_santa: tuple = tuple(houses_coordinates_santa)
        houses_coordinates_robot: tuple = tuple(houses_coordinates_robot)

        houses_coordinates_matrix_santa_and_robot.add(houses_coordinates_santa)
        houses_coordinates_matrix_santa_and_robot.add(houses_coordinates_robot)

    return len(houses_coordinates_matrix_santa_and_robot)


if __name__ == '__main__':
    print(f'Santa left at least one present in {count_gifted_houses_by_santa(houses_directions)} houses.')
    print(f'Santa and robot left at least one present in '
          f'{count_gifted_houses_by_santa_and_robot(houses_directions)} houses.')

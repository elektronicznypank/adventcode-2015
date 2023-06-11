with open('input.txt') as houses:
    houses_directions: str = houses.readline().replace('\n', '')


def count_gifted_houses_by_santa_and_robot(houses_input: str) -> tuple[int, int]:

    houses_coordinates_santa_alone: list = [0, 0]
    houses_coordinates_santa_turn: list = [0, 0]
    houses_coordinates_robot_turn: list = [0, 0]
    houses_coordinates_matrix_santa_alone: set = {(0, 0)}
    houses_coordinates_matrix_santa_and_robot: set = {(0, 0)}

    for house_index, sign in enumerate(houses_input):

        houses_coordinates_santa_alone: list = list(houses_coordinates_santa_alone)
        houses_coordinates_santa_turn: list = list(houses_coordinates_santa_turn)
        houses_coordinates_robot_turn: list = list(houses_coordinates_robot_turn)

        if house_index % 2 == 0:

            if sign == '^':
                houses_coordinates_santa_alone[0] += 1
                houses_coordinates_santa_turn[0] += 1
            elif sign == 'v':
                houses_coordinates_santa_alone[0] -= 1
                houses_coordinates_santa_turn[0] -= 1
            elif sign == '>':
                houses_coordinates_santa_alone[1] += 1
                houses_coordinates_santa_turn[1] += 1
            elif sign == '<':
                houses_coordinates_santa_alone[1] -= 1
                houses_coordinates_santa_turn[1] -= 1
            else:
                raise Exception("Houses' input contains illegal characters. Please verify it.")

        else:

            if sign == '^':
                houses_coordinates_santa_alone[0] += 1
                houses_coordinates_robot_turn[0] += 1
            elif sign == 'v':
                houses_coordinates_santa_alone[0] -= 1
                houses_coordinates_robot_turn[0] -= 1
            elif sign == '>':
                houses_coordinates_santa_alone[1] += 1
                houses_coordinates_robot_turn[1] += 1
            elif sign == '<':
                houses_coordinates_santa_alone[1] -= 1
                houses_coordinates_robot_turn[1] -= 1
            else:
                raise Exception("Houses' input contains illegal characters. Please verify it.")

        houses_coordinates_santa_alone: tuple = tuple(houses_coordinates_santa_alone)
        houses_coordinates_santa_turn: tuple = tuple(houses_coordinates_santa_turn)
        houses_coordinates_robot_turn: tuple = tuple(houses_coordinates_robot_turn)

        houses_coordinates_matrix_santa_alone.add(houses_coordinates_santa_alone)
        houses_coordinates_matrix_santa_and_robot.add(houses_coordinates_santa_turn)
        houses_coordinates_matrix_santa_and_robot.add(houses_coordinates_robot_turn)

    return len(houses_coordinates_matrix_santa_alone), len(houses_coordinates_matrix_santa_and_robot)


if __name__ == '__main__':
    gifted_houses_santa_alone, gifted_houses_santa_and_robot = count_gifted_houses_by_santa_and_robot(houses_directions)
    print(f'Santa left at least one present in {gifted_houses_santa_alone} houses.')
    print(f'Santa and robot left at least one present in {gifted_houses_santa_and_robot} houses.')

with open('input.txt') as houses:
    houses_matrix: str = houses.readline()


def count_visited_houses(amount_of_houses: str) -> int:
    houses_coordinates: list = [0, 0]
    houses_coordinates_matrix: set = {(0, 0)}
    for i in amount_of_houses:
        houses_coordinates = list(houses_coordinates)
        if i == '^':
            houses_coordinates[0] += 1
        elif i == 'v':
            houses_coordinates[0] -= 1
        elif i == '>':
            houses_coordinates[1] += 1
        elif i == '<':
            houses_coordinates[1] -= 1
        houses_coordinates: tuple = tuple(houses_coordinates)
        houses_coordinates_matrix.add(houses_coordinates)
    return len(houses_coordinates_matrix)


if __name__ == '__main__':
    print(f'Santa left at least one present in {count_visited_houses(houses_matrix)} houses.')

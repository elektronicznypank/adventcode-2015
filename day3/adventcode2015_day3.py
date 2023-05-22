with open('input.txt') as houses:
    houses_matrix: str = houses.readline()


def count_visited_houses(amount_of_houses: str) -> int:
    coordinates: list = [0, 0]
    coordinates_matrix: set = {(0, 0)}
    for i in amount_of_houses:
        coordinates = list(coordinates)
        if i == '^':
            coordinates[0] += 1
        elif i == 'v':
            coordinates[0] -= 1
        elif i == '>':
            coordinates[1] += 1
        elif i == '<':
            coordinates[1] -= 1
        coordinates: tuple = tuple(coordinates)
        coordinates_matrix.add(coordinates)
    return len(coordinates_matrix)


if __name__ == '__main__':
    print(f'Santa left at least one present in {count_visited_houses(houses_matrix)} houses.')

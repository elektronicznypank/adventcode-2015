with open('input.txt', 'r') as paper_dimensions_data:
    dimensions_of_paper: list = paper_dimensions_data.readlines()


def count_wrapping_paper_and_ribbon(amount_of_paper: list, wrapping_paper: int = 0, ribbon: int = 0) -> tuple[int, int]:

    for index in range(len(amount_of_paper)):

        amount_of_paper[index] = amount_of_paper[index].replace('\n', '')

        length, width, height = amount_of_paper[index].split('x')

        length, width, height = int(length), int(width), int(height)

        wrapping_paper += 2 * (length * width + width * height + length * height)\
            + min(length, width, height) * sorted([length, width, height])[1]

        ribbon += 2 * min(length, width, height) + 2 * sorted([length, width, height])[1] + length * width * height

    return wrapping_paper, ribbon


if __name__ == '__main__':
    print(f'Elves should order {count_wrapping_paper_and_ribbon(dimensions_of_paper)[0]} feet of paper '
          f'and {count_wrapping_paper_and_ribbon(dimensions_of_paper)[1]} feet of ribbon.')
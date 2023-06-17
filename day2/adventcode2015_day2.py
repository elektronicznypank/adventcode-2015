with open('input.txt', 'r') as gifts_dimensions_database:
    gifts_dimensions: list = gifts_dimensions_database.readlines()


def count_wrapping_paper_and_ribbon(amount_of_paper: list) -> tuple[int, int]:

    wrapping_paper: int = 0
    ribbon: int = 0
    
    for index in range(len(amount_of_paper)):

        amount_of_paper[index] = amount_of_paper[index].replace('\n', '')

        length, width, height = amount_of_paper[index].split('x')

        length, width, height = int(length), int(width), int(height)

        wrapping_paper += 2 * (length * width + width * height + length * height)\
            + min(length, width, height) * sorted([length, width, height])[1]

        ribbon += 2 * min(length, width, height) + 2 * sorted([length, width, height])[1] + length * width * height

    return wrapping_paper, ribbon


if __name__ == '__main__':
    sum_of_paper, sum_of_ribbon = count_wrapping_paper_and_ribbon(gifts_dimensions)
    print(f'Elves should order {sum_of_paper} feet of paper and {sum_of_ribbon} feet of ribbon.')

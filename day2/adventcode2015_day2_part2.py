with open('input.txt', 'r') as paper_dimensions_data:
    dimensions_to_count_ribbon: list = paper_dimensions_data.readlines()


def count_ribbon_dimension(amount_of_paper: list, final_dimension: int = 0) -> int:
    for i in range(len(amount_of_paper)):
        if '\n' in amount_of_paper[i]:
            amount_of_paper[i] = amount_of_paper[i].replace('\n', '')
        l, w, h = amount_of_paper[i].split('x')
        l, w, h = int(l), int(w), int(h)
        final_dimension += 2 * min(l, w, h) + 2 * sorted([l, w, h])[1] + l * w * h
    return final_dimension


if __name__ == '__main__':
    print(f'Elves should order {count_ribbon_dimension(dimensions_to_count_ribbon)} feet of ribbon.')

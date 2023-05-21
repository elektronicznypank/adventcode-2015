with open('input.txt', 'r') as paper_dimensions_data:
    wrapping_paper: list = paper_dimensions_data.readlines()


def count_paper_dimension(amount_of_paper: list, final_dimension=0) -> int:
    for i in range(len(amount_of_paper)):
        if '\n' in amount_of_paper[i]:
            amount_of_paper[i] = amount_of_paper[i].replace('\n', '')
        l, w, h = amount_of_paper[i].split('x')
        l, w, h = int(l), int(w), int(h)
        final_dimension += 2 * (l * w + w * h + l * h) + min(l, w, h) * sorted([l, w, h])[1]
    return final_dimension


if __name__ == '__main__':
    print(count_paper_dimension(wrapping_paper))
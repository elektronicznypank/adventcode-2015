with open('input.txt', 'r') as paper_dimensions_data:
    wrapping_paper: list = paper_dimensions_data.readlines()


def count_paper_dimension(final_dimension=0) -> int:
    for i in range(len(wrapping_paper)):
        wrapping_paper[i] = wrapping_paper[i].replace('\n', '')
        l, w, h = wrapping_paper[i].split('x')
        l, w, h = int(l), int(w), int(h)
        extra_paper: int = min(l, w, h) ** 2
        present_area: int = 2 * (l * w + w * h + l * h)
        final_dimension += present_area + extra_paper
    return final_dimension


if __name__ == '__main__':
    print(count_paper_dimension())

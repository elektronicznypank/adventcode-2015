with open('input.txt', 'r') as paper_dimensions:
    paper_list: list = paper_dimensions.readlines()


def count_paper_dimension(final_dimension=0):
    for i in range(len(paper_list)):
        paper_list[i] = paper_list[i].replace('\n', '')
        q, w, e = paper_list[i].split('x')
        q, w, e = int(q), int(w), int(e)
        minimum: int = min(q, w, e) ** 2
        length = 2 * q * w
        width = 2 * w * e
        height = 2 * q * e
        final_dimension += length + width + height + minimum
    return final_dimension


print(count_paper_dimension())

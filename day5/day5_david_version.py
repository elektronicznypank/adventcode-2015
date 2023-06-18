with open('input.txt') as input_matrix:
    input_data = input_matrix.readlines()

def check_if_nice_2(input):
    has_two_consecutive_letters_separated = False

    for index, letter in enumerate(input):
        next_letter = initialize_nth_letter(1, input, index)
        next_next_letter = initialize_nth_letter(2, input, index)

        if letter == next_next_letter and letter != next_letter:
            has_two_consecutive_letters_separated = True

    return has_two_consecutive_letters_separated



def check_if_nice(input):
    vowels_list = 'aieou'
    vowels_counter = 0

    is_ab = False
    is_cd = False
    is_pq = False
    is_xy = False
    has_two_consecutive_letters = False

    for index, letter in enumerate(input):
        next_letter = initialize_nth_letter(1, input, index)
        next_next_letter = initialize_nth_letter(2, input, index)

        # summing of three vowels
        if letter in vowels_list:
            vowels_counter += 1

        # checking forbidden letters
        if letter == 'a' and next_letter == 'b':
            is_ab = True
        if letter == 'c' and next_letter == 'd':
            is_cd = True
        if letter == 'p' and next_letter == 'q':
            is_pq = True
        if letter == 'x' and next_letter == 'y':
            is_xy = True

        # checking two same letters in a row
        if letter == next_letter:
            has_two_consecutive_letters = True
        if letter == next_next_letter and letter != next_letter:
            has_two_consecutive_letters_separated = True

    if is_ab or is_xy or is_pq or is_cd:
        return False

    return vowels_counter >= 3 and has_two_consecutive_letters


def initialize_nth_letter(n, input, index):
    if index < len(input) - n:
        return input[index + n]

    return None

print(check_if_nice_2("axa"))
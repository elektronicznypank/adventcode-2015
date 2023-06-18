with open('input.txt') as input_matrix:
    input_data = input_matrix.readlines()


def initialize_nth_letter(n, string_input, index):

    if index < len(string_input) - n:
        return string_input[index + n]

    return None


def check_if_nice(string_input):

    vowels = 'aieou'
    vowels_counter = 0

    is_ab = False
    is_cd = False
    is_pq = False
    is_xy = False
    has_two_consecutive_letters = False

    for index, letter in enumerate(string_input):

        next_letter = initialize_nth_letter(1, string_input, index)

        # summing of three vowels
        if letter in vowels:
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

    if is_ab or is_xy or is_pq or is_cd:
        return False

    return vowels_counter >= 3 and has_two_consecutive_letters


def check_if_nice_2(string_input):

    has_two_consecutive_letters_separated = False
    has_two_pairs_without_overlapping = False

    for index, letter in enumerate(string_input):

        next_letter = initialize_nth_letter(1, string_input, index)
        next_next_letter = initialize_nth_letter(2, string_input, index)

        # checking two letters separated or three the same at all
        if letter == next_next_letter:
            has_two_consecutive_letters_separated = True

        # checking a pair of letters that appears at least twice without overlapping
        if string_input.count(f'{letter}{next_letter}') >= 2:
            has_two_pairs_without_overlapping = True

    return has_two_consecutive_letters_separated and has_two_pairs_without_overlapping


print(check_if_nice_2("axa"))
print(check_if_nice_2("aaa"))
print(check_if_nice_2("qjhvhtzxzqqjkmpb"))
print(check_if_nice_2("xxyxx"))
print(check_if_nice_2('uurcxstgmygtbstg'))
print(check_if_nice_2("ieodomkazucvgmuy"))

number_of_nices_2 = 0

for i in input_data:
    if check_if_nice_2(i):
        number_of_nices_2 += 1
else:
    print(number_of_nices_2)

with open('input.txt') as input_file:
    strings_to_be_processed_matrix: list = input_file.readlines()


def remove_new_line_from_string_element_in_list(input_list: list[str]) -> list[str]:
    for element_index, element in enumerate(input_list):
        input_list[element_index] = element.rstrip()
    return input_list


def check_if_string_contains_at_least_three_vowels(input_string: str, vowels: str = 'aeiou') -> bool:
    amount_of_vowels: int = 0
    for letter in input_string:
        if letter in vowels:
            amount_of_vowels += 1
        if amount_of_vowels == 3:
            return True
    return False


def check_if_string_contains_double_letters_in_a_row(input_string: str) -> bool:
    for letter_index in range(len(input_string) - 1):
        if input_string[letter_index] == input_string[letter_index + 1]:
            return True
    return False


def check_if_string_is_forbidden_characters_free(input_string: str) -> bool:

    if 'ab' not in input_string \
            and 'cd' not in input_string \
            and 'pq' not in input_string \
            and 'xy' not in input_string:
        return True
    return False


def check_if_string_is_nice(input_string: str) -> bool:
    if check_if_string_contains_at_least_three_vowels(input_string) \
            and check_if_string_contains_double_letters_in_a_row(input_string) \
            and check_if_string_is_forbidden_characters_free(input_string):
        return True
    return False


def count_nice_strings_in_list(input_list: list, counter: int = 0) -> int:
    for element in input_list:
        if check_if_string_is_nice(element):
            counter += 1
    return counter


if __name__ == '__main__':
    remove_new_line_from_string_element_in_list(strings_to_be_processed_matrix)
    print(f'There are {count_nice_strings_in_list(strings_to_be_processed_matrix)} nice strings in the list.')

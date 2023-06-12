from hashlib import md5

with open('input.txt') as input_file:
    secret_key: str = input_file.readline().replace('\n', '')


def find_md5_hash_starting_with_zeroes(input_key: str):

    index: int = 1

    hash_with_five_zeroes: str = ''
    hash_with_six_zeroes: str = ''

    is_five_zeroes_found: bool = False
    is_six_zeroes_found: bool = False

    while not (is_five_zeroes_found and is_six_zeroes_found):

        key_to_be_hashed: str = f'{input_key}{index}'
        encoded_key_to_be_hashed: hash = md5(key_to_be_hashed.encode())
        hexadecimal_encoded_key: hash = encoded_key_to_be_hashed.hexdigest()

        if hexadecimal_encoded_key[:5] == '00000' and not is_five_zeroes_found:
            is_five_zeroes_found: bool = True
            hash_with_five_zeroes = key_to_be_hashed

        if hexadecimal_encoded_key[:6] == '000000':
            is_six_zeroes_found: bool = True
            hash_with_six_zeroes: str = key_to_be_hashed

        index += 1

    return hash_with_five_zeroes, hash_with_six_zeroes


if __name__ == '__main__':
    five_zeroes, six_zeroes = find_md5_hash_starting_with_zeroes(secret_key)
    five_zeroes: str = five_zeroes.replace(secret_key, '')
    six_zeroes: str = six_zeroes.replace(secret_key, '')
    print(f'First answer - {five_zeroes}, second answer - {six_zeroes}.')

str1 = str(input())


def count_letters(filename):
    letter_count = {}

    with open(filename, 'r') as file:
        for line in file:
            for letter in line:
                if letter.isalpha():
                    letter = letter.lower()
                    if letter in letter_count:
                        letter_count[letter] += 1
                    else:
                        letter_count[letter] = 1

    sorted_letters = sorted(letter_count.items(), key=lambda x: x[1])

    with open(filename, 'w') as result_file:
        for letter, count in sorted_letters:
            result_file.write(f"{letter}: {count}\n")


count_letters(str1)
str1 = str(input())

def can_form_palindrome(word):
    letter_count = {}
    for letter in word:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

    odd_count = 0
    for count in letter_count.values():
        if count % 2 != 0:
            odd_count += 1

    if odd_count > 1:
        return "Невозможно составить палиндром"

    palindrome = ""
    for letter, count in letter_count.items():
        palindrome += letter * (count // 2)

    odd_letter = ""
    for letter, count in letter_count.items():
        if count % 2 != 0:
            odd_letter = letter

    return palindrome + odd_letter + palindrome[::-1]


palindrome = can_form_palindrome(str1)
if palindrome != "Невозможно составить палиндром":
    print(palindrome)
else:
    print(palindrome)
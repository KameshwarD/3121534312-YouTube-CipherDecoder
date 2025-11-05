
letter_to_number = {
    'A': 41,
    'B': 42,
    'C': 43,
    'D': 121,
    'E': 15,
    'F': 123,
    'G': 131,
    'H': 132,
    'I': 16,
    'J': 24,
    'K': 212,
    'L': 213,
    'M': 51,
    'N': 52,
    'O': 53,
    'P': 231,
    'Q': 232,
    'R': 26,
    'S': 34,
    'T': 312,
    'U': 313,
    'V': 321,
    'W': 35,
    'X': 323,
    'Y': 61,
    'Z': 62,
    ' ': 0  # Space
}
number_to_letter = {v: k for k, v in letter_to_number.items()}

def letters_to_numbers(text):
    text = text.upper()
    numbers = [str(letter_to_number.get(char, '?')) for char in text]
    return ' '.join(numbers)

def numbers_to_letters(numbers_str):
    numbers = numbers_str.split()
    letters = [number_to_letter.get(int(num), '?') for num in numbers]
    return ''.join(letters)

# Test
print(letters_to_numbers("TEST"))
print(numbers_to_letters("312 15 34 312"))

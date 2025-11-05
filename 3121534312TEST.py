# --- custom mapping ---
letter_to_number = {
    'A': 3, 'B': 15, 'C': 88, 'D': 42, 'E': 7,
    'F': 19, 'G': 5, 'H': 24, 'I': 11, 'J': 9,
    'K': 31, 'L': 54, 'M': 2,  'N': 26, 'O': 20,
    'P': 77, 'Q': 14, 'R': 1,  'S': 55, 'T': 10,
    'U': 60, 'V': 63, 'W': 29, 'X': 36, 'Y': 6, 'Z': 72
}
# Create reverse mapping
number_to_letter = {v: k for k, v in letter_to_number.items()}

def letters_to_numbers(text: str) -> str:
    text = ''.join(c for c in text.upper() if c.isalpha())
    return ' '.join(str(letter_to_number.get(c, '?')) for c in text)

def numbers_to_letters(numbers: str) -> str:
    out = []
    for token in numbers.split():
        try:
            n = int(token)
            out.append(number_to_letter.get(n, '?'))
        except ValueError:
            out.append('?')
    return ''.join(out)

# Test the code
print(letters_to_numbers("TEST"))  # Example input
print(numbers_to_letters("10 7 55 10"))  # Example input

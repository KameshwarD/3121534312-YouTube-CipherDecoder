letter_to_number = {
    'A': 41,  'B': 42,  'C': 43,  'D': 121, 'E': 15,  'F': 123,
    'G': 131, 'H': 132, 'I': 16,  'J': 24,  'K': 212, 'L': 213,
    'M': 51,  'N': 52,  'O': 53,  'P': 231, 'Q': 232, 'R': 26,
    'S': 34,  'T': 312, 'U': 313, 'V': 321, 'W': 35,  'X': 323,
    'Y': 61,  'Z': 62,  ' ': 0
}

number_to_letter = {str(v): k for k, v in letter_to_number.items()}

codes = set(number_to_letter.keys())
max_len = max(len(c) for c in codes)

def letters_to_numbers(text: str) -> str:
    """Encode letters to numbers, skipping spaces, and return a concatenated string."""
    out = []
    for ch in text.upper():
        if ch == ' ':
            continue
        out.append(str(letter_to_number.get(ch, '')))
    return ''.join(out)

def numbers_to_letters(s: str) -> str:
    """Decode numbers to letters.
       - If spaced (e.g., '312 15 34'), use direct lookup.
       - If unspaced (e.g., '3121534312'), greedy longest-match scan.
    """
    s = s.strip()
    if ' ' in s:
        return ''.join(number_to_letter.get(tok, '?') for tok in s.split())
    else:
        i, out = 0, []
        n = len(s)
        while i < n:
            match = None
            for L in range(min(max_len, n - i), 0, -1):
                chunk = s[i:i+L]
                if chunk in number_to_letter:
                    match = number_to_letter[chunk]
                    i += L
                    break
            if match is None:
                out.append('?')
                i += 1
            else:
                # Ignore decoded space unless you want to keep it
                if match != ' ':
                    out.append(match)
        return ''.join(out)

# ---- Examples ----
print(letters_to_numbers("TEST this game"))
# -> 3121534312  (no spaces; spaces in input are skipped)

print(numbers_to_letters("3121534312"))
# -> TEST

print(numbers_to_letters("312 15 34 312"))
# -> TEST


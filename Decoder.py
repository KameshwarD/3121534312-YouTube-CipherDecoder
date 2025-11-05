letter_to_number = {
    'A': 41,  'B': 42,  'C': 43,  'D': 121, 'E': 15,  'F': 123,
    'G': 131, 'H': 132, 'I': 16,  'J': 24,  'K': 212, 'L': 213,
    'M': 51,  'N': 52,  'O': 53,  'P': 231, 'Q': 232, 'R': 26,
    'S': 34,  'T': 312, 'U': 313, 'V': 321, 'W': 35,  'X': 323,
    'Y': 61,  'Z': 62,  ' ': 0
}
number_to_letter = {str(v): k for k, v in letter_to_number.items()}

CODES = set(k for k in number_to_letter if k != '0')  # valid code strings
PREFIX = set()
for c in CODES:
    for k in range(1, len(c)):
        PREFIX.add(c[:k])

from functools import lru_cache
import re

def _expansions(ch: str):
    """Return possible digit-expansions for one observed digit."""
    if ch == '4':  # 11 compressed
        return ("4", "11")
    if ch == '6':  # 33 compressed
        return ("6", "33")
    return (ch,)

@lru_cache(None)
def _decode_segment(seg: str):
    """
    Best-effort decode of a segment with no zeros by expanding each observed digit and
    incrementally forming letter codes. Emits '?' only at positions that can't be resolved,
    instead of failing the whole word.
    """
    n = len(seg)

    @lru_cache(None)
    def dfs(i: int, buf: str) -> str:
        """
        i  : index in observed seg
        buf: current partial digit-buffer (0..2 digits) toward the next code
        returns: decoded suffix from i with current buf (best-effort, never None)
        """
        # End of observed digits
        if i == n:
            if buf in CODES:
                return number_to_letter[buf]          # complete last code
            elif buf == '':
                return ''                              # nothing pending
            else:
                return '?'                             # leftover partial -> unknown

        # Try all expansions for this observed digit (if 4/6), else the digit itself
        for ex in _expansions(seg[i]):
            res = _consume_expansion(i, 0, ex, buf)
            if res is not None:
                return res  # return first successful path

        # If no expansion path works here, emit '?' and advance one digit (keep buf)
        return '?' + dfs(i + 1, buf)

    @lru_cache(None)
    def _consume_expansion(i: int, k: int, ex: str, buf: str):
        """
        Consume the k-th digit of expansion 'ex' at observed index i, updating buf.
        Emit letters as soon as buf equals a valid code. Returns decoded suffix or None.
        """
        # Finished applying this expansion: move to next observed char
        if k == len(ex):
            return dfs(i + 1, buf)

        d = ex[k]
        new_buf = buf + d

        # Too long for any code (max len 3)
        if len(new_buf) > 3:
            return None

        # If new_buf is exactly a code: emit it now and continue (reset buf)
        if new_buf in CODES:
            letter = number_to_letter[new_buf]
            rest = _consume_expansion(i, k + 1, ex, '')
            if rest is not None:
                return letter + rest
            return None

        # If new_buf isn't a prefix of any code, dead end for this expansion path
        if new_buf not in PREFIX:
            return None
        return _consume_expansion(i, k + 1, ex, new_buf)

    return dfs(0, '')

def numbers_to_letters(s: str) -> str:
    """Public decoder: splits on zero-runs; each '0' is one space (00 = two, etc.)."""
    if not s:
        return ''
    parts = re.findall(r'0+|[1-9]+', s)
    out = []
    for part in parts:
        if part[0] == '0':
            out.append(' ' * len(part))
        else:
            _decode_segment.cache_clear()
            decoded = _decode_segment(part)
            out.append(decoded)
    return ''.join(out)

# ---------- Quick checks ----------
if __name__ == "__main__":
    print(numbers_to_letters("234526123154612"))
    print(numbers_to_letters("12126163245"))
    print(numbers_to_letters("34442315"))
    print(numbers_to_letters("34351651"))
    print(numbers_to_letters("2656161216521504321315412641524315012443124104412345326231312165352"))
    print(numbers_to_letters("16555152604353261505441652312155241524315"))

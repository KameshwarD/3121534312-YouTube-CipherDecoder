# 🔐 Cipher Decoder for "3121534312" YouTube Channel

A Python-based decoder for a custom alphanumeric cipher using **digit-to-letter mapping** and **lossy compression rules**. Designed to handle unclear or compressed inputs while still revealing as many decoding clues as possible by intelligently inserting `?` in place of unresolved characters.

---

## 📜 Cipher Rules

- Each **letter maps to a unique digit sequence** (e.g., `A → 41`, `T → 312`).
- **Spaces are encoded as 0**:
  - `0` → space  
  - `00` → two spaces  
  - `000` → three spaces  
- Compression rule:
  - `11` is encoded as `4`
  - `33` is encoded as `6`
- The decoder expands `4` and `6` back into `11` and `33` **when it leads to better decoding**.
- Handles ambiguous or invalid parts using `?`, instead of failing entire words.

---

## ✨ Features

- ✅ Converts digit strings into meaningful text (`numbers_to_letters`)
- ✅ Supports optional reverse encoding (`letters_to_numbers`)
- ✅ Best-effort pattern recognition (keeps partial words intact)
- ✅ Handles edge cases like:
  - Cross-letter compression
  - Mixed literal + compressed digits
  - Global ambiguity
- ✅ Works word-by-word (segments by `0`)

---

## 🛠 Usage

### 1. Run the script directly
```bash
3121534312TEST.py

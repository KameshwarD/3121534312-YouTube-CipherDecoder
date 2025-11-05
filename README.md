# 🔐 Cipher Decoder for "3121534312" YouTube Channel

It is the answer to many videos on the YouTube Channel https://www.youtube.com/@3121534312/videos
A Python-based decoder for a custom alphanumeric cipher using **digit-to-letter mapping** and **lossy compression rules**. Designed to handle unclear or compressed inputs while still revealing as many decoding clues as possible by intelligently inserting `?` in place of unresolved characters.

**Decode secret number codes into readable text — in Python & Web!**

[![Live Web Demo](https://img.shields.io/badge/Live-Web_Demo-00d4ff?style=for-the-badge&logo=googlechrome&logoColor=white)](https://your-username.github.io/TESTYouTubeChannel/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](Decoder.py)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](index.html)
[![License](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)

---

## Live Demo

**Try it now**: https://kameshward.github.io/3121534312-YouTube-CipherDecoder/

> **Replace `your-username` with your actual GitHub username**

---

## Features

| Feature | Description |
|-------|-----------|
| **Web App** | Beautiful glass-morphism UI with animated gradient |
| **Real-time Decoding** | Instant results as you type |
| **Responsive** | Works on phone, tablet, and desktop |
| **Python Version** | Original logic in `Decoder.py` |
| **Zero Dependencies** | Pure HTML/CSS/JS — no build tools |
| **Ctrl+Enter** | Quick decode shortcut |
| **Example Buttons** | Test with pre-filled codes |

---

## How It Works

This decoder uses a **custom mapping** where each letter is represented by a unique number:

```json
"A": 41, "B": 42, "C": 43, ..., " ": 0
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
Decoder.py

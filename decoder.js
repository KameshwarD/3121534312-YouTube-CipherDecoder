class NumberDecoder {
  constructor(mapping) {
    this.letterToNumber = mapping;
    this.numberToLetter = {};
    this.CODES = new Set();
    this.PREFIX = new Set();

    // reverse map + valid codes
    for (const [letter, num] of Object.entries(mapping)) {
      const code = String(num);
      this.numberToLetter[code] = letter;
      if (code !== '0') this.CODES.add(code);
    }

    // prefixes (1-based slices)
    for (const code of this.CODES) {
      for (let i = 1; i < code.length; i++) {
        this.PREFIX.add(code.substring(0, i));
      }
    }
  }

  _expansions(ch) {
    if (ch === '4') return ['4', '11'];
    if (ch === '6') return ['6', '33'];
    return [ch];
  }

  _decodeSegment(seg) {
    const n = seg.length;
    const memo = new Map();

    const dfs = (i, buf) => {
      const key = `${i},${buf}`;
      if (memo.has(key)) return memo.get(key);

      if (i === n) {
        if (this.CODES.has(buf)) return this.numberToLetter[buf];
        if (buf === '') return '';
        return '?';
      }

      for (const ex of this._expansions(seg[i])) {
        const res = this._consumeExpansion(i, 0, ex, buf);
        if (res !== null) {
          memo.set(key, res);
          return res;
        }
      }

      // no expansion works → unknown char
      const fallback = '?' + dfs(i + 1, buf);
      memo.set(key, fallback);
      return fallback;
    };

    // separate memo for the inner recursion
    const consumeMemo = new Map();
    this._consumeExpansion = (i, k, ex, buf) => {
      const key = `${i},${k},${buf}`;
      if (consumeMemo.has(key)) return consumeMemo.get(key);

      if (k === ex.length) {
        const res = dfs(i + 1, buf);
        consumeMemo.set(key, res);
        return res;
      }

      const d = ex[k];
      const newBuf = buf + d;

      if (newBuf.length > 3) {
        consumeMemo.set(key, null);
        return null;
      }

      if (this.CODES.has(newBuf)) {
        const letter = this.numberToLetter[newBuf];
        const rest = this._consumeExpansion(i, k + 1, ex, '');
        if (rest !== null) {
          const result = letter + rest;
          consumeMemo.set(key, result);
          return result;
        }
      }

      if (newBuf !== '' && !this.PREFIX.has(newBuf)) {
        consumeMemo.set(key, null);
        return null;
      }

      const result = this._consumeExpansion(i, k + 1, ex, newBuf);
      consumeMemo.set(key, result);
      return result;
    };

    return dfs(0, '');
  }

  numbersToLetters(s) {
    if (!s) return '';
    const parts = s.match(/0+|[1-9]+/g) || [];
    let out = '';

    for (const part of parts) {
      if (part[0] === '0') {
        out += ' '.repeat(part.length);
      } else {
        out += this._decodeSegment(part);
      }
    }
    return out;
  }
}
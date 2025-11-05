document.addEventListener('DOMContentLoaded', () => {
  const input   = document.getElementById('input');
  const btn     = document.getElementById('decodeBtn');
  const output  = document.getElementById('output');
  const examples = document.querySelectorAll('.example-btn');

  // ---- 1. Load mapping (inline JSON) ----
  let decoder = null;
  try {
    const mapping = JSON.parse(document.getElementById('mapping-data').textContent);
    decoder = new NumberDecoder(mapping.letter_to_number);
    console.log('Decoder ready');
  } catch (e) {
    output.textContent = 'Failed to parse mapping data.';
    console.error(e);
    return;
  }

  // ---- 2. Decode function ----
  const decode = () => {
    const value = input.value.trim();
    if (!value) {
      output.textContent = 'Please enter some numbers.';
      return;
    }
    const result = decoder.numbersToLetters(value);
    output.textContent = result || '(empty)';
  };

  // ---- 3. UI events ----
  btn.addEventListener('click', decode);

  input.addEventListener('keydown', e => {
    if (e.key === 'Enter' && e.ctrlKey) decode();
  });

  examples.forEach(b => {
    b.addEventListener('click', () => {
      input.value = b.dataset.input;
      decode();
    });
  });
});

const VOWELS = ['a', 'e', 'i', 'o', 'u'];

function vowelCount(string='') {
  let frequency = {};
  for (let v of VOWELS) {
    frequency[v] = 0;
  }

  for (let l of string) {
    if (frequency.hasOwnProperty(l)) {
      frequency[l] += 1;
    }
  }

  return frequency;
}

console.log(vowelCount('fifteen'));
console.log(vowelCount('dioxyribonucleic acid'));

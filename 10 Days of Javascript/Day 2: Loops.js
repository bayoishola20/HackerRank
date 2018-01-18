/*
 * Complete the vowelsAndConsonants function.
 * Print your output using 'console.log()'.
 */
function vowelsAndConsonants(s) {
    let allVowels = 'aeiou';
    let vowels = '';
    let consonants = '';
    for (let i of s) {
        if (allVowels.indexOf(i) !== -1) {
            vowels += i;
        } else {
            consonants += i;
        }
    }
    let ans = vowels + consonants;
    for (let j of ans) {
        console.log(j);
    }
}
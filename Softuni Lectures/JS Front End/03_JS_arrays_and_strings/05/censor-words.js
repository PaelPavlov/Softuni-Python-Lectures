function solve(text, word) {
    console.log(text.replaceAll(word, '*'.repeat(word.length)));
}

solve('A small sentence with some words', 'small'); //	A ***** sentence with some words
solve('Find the hidden word', 'hidden'); //	Find the ****** word

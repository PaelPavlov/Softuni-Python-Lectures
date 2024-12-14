function solve(input) {

    const searchWords = input.shift().split(' ');
    const matched = searchWords.reduce((matched, word) => ({ ...matched, [word]: 0 }), {});

    input.forEach(word => {
        if ( matched.hasOwnProperty(word) ) matched[word] += 1;
    });

    Object
        .entries(matched)
        .sort((a, b) => b[1] - a[1])
        .forEach(([word, count]) => console.log(`${word} - ${count}`));
}

solve([
    'this sentence', 
    'In', 'this', 'sentence', 'you', 'have', 'to', 'count', 'the', 'occurrences', 'of', 'the', 'words', 'this', 'and', 'sentence', 'because', 'this', 'is', 'your', 'task'
]);
// this - 3
// sentence - 2

solve([
    'is the', 
    'first', 'sentence', 'Here', 'is', 'another', 'the', 'And', 'finally', 'the', 'the', 'sentence'
]);
// the – 3
// is - 1





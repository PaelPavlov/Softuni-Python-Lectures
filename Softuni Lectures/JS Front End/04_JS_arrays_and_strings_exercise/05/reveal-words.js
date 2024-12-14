function solve(words, sentence) {

    words = words.split(', ');
    
    for ( let w of words ) {
        sentence = sentence.replace( '*'.repeat(w.length), w );
    }

    console.log(sentence);
}

solve('great','softuni is ***** place for learning new programming languages');
// softuni is great place for learning new programming languages
solve('great, learning','softuni is ***** place for ******** new programming languages');
// softuni is great place for learning new programming languages

function isPerfectNumber(num) {
    
    let sum = 1;

    for ( let i = 2; i < num; i++ ) {
        if ( num % i === 0 ) sum += i;
    }

    if ( num === sum ) {
        console.log("We have a perfect number!");
    } else {
        console.log("It's not so perfect.");
    }
}

isPerfectNumber(6); // We have a perfect number!
isPerfectNumber(28); // We have a perfect number!
isPerfectNumber(1236498); // It's not so perfect.

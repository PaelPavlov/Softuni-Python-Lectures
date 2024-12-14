function solve(...args) {

    let largestNumber = Math.max(...args);

    console.log(`The largest number is ${largestNumber}.`);
}

solve(5, -3, 16); //	The largest number is 16.
solve(-3, -5, -22.5); //	The largest number is -3.

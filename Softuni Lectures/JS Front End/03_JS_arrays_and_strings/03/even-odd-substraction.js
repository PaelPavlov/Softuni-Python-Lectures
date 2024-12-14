function solve(numbers) {
    let evenSum = 0;
    let oddSum = 0;

    numbers.forEach(function(number){
        if ( number % 2 === 0 ) {
            evenSum += number;
        } else {
            oddSum += number;
        }
    })

    console.log(evenSum - oddSum);
}

solve([1,2,3,4,5,6]); //	3
solve([3,5,7,9]); //	-24
solve([2,4,6,8,10]); //	30

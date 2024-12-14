// function oddAndEvenSum(num) {

//     const digits = Math.abs(num).toString().split('').map(Number);

//     const evenSum = digits.filter(d => d % 2 === 0).reduce((sum, d) => sum + d, 0);
//     const oddSum = digits.filter(d => d % 2 !== 0).reduce((sum, d) => sum + d, 0);

//     console.log(`Odd sum = ${oddSum}, Even sum = ${evenSum}`);
// }

function oddAndEvenSum(num) {
    const digits = Math.abs(num).toString().split('').map(Number);
    let eSum = 0, oSum = 0;
    digits.forEach(d => ( d % 2 == 0 ) ? eSum += d : oSum += d );
    console.log(`Odd sum = ${oSum}, Even sum = ${eSum}`);
}

oddAndEvenSum(1000435); // Odd sum = 9, Even sum = 4
oddAndEvenSum(3495892137259234); // Odd sum = 54, Even sum = 22


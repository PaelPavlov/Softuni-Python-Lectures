// function checkSign(num1, num2, num3) {

//     const array = [num1, num2, num3];

//     const isNegative = array.filter(num => num < 0).length % 2 !== 0;

//     console.log( isNegative ? 'Negative' : 'Positive' );
// }


function checkSign(num1, num2, num3) {
    const isNegative = [...arguments].filter(n => n < 0).length % 2 !== 0;
    console.log( isNegative ? 'Negative' : 'Positive' );
}

checkSign(5,12,-15); // Negative
checkSign(-6,-12,14); // Positive

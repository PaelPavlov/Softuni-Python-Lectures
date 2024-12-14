// function solve(numbers) {
//     const first = numbers[0];
//     const last = numbers[numbers.length-1];
//     console.log(first + last);
// }

function solve(numbers) {
    const first = numbers.shift();
    const last = numbers.pop();
    console.log(first + last);
}

solve([20, 30, 40]); //	60
solve([10, 17, 22, 33]); //	43
solve([11, 58, 69]); //	80

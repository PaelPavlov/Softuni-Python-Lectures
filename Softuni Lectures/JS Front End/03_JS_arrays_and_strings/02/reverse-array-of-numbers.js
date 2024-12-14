// function solve(n, numbers) {
//     let newArray = [];
    
//     for (let i = 0; i < n; i++) {
//         newArray.push(numbers[i])
//     }

//     console.log(newArray.reverse().join(' '));
// }

function solve(n, numbers) {
    console.log(numbers.splice(0, n).reverse().join(' '));
}

solve(3, [10, 20, 30, 40, 50]); // 	30 20 10
solve(4, [-1, 20, 99, 5]); // 5 99 20 -1
solve(2, [66, 43, 75, 89, 47]); // 	43 66

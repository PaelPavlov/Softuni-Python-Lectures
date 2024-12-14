function findSmallestNumber(num1, num2, num3) {
    return Math.min(...arguments);
}

console.log( findSmallestNumber(2,5,3) ); // 2
console.log( findSmallestNumber(600,342,123) );// 123
console.log( findSmallestNumber(25,21,4) ); // 4
console.log( findSmallestNumber(2,2,2) ); // 2
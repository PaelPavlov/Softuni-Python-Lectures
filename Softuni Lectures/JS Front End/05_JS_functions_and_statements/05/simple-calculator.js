function calculate(x, y, operator) {

    const operations = [];

    operations['multiply'] = (a, b) => a * b;
    operations['divide'] = (a, b) => a / b;
    operations['add'] = (a, b) => a + b;
    operations['subtract'] = (a, b) => a - b;

    console.log( operations[operator](x, y) );

}

calculate(5, 5, 'multiply'); // 25
calculate(40, 8, 'divide'); // 5
calculate(12, 19, 'add'); // 31
calculate(50, 13, 'subtract'); // 37


// operations['multiply'] = (a, b) => a * b;

// operations['multiply'] = function(a, b) {
//     return a * b;
// }

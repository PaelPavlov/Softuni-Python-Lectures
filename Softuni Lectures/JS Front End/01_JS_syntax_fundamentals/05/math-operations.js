function solve(num1, num2, operation) {

    let result;

    switch(operation) {
        case '+':
            result = num1 + num2;
            break;
        case '-':
            result = num1 - num2;
            break;
        case '*':
            result = num1 * num2;
            break;
        case '/':
            result = num1 / num2;
            break;
        case '%':
            result = num1 % num2;
            break;
        case '**':
            result = num1 ** num2;
            break;
    }

    console.log( result );
}

solve(5, 6, '+'); // 11
solve(3, 5.5, '*'); // 16.5

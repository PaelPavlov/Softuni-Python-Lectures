function factorialDivision(num1, num2) {

    function calculateFoctorial(num) {
        if ( num == 0 || num == 1 ) {
            return 1;
        } else {
            return num * calculateFoctorial(num - 1);
        }
    }

    const factorial1 = calculateFoctorial(num1);
    const factorial2 = calculateFoctorial(num2);

    const result = factorial1 / factorial2;

    console.log( result.toFixed(2) );

}

factorialDivision(5,2); // 60.00
factorialDivision(6,2); // 360.00
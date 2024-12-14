function solve(input) {
    
    const parking = {};

    input.forEach(entry => {
        
        const [ direction, carNumber ] = entry.split(', ');

        if ( direction == 'IN' ) {
            if ( ! parking.hasOwnProperty(carNumber) ) parking[carNumber] = 1;
        } else {
            if ( parking.hasOwnProperty(carNumber) ) delete parking[carNumber];
        }

    });

    if ( Object.keys(parking).length > 0 ) {
        Object.entries(parking).sort().forEach(([carNumber]) => console.log(carNumber));
    } else {
        console.log('Parking Lot is Empty');
    }

}

solve(['IN, CA2844AA','IN, CA1234TA','OUT, CA2844AA','IN, CA9999TT','IN, CA2866HI','OUT, CA1234TA','IN, CA2844AA','OUT, CA2866HI','IN, CA9876HH','IN, CA2822UU']);
// CA2822UU
// CA2844AA
// CA9876HH
// CA9999TT

console.log('--------------');

solve(['IN, CA2844AA','IN, CA1234TA','OUT, CA2844AA','OUT, CA1234TA']);
// Parking Lot is Empty
    

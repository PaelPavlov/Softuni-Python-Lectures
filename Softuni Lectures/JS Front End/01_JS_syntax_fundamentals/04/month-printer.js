function solve(num) {    
    if ( num > 0 && num < 13 ) {
        console.log(new Date(1986, num-1).toLocaleString('default', { month: 'long' }));
    } else {
        console.log('Error!');
    }
}

solve(2); // February
solve(13); // Error!
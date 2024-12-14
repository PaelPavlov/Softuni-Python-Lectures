// function solve(input) {
    
//     const zippedArray = [];
//     const initialArrayLength = input.length;

//     input.sort(function(a, b){
//         return a - b;
//     });

//     for ( let i = 0; i < initialArrayLength; i++) {
//         if ( i % 2 == 0 ) {
//             const el = input.shift();
//             zippedArray.push(el);
//         } else {
//             const el = input.pop();
//             zippedArray.push(el);
//         }
//     }

//     return zippedArray;

// }

function solve(input) { 

    input.sort(function(a, b){
        return a - b;
    });

    const counter = [...new Array(input.length).keys()];

    console.log(counter);

    return counter.reduce(function(result, i){
        if ( i % 2 == 0 ) {
            return [ ...result, input.shift() ];
        } else {
            return [ ...result, input.pop() ];
        }
    }, []);

}

console.log( solve([1, 65, 3, 52, 48, 63, 31, -3, 18, 56]) );
// [-3, 65, 1, 63, 3, 56, 18, 52, 31, 48]

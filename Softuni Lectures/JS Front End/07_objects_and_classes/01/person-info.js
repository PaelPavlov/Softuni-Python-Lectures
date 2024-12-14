// function personInfo(firstName, lastName, age) {
//     const person = {
//         firstName: firstName,
//         lastName: lastName,
//         age: age,
//     }

//     return person;
// }

function personInfo(firstName, lastName, age) {
    return {
        firstName,
        lastName,
        age
    }
}


function personInfo(firstName, lastName, age) {
    return { firstName, lastName, age }
}

console.log( personInfo('Jack', 'Sparrow', 'unknown') );

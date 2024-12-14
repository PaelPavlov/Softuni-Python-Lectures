// function solve(input) {
//     const employees = {}

//     input.forEach(element => {
//         employees[element] = element.length;
//     });

//     for (const name in employees) {
//         console.log(`Name: ${name} -- Personal Number: ${employees[name]}`);
//     }

// }

// function solve(input) {
//     input.forEach(element => {
//         console.log(`Name: ${element} -- Personal Number: ${element.length}`);
//     });
// }


function solve(input) {

    function processEmployees(list) {
        return list.reduce((employees, person) => {
            employees[person] = person.length
            return employees;
        },{});
    }

    function printEmployees(employees) {
        for (const employee in employees) {
            console.log(`Name: ${employee} -- Personal Number: ${employees[employee]}`);
        }
    }

    const employees = processEmployees(input);
    printEmployees(employees);
    
}


solve(['Silas Butler','Adnaan Buckley','Juan Peterson','Brendan Villarreal']);
// Name: Silas Butler -- Personal Number: 12
// Name: Adnaan Buckley -- Personal Number: 14
// Name: Juan Peterson -- Personal Number: 13
// Name: Brendan Villarreal -- Personal Number: 18

console.log('-------');

solve(['Samuel Jackson','Will Smith','Bruce Willis','Tom Holland']);
// Name: Samuel Jackson -- Personal Number: 14
// Name: Will Smith -- Personal Number: 10
// Name: Bruce Willis -- Personal Number: 12
// Name: Tom Holland -- Personal Number: 11



const someString = 'Hello';

console.log(someString[0]);

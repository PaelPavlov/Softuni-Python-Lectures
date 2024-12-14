// function processSity(city){
//     const keys = Object.keys(city);

//     for (const key of keys) {
//         console.log(`${key} -> ${city[key]}`);
//     }
// }

function processSity(city){
    const entries = Object.entries(city);

    for (const [ property, value ] of entries) {
        console.log(`${property} -> ${value}`);
    }
}

processSity({ name: 'Sofia', area: 492, population: 1238438, country: 'Bulgaria', postCode: 1000 });
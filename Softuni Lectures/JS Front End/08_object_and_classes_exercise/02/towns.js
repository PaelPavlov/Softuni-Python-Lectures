function solve(input) {
    input.forEach(element => {
        let [ town, latitude, longitude ] = element.split(' | ');
        latitude = Number(latitude).toFixed(2);
        longitude = Number(longitude).toFixed(2);
        console.log({ town, latitude, longitude });
    });
}

solve(['Sofia | 42.696552 | 23.32601', 'Beijing | 39.913818 | 116.363625']);
// { town: 'Sofia', latitude: '42.70', longitude: '23.33' }
// { town: 'Beijing', latitude: '39.91', longitude: '116.36' }
    
solve(['Plovdiv | 136.45 | 812.575']);
//{ town: 'Plovdiv', latitude: '136.45', longitude: '812.58' }
    
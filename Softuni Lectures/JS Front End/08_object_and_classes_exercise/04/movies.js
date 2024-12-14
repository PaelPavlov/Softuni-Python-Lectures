function solve(input) {

    const movies = {};

    input.forEach((line) => {

        if ( line.includes('addMovie') ) {
            
            const [_, name] = line.split('addMovie ');
            movies[name] = { name };

        } else if ( line.includes('directedBy') ) {

            const [name, director] = line.split(' directedBy ');
            movies[name] ??= {};
            movies[name].director = director;
            
        } else if ( line.includes('onDate') ) {

            const [name, date] = line.split(' onDate ');
            movies[name] ??= {};
            movies[name].date = date;

        }
    });
    
    for (const movie in movies) {
        if ( Object.keys(movies[movie]).length > 2 ) console.log(JSON.stringify(movies[movie]));
    }
    
}

solve([
    'addMovie Fast and Furious',
    'addMovie Godfather',
    'Inception directedBy Christopher Nolan',
    'Godfather directedBy Francis Ford Coppola',
    'Godfather onDate 29.07.2018',
    'Fast and Furious onDate 30.07.2018',
    'Batman onDate 01.08.2018',
    'Fast and Furious directedBy Rob Cohen'
]);
// {"name":"Fast and Furious","date":"30.07.2018","director":"Rob Cohen"}
// {"name":"Godfather","director":"Francis Ford Coppola","date":"29.07.2018"}

// console.log('-------------');

// solve([
//     'addMovie The Avengers',
//     'addMovie Superman',
//     'The Avengers directedBy Anthony Russo',
//     'The Avengers onDate 30.07.2010',
//     'Captain America onDate 30.07.2010',
//     'Captain America directedBy Joe Russo'
// ]);
//{"name":"The Avengers","director":"Anthony Russo","date":"30.07.2010"}
    

// const movie = {
//     'Fast and Furious': { name: 'Fast and Furious' },
//     Godfather: { name: 'Godfather' }
//   }

// console.log(JSON.stringify(movie, 0, 2));

// movie['Godfather'].test = 'stuff';

// console.log(JSON.stringify(movie, 0, 2));
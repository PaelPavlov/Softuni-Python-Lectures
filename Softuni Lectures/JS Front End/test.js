function movies(input) {
    const movieList = [];

    input.forEach(command => {
        if (command.startsWith("addMovie")) {
            const movieName = command.replace("addMovie ", "").trim();
            movieList.push({ name: movieName });
        } else if (command.includes("directedBy")) {
            const [movieName, director] = command.split(" directedBy ");
            const movie = movieList.find(m => m.name === movieName.trim());
            if (movie) {
                movie.director = director.trim();
            }
        } else if (command.includes("onDate")) {
            const [movieName, date] = command.split(" onDate ");
            const movie = movieList.find(m => m.name === movieName.trim());
            if (movie) {
                movie.date = date.trim();
            }
        }
    });

    // Filter movies with complete information and print each in the specified format
    const completeMovies = movieList.filter(m => m.name && m.director && m.date);
    completeMovies.forEach(movie => {
        console.log(`{"name":"${movie.name}","director":"${movie.director}","date":"${movie.date}"}`);
    });
}

// Example usage with your input
const input = [
    'addMovie Fast and Furious',
    'addMovie Godfather',
    'Inception directedBy Christopher Nolan',
    'Godfather directedBy Francis Ford Coppola',
    'Godfather onDate 29.07.2018',
    'Fast and Furious onDate 30.07.2018',
    'Batman onDate 01.08.2018',
    'Fast and Furious directedBy Rob Cohen'
];

movies(input);


function processNumbers(input) {
    
    const phoneBook = {};

    input.forEach(entry => {
        const [name, phone] = entry.split(' ');
        phoneBook[name] = phone;
    });

    for ( const key in phoneBook ) {
        console.log(`${key} -> ${phoneBook[key]}`);
    }

    // console.log( phoneBook['Tim'] );
    // console.log( phoneBook.Tim );


}

processNumbers(['Tim 08812312331', 'Peter 08812312332', 'Bill 08812312333', 'Tim 08812312334']);
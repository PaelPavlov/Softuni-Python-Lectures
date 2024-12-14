function addressBook(input) {
    
    const addressBook = {}

    input.forEach(entry => {
        const [name, place] = entry.split(':');
        addressBook[name] = place;
    });

    console.log(addressBook);

    const addressBookSortable = Object.entries(addressBook);

    console.log(addressBookSortable);

    addressBookSortable.sort(([keyA, valueA], [keyB, valueB]) => {
        return valueA.localeCompare(valueB);
    });

    for (const [name, place] of addressBookSortable) {
        console.log(`${name} -> ${place}`);
    }

}

addressBook(['Tim:Doe Crossing','Bill:Nelson Place','Peter:Carlyle Ave','Bill:Ornery Rd']);

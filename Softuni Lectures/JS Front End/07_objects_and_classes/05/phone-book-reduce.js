function solve(input) {

    const phoneNumbers = input
        .map((entry) => entry.split(" "))
        .reduce((phoneBook, [name, phone]) => {
            phoneBook[name] = phone;
            return phoneBook;
        }, {});
    
    Object
        .entries(phoneNumbers)
        .forEach(([k, v]) => console.log(`${k} -> ${v}`));
}

solve([
    "Tim 0834212554",
    "Peter 0877547887",
    "Bill 0896543112",
    "Tim 0876566344",
]);
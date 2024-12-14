// function solve(stock, ordered) {

//     const storage = {}

//     for (let i = 0; i < stock.length; i += 2) {
//         storage[stock[i]] = Number(stock[i + 1])
//     }

//     for (let i = 0; i < ordered.length; i += 2) {
//         if ( ! storage.hasOwnProperty(ordered[i]) ) storage[ordered[i]] = 0;
//         storage[ordered[i]] += Number(ordered[i + 1]);
//     }

//     for (const product in storage) {
//         console.log(`${product} -> ${storage[product]}`);
//     }   

// }

// function solve(stock, ordered) {
    
//     const storage = [ ...stock, ...ordered ].reduce((storage, product, i, array) => {
//         if ( i % 2 == 0 ) storage[product] = ( storage[product] || 0 ) + Number(array[i + 1]);
//         return storage;
//     }, {});

//     for (const product in storage) {
//         console.log(`${product} -> ${storage[product]}`);
//     }  

// }


function solve(s, o) {
    Object
        .entries([...s,...o].reduce((s,p,i,a) => ( i%2==0 ? { ...s, [p]: ( s[p] || 0 ) + Number(a[i + 1]) } : s ), {}))
        .forEach(([p,q]) => console.log(`${p} -> ${q}`));
}

solve(['Chips', '5', 'CocaCola', '9', 'Bananas', '14', 'Pasta', '4', 'Beer', '2'],['Flour', '44', 'Oil', '12', 'Pasta', '7', 'Tomatoes', '70', 'Bananas', '30']);
// Chips -> 5
// CocaCola -> 9
// Bananas -> 44
// Pasta -> 11
// Beer -> 2
// Flour -> 44
// Oil -> 12
// Tomatoes -> 70

console.log('---');

solve(['Salt', '2', 'Fanta', '4', 'Apple', '14', 'Water', '4', 'Juice', '5'],['Sugar', '44', 'Oil', '12', 'Apple', '7', 'Tomatoes', '7', 'Bananas', '30']);
// Salt -> 2
// Fanta -> 4
// Apple -> 21
// Water -> 4
// Juice -> 5
// Sugar -> 44
// Oil -> 12
// Tomatoes -> 7
// Bananas -> 30

function total(numberOfPeople, type, day) {
    let row = find_row_code(type), col = find_col_code(day);
    let rate = rateTable(row, col);
    return numberOfPeople * rate - discount(numberOfPeople, type, rate);
}
function rateTable(row, col) {
    let rates = [
        [8.45,9.80,10.46],
        [10.90,15.60,16],
        [15,20,22.50]
    ]
    return rates[row][col];
}
function discount(numberOfPeople, type, rate) {
    let discount = 0;
    if (type === "Business" && numberOfPeople >= 100) {
        discount = 10 * rate;
    }
    if (type === "Students" && numberOfPeople >= 30) {
        discount = 0.15 * rate * numberOfPeople;
    }
    if (type === "Regular" && numberOfPeople > 10 && numberOfPeople <= 20) {
        discount = 0.05 * rate * numberOfPeople;
    }
    return discount;
}
function find_col_code(day) {
    const col_codes = new Map([
        ["Friday", 0],
        ["Saturday", 1],
        ["Sunday", 2],
    ]);
    return col_codes.get(day);
}
function find_row_code(type) {
    const rowCodes = new Map([
        ["Students", 0],
        ["Business", 1],
        ["Regular", 2],
    ]);
    return rowCodes.get(type);
}
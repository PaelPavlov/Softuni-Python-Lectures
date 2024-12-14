function solve(num) {
    const stringFromNumber = num.toString();

    let sum = 0;
    for (let i = 0; i < stringFromNumber.length; i++) {
        sum += Number(stringFromNumber[i]);
    }

    console.log(sum);
}

solve(245678); // 32
solve(97561); // 28
solve(543); // 12

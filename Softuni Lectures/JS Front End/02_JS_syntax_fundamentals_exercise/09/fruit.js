function solve(fruit, weightInGrams, pricePerKg) {
    const weightInKg = weightInGrams / 1000;
    const cost = weightInKg * pricePerKg; 
    console.log(`I need $${cost.toFixed(2)} to buy ${weightInKg.toFixed(2)} kilograms ${fruit}.`);
}

solve('orange', 2500, 1.80); //	I need $4.50 to buy 2.50 kilograms orange.
solve('apple', 1563, 2.35); //	I need $3.67 to buy 1.56 kilograms apple.

class Vehicle {
    constructor(type, model, parts, fuel) {
        this.type = type;
        this.model = model;
        this.fuel = fuel;
        this.parts = parts;
        this.parts.quality = parts.engine * parts.power;
    }

    drive(amount) {
        this.fuel -= amount;
    }
}

let myParts = { engine: 6, power: 100 };
let myVehicle = new Vehicle('a', 'b', myParts, 200);
myVehicle.drive(100);
console.log(myVehicle.fuel);
console.log(myVehicle.parts.quality);

// let parts = {engine: 9, power: 500};
// let myVehicle = new Vehicle('l', 'k', parts, 840);
// myVehicle.drive(20);
// console.log(vehicle.fuel);
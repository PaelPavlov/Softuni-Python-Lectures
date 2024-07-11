function calculateBusStationIncome(busRoutes, passengerCounts, ticketPrices) {
    let totalIncome = 0;

    for (let i = 0; i < busRoutes.length; i++) {
        const route = busRoutes[i];
        const passengers = passengerCounts[i];
        const ticketPrice = ticketPrices[route];

        totalIncome += passengers * ticketPrice;
    }

    return `Total income for the bus station is $${totalIncome.toFixed(2)}`;
}

const busRoutes = ["A", "B", "C"];

const passengerCounts = [44, 30, 50];


const ticketPrices = {
    "A": 2.5,
    "B": 4.0,
    "C": 3.8
};
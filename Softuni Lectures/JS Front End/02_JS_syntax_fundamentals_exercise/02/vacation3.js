function solve(...line) {
    let group = Number(line[0]);
    let type = line[1];
    let day = line[2];

    console.log( group, type, day);

    let price;
    const perStudentFriday = 8.45;
    const perStudentSaturday = 9.80;
    const perStudentSunday = 10.46;
    const perBusinessFriday = 10.90;
    const perBusinessSaturday = 15.60;
    const perBusinessSunday = 16.00;
    const perRegularFriday = 15;
    const perRegularSaturday = 20;
    const perRegularSunday = 22.50;
 
    switch(day) {
        case "Friday":
            if (type == "Students") {
                price = group * perStudentFriday;
                if(group >= 30) {
                    price -= price  * ( 1 - 0.85);
                } 
            } else if (type == "Business") {
                    price = group * perBusinessFriday;
                    if( group >= 100) {
                    }
                        price = (group - 10) + perBusinessFriday;
            } else if ( type == "Regular") {
                        price = group * perRegularFriday;
                    if (group >= 10 && group <= 20) {
                            price -= price(1 - 0.95);
                    }
                }
            break;
        case "Saturday":
            if (type == "Students") {
                price = group * perStudentSaturday;
                if(group >= 30) {
                    price -= (price  * ( 1 - 0.85));
                } 
            } else if (type == "Business") {
                    price = group * perBusinessSaturday;
                    if( group >= 100) {
                    }
                        price = (group - 10) + perBusinessSaturday;
            } else if (type == "Regular") {
                        price = group * perRegularSaturday;
                    if (group >= 10 && group <= 20) {
                            price -= price(1 - 0.95);
                    }
                }
            break;
        case "Sunday":
            if (type == "Students") {
                price = group * perStudentSunday;
                if(group >= 30) {
                    price -= (price  * ( 1 - 0.85));
                } 
            } else if (type == "Business") {
                    price = group * perBusinessSunday;
                    if( group >= 100) {
                    }
                        price = (group - 10) + perBusinessSunday;
            } else if ( type == "Regular") {
                        price = group * perRegularSunday;
                    if (group >= 10 && group <= 20) {
                            price -= price(1 - 0.95);
                    }
                }
            break;
    }
    console.log( price );
 
    price = Number(price).toFixed(2);
 
    console.log(`Total price: ${price}`)
 
}


solve(30, "Students", "Sunday"); //	Total price: 266.73
solve(40, "Regular", "Saturday"); // Total price: 800.00

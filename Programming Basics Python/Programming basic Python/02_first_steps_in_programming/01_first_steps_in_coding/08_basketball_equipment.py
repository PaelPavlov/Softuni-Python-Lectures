# • Баскетболни кецове – цената им е 40% по-малка от таксата за една година

# • Баскетболен екип – цената му е 20% по-евтина от тази на кецовете

# • Баскетболна топка – цената ѝ е 1 / 4 от цената на баскетболния екип

# • Баскетболни аксесоари – цената им е 1 / 5 от цената на баскетболната топка 

annual_fee = int(input())
shoes = annual_fee * (1 - 0.40)
clothes = shoes * (1 -0.20)
ball = clothes * 1 / 4
accessories = ball * 1 / 5

total_cost = annual_fee + shoes + clothes + ball + accessories

print(total_cost)
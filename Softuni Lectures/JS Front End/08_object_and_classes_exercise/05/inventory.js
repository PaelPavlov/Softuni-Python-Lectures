function solve(input) {

    const list = [];

    input.forEach(line => {
        let [name, level, items] = line.split(' / ');
        level = Number(level);
        list.push({ name, level, items });
    });

    list
        .sort((a, b) => a.level - b.level)
        .forEach(hero => {
            console.log(`Hero: ${hero.name}`);
            console.log(`level => ${hero.level}`);
            console.log(`items => ${hero.items}`);
        });
}

solve([
    'Isacc / 25 / Apple, GravityGun',
    'Derek / 12 / BarrelVest, DestructionSword',
    'Hes / 1 / Desolator, Sentinel, Antara'
]);
// Hero: Hes
// level => 1
// items => Desolator, Sentinel, Antara
// Hero: Derek
// level => 12
// items => BarrelVest, DestructionSword
// Hero: Isacc
// level => 25
// items => Apple, GravityGun

console.log('-----------');

solve([
    'Batman / 2 / Banana, Gun',
    'Superman / 18 / Sword',
    'Poppy / 28 / Sentinel, Antara'
]);
// Hero: Batman
// level => 2
// items => Banana, Gun
// Hero: Superman
// level => 18
// items => Sword
// Hero: Poppy
// level => 28
// items => Sentinel, Antara
    
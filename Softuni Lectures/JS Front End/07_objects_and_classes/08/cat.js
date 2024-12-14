function catCreator(arr) {

    class Cat {
        constructor(name, age) {
            this.name = name;
            this.age = age;
        }

        meow() {
            console.log(`${this.name}, age ${this.age} says Meow`);
        }
    }

    const cats = [];

    arr.forEach(element => {
        const [ name, age ] = element.split(' ');
        cats.push( new Cat(name, age) );
    });

    for (const cat of cats) {
        cat.meow();
    }

}

catCreator(['Mellow 2', 'Tom 5']);
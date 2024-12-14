function convertToJson(name, lastName, hairColor) {
    const object = { name, lastName, hairColor }
    console.log(JSON.stringify(object));
}

convertToJson('George', 'Jones', 'Brown');
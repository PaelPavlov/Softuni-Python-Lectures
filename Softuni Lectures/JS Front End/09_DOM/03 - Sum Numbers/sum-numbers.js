// function calc() {
//     const num1Element = document.querySelector('#num1');
//     const num2Element = document.querySelector('#num2');
//     const sumElement = document.querySelector('#sum');

//     sumElement.value = Number(num1Element.value) + Number(num2Element.value);
// }

function calc() {
    const num1 = Number(document.querySelector('#num1').value);
    const num2 = Number(document.querySelector('#num2').value);
    document.querySelector('#sum').value = num1 + num2;
}
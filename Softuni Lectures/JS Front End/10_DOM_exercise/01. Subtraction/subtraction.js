// function subtract() {

//     const inputElFirst = document.querySelector('#firstNumber');
//     const inputElSecond = document.querySelector('#secondNumber');
//     const resultEl = document.querySelector('#result');

//     console.log(inputElFirst);

//     const result = Number(inputElFirst.value) - Number(inputElSecond.value);

//     resultEl.textContent = result;

// }

function subtract() {
    
    const num1 = Number(document.querySelector('#firstNumber').value);
    const num2 = Number(document.querySelector('#secondNumber').value);
    
    document.querySelector('#result').textContent = num1 - num2;
    
}

// function subtract() {
    
//     const [ el1, el2 ] = document.querySelectorAll('input[type="text"]');
//     document.querySelector('#result').textContent = Number(el1.value) - Number(el2.value);
    
// }

// function subtract() {
    
//     const [ num1, num2 ] = [...document.querySelectorAll('input[type="text"]')].map(el => Number(el.value));
//     document.querySelector('#result').textContent = num1 - num2;
    
// }
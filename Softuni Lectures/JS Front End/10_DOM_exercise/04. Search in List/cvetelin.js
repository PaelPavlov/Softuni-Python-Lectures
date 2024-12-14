function solve() {
    
    const listElement = Array.from(document.getElementById('towns').querySelectorAll('li'));
    
    const inputElement = document.getElementById('searchText');
    const searchText = inputElement.value;
    
    let counter = 0;
    
    const resultEl = document.getElementById('result');
    
    listElement.forEach(el => {

        console.log(searchText, el.textContent);
        
        if (searchText === el.textContent) {
            el.style.textDecoration = 'underline';
            el.style.fontWeight = 'bold';
            counter++;
        }
    });
    
    resultEl.textContent = `${counter} matches found`;
}
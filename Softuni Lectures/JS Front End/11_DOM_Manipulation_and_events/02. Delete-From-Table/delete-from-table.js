function deleteByEmail() {
    const inputEl = document.querySelector('input[name="email"]');
    const searchStr = inputEl.value.toLowerCase();
    const people = document.querySelectorAll('table tbody tr td:nth-child(2)');
    const resultEl = document.querySelector('#result');

    if ( searchStr == '' ) return;

    const [ matchedEl ] = [...people].filter(person => {
        return person.textContent.toLowerCase().includes(searchStr)
    });

    if ( matchedEl ) {
        matchedEl.parentElement.remove();
        resultEl.textContent = 'Deleted.';
    } else {
        resultEl.textContent = 'Not found.';
    }

    inputEl.value = '';
}

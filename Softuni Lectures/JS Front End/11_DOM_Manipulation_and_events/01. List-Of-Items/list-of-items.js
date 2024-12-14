function addItem() {
    
    const inputEl = document.querySelector('#newItemText');
    const listEl = document.querySelector('#items');
    
    if ( inputEl.value == '' ) return;

    // Create new li element
    const newListItem = document.createElement('li');

    // Set the text content of the newly created element to the value of the input
    newListItem.textContent = inputEl.value;

    // Attach the new element to the list
    listEl.appendChild(newListItem);

    // Reset text inside the input field
    inputEl.value = '';
}
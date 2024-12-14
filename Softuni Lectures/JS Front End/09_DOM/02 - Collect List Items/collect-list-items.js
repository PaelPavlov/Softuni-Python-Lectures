function extractText() {
    const listElements = $$('ul li');
    const textareaElement = document.querySelector('#result');

    textareaElement.value = [...listElements].map(el => el.textContent.trim()).join('\n');
}
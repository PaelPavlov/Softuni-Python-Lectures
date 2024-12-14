document.addEventListener('DOMContentLoaded', solve);

// function solve() {
    
//     function sectionFocusedEventHandler(event) {
//         event.currentTarget.parentElement.classList.add('focused');
//     }
    
//     function sectionBluredEventHandler(event) {
//         event.currentTarget.parentElement.classList.remove('focused');
//     }

//     const inputFields = document.querySelectorAll('input[type="text"]');

//     [...inputFields].forEach(el => {
//         el.addEventListener('focus', sectionFocusedEventHandler);
//         el.addEventListener('blur', sectionBluredEventHandler);
//     })
// }

function solve() {
    const sections = Array.from(document.querySelectorAll('.panel'));

    sections.forEach(panel => {
        const input = panel.querySelector('input');

        input.addEventListener('focus', () => {
            panel.classList.add('focused');
        });
        
        input.addEventListener('blur', () => {
            panel.classList.remove('focused');
        });
    
    });
    

    console.log(sections);
}
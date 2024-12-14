function checkForPalindromes(numbers) {
    
    const isPalindrome = (num) => {
        const strNum = num.toString();
        const strNumReversed = strNum.split('').reverse().join('');

        return strNum === strNumReversed;
    }

    numbers.forEach(num => console.log(isPalindrome(num)));
}

checkForPalindromes([123,323,421,121]);
// false
// true
// false
// true

console.log('-----');
checkForPalindromes([32,2,232,1010]);
// false
// true
// true
// false
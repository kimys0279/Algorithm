/**
 * @param {string} s
 * @return {string}
 */
 var longestPalindrome = function(str) {
    if (str.length < 1 || str === null) return '';
    
    let longest = '';
    
    for (let i = 0; i < str.length; i++) {
        let oddPalindrome = expandFromCenter(str, i, i);
        let evenPalindrome = expandFromCenter(str, i-1, i);
        
        if (oddPalindrome.length > longest.length) {
            longest = oddPalindrome;
        }
        if (evenPalindrome.length > longest.length) {
            longest = evenPalindrome;
        }
    }
    return longest;
};

function expandFromCenter(str, left, right) {
    let i = 0;
    while (str[left - i] && str[left - i] === str[right + i]) {
        i++;
        
    }
    i--;
    
    return str.slice(left - i, right + i + 1);
}
//create a function that takes a string and returns the string reversed
function reverseString(str) {
  return str.split('').reverse().join('');
}

module.exports = reverseString;

//create regex to match a phone number in the format of 123-456-7890
const phoneNumberRegex = /\d{3}-\d{3}-\d{4}/;



// write a function that takes a string and returns the first phone number it finds and returns it in the format with regex
function findPhoneNumber(str) {
  const phoneNumberRegex = /\d{3}-\d{3}-\d{4}/;
  const match = str.match(phoneNumberRegex);
  return match ? match[0] : null;
}

// export the function
module.exports = findPhoneNumber;

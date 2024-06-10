const findPhoneNumber = require("../src/regex");

describe("findPhoneNumber", () => {


  test("it should return the first phone number in the string", () => {
    const input = "My phone number is 123-456-7890";
    const output = "123-456-7890";
    expect(findPhoneNumber(input)).toEqual(output);
  });

  test("it should return null if no phone number is found", () => {
    const input = "This string does not contain a phone number";
    const output = null;
    expect(findPhoneNumber(input)).toEqual(output);
  });

  test("it should return the first phone number even if there are multiple phone numbers in the string", () => {
    const input = "My phone numbers are 123-456-7890 and 987-654-3210";
    const output = "123-456-7890";
    expect(findPhoneNumber(input)).toEqual(output);
  });


  
});
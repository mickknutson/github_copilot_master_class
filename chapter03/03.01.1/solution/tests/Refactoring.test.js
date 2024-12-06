const { add, addAll, isPrime } = require('../Refactoring');

test('add function - valid inputs', () => {
  expect(add(2, 3)).toBe(5);
  expect(add(-1, 1)).toBe(0);
});

test('add function - null inputs', () => {
  expect(() => add(null, 3)).toThrow("Invalid input: one or both arguments are null");
  expect(() => add(2, null)).toThrow("Invalid input: one or both arguments are null");
});

test('addAll function - valid inputs', () => {
  expect(addAll(1, 2, 3)).toBe(6);
  expect(addAll(0, 0, 0)).toBe(0);
});

test('addAll function - null inputs', () => {
  expect(() => addAll(1, null, 3)).toThrow("Invalid input: one or more arguments are null");
  expect(() => addAll(null)).toThrow("Invalid input: one or more arguments are null");
});

test('isPrime function - valid inputs', () => {
  expect(isPrime(2)).toBe(true);
  expect(isPrime(4)).toBe(false);
  expect(isPrime(17)).toBe(true);
});

test('isPrime function - edge cases', () => {
  expect(isPrime(0)).toBe(false);
  expect(isPrime(1)).toBe(false);
  expect(isPrime(-5)).toBe(false);
});

test('isPrime function - null input', () => {
  expect(() => isPrime(null)).toThrow("Invalid input: argument is null");
});
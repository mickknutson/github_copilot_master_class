// Description: calculator function

/**
 * Performs arithmetic operations on two numbers.
 *
 * @param {number} a - The first number.
 * @param {number} b - The second number.
 * @param {string} operator - The arithmetic operator (+, -, *, /).
 * @returns {number} The result of the arithmetic operation.
 * @throws {Error} If an invalid operator is provided.
 */
function calculator(a, b, operator) {
  switch (operator) {
    case '+':
      return a + b;
    case '-':
      return a - b;
    case '*':
      return a * b;
    case '/':
      return a / b;
    default:
      throw new Error('Invalid operator');
  }
}
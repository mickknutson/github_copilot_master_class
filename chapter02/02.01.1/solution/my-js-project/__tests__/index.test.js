const helloWorld = require('../src/index');

test('helloWorld function returns the correct greeting', () => {
  const result = helloWorld();
  expect(result).toBe('Hello, World!');
});
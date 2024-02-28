// Code refactoring example:
// Prompt: Can you please help me to make sure that the functions can handle exception cases like null or divide by zero?

function add(a, b) {
  return a + b;
}

function addAll(...args){
    return args.reduce((a, b) => a+ b, 0);
}

function isPrime(num) {
  if (num <= 1) {
    return false;
  }
  
  for (let i = 2; i <= Math.sqrt(num); i++) {
    if (num % i === 0) {
      return false;
    }
  }
  
  return true;
}

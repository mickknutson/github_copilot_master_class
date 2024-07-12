// Code refactoring example:

// Prompt: Can you please help me to make sure that the functions can handle exception cases like null or divide by zero?

// Make sure that the functions can handle exception cases lke null or divide by zero?

function add(a, b) {
  try {
    return a + b;
  } catch (error) {
    console.error('Error occurred while adding:', error);
    return null;
  }
}

function addAll(...args){
  try {
    return args.reduce((a, b) => a+ b, 0);
  } catch (error) {
    console.error('Error occurred while adding all:', error);
    return null;
  }
}

function isPrime(num) {
  try {
    if (num <= 1) {
      return false;
    }
    
    for (let i = 2; i <= Math.sqrt(num); i++) {
      if (num % i === 0) {
        return false;
      }
    }
    
    return true;
  } catch (error) {
    console.error('Error occurred while checking prime:', error);
    return null;
  }
}

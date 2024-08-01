function add(a, b) {
  try {
    if (a === null || b === null) {
      throw new Error('Null values are not allowed');
    }
    return a + b;
  } catch (error) {
    console.error('Error occurred while adding:', error);
    return null;
  }
}

function addAll(...args){
  try {
    if (args.some(arg => arg === null)) {
      throw new Error('Null values are not allowed');
    }
    return args.reduce((a, b) => a + b, 0);
  } catch (error) {
    console.error('Error occurred while adding all:', error);
    return null;
  }
}

function isPrime(num) {
  try {
    if (num === null) {
      throw new Error('Null value is not allowed');
    }
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

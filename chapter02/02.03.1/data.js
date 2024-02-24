// create  function that creates 10 random numbers and returns them in an array
function createRandomNumbers() {
  var numbers = [];
  for (var i = 0; i < 10; i++) {
    numbers.push(Math.random());
  }
  return numbers;
}
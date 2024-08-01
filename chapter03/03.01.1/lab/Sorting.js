// 03.01.1 Description: Explain and transform a sort algorithm.

// 03.01.1 Description: Implement a sort algorithm.

// I have a very large list of email addesses that I need to sort. I have a function that sorts the list, but it is not working. Can you help me fix it?

// I have a very large list of email addesses that I need to sort. I have a function that sorts the list, but dos not perform well. Can you help me fix it?

// I have a very large list of email addesses that I need to sort. What are some ways I can improve the performance of the sorting algorithm?

// I have a very large list of email addesses that I need to sort. What are the differet sorting algorithms that I can use?

/**
 * Sorts an array in ascending order using the insertion sort algorithm.
 * 
 * 
 * @param {Array} arr - The array to be sorted.
 * @returns {Array} - The sorted array.
 */
/**
 * Sorts an array in ascending order using the insertion sort algorithm.
 * 
 * @param {Array} arr - The array to be sorted.
 * @returns {Array} - The sorted array.
 */
function sort(arr) {
  for (let i = 1; i < arr.length; i++) {
    let current = arr[i];
    let j = i - 1;
    while (j >= 0 && arr[j] > current) {
      arr[j + 1] = arr[j];
      j--;
    }
    arr[j + 1] = current;
  }
  return arr;
}

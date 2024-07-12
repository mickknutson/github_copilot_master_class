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

/**
 * Sorts an array in ascending order using the quicksort algorithm.
 * 
 * @param {Array} arr - The array to be sorted.
 * @returns {Array} - The sorted array.
 */
function quickSort(arr) {
  if (arr.length <= 1) {
    return arr;
  }
  
  const pivot = arr[Math.floor(arr.length / 2)];
  const left = [];
  const right = [];
  
  for (let i = 0; i < arr.length; i++) {
    if (i === Math.floor(arr.length / 2)) {
      continue;
    }
    
    if (arr[i] < pivot) {
      left.push(arr[i]);
    } else {
      right.push(arr[i]);
    }
  }
  
  return [...quickSort(left), pivot, ...quickSort(right)];
}

/**
 * Sorts an array in ascending order using the merge sort algorithm.
 * 
 * @param {Array} arr - The array to be sorted.
 * @returns {Array} - The sorted array.
 */
function mergeSort(arr) {
  if (arr.length <= 1) {
    return arr;
  }
  
  const mid = Math.floor(arr.length / 2);
  const left = arr.slice(0, mid);
  const right = arr.slice(mid);
  
  return merge(mergeSort(left), mergeSort(right));
}

function merge(left, right) {
  const result = [];
  let i = 0;
  let j = 0;
  
  while (i < left.length && j < right.length) {
    if (left[i] < right[j]) {
      result.push(left[i]);
      i++;
    } else {
      result.push(right[j]);
      j++;
    }
  }
  
  return [...result, ...left.slice(i), ...right.slice(j)];
}

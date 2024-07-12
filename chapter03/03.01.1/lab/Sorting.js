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
    let result = [];
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

    return result.concat(left.slice(i)).concat(right.slice(j));
}

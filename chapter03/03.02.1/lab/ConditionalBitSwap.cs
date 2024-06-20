// Description: Conditional bit swap
/*

Generate a function 'conditionalBitSwap' that takes in 4 arguments:
- 'arr1': an array of char 
- 'arr2': an array of char 
- 'm': a char that represents a char bit mask.
- 'arrLen': a size_t that represents the length of the array.

Implementation details:
- the conditionalBitSwap function swaps the bits in the same positions
of the elements of two arrays, but only if the corresponding bit
in the mask is set and the bits to be swapped are different.
- the conditionalBitSwap function should not return anything.

Example:
arr1 = [0b1010, 0b1100]
arr2 = [0b0110, 0b0011]
m = 0b1010

After calling conditionalBitSwap(arr1, arr2, m), arr1 and arr2 should be:
arr1 = [0b0010, 0b0110]
arr2 = [0b1110, 0b1001]
*/
// C++
// Create a conditionalBitSwap method using the following CPP method signature:
// void conditionalBitSwap(char arr1[], char arr2[], char m, size_t arrLen) {
//     for (size_t i = 0; i < arrLen; i++) {
//         char mask = 1;
//         for (int j = 0; j < 8; j++) {
//             if ((m & mask) && ((arr1[i] & mask) != (arr2[i] & mask))) {
//                 arr1[i] ^= mask;
//                 arr2[i] ^= mask;
//             }
//             mask <<= 1;
//         }
//     }
// }

// C# code
// public void conditionalBitSwap(char[] arr1, char[] arr2, char m, int arrLen)
// {
//     for (int i = 0; i < arrLen; i++)
//     {
//         if ((m & (1 << i)) != 0 && arr1[i] != arr2[i])
//         {
//             arr1[i] ^= arr2[i];
//             arr2[i] ^= arr1[i];
//             arr1[i] ^= arr2[i];
//         }
//     }
// }

// public void conditionalBitSwap(char[] arr1, char[] arr2, char m, int arrLen)
// {
//     for (int i = 0; i < arrLen; i++)
//     {
//         char mask = 1;
//         for (int j = 0; j < 8; j++)
//         {
//             if ((m & mask) != 0 && ((arr1[i] & mask) != (arr2[i] & mask)))
//             {
//                 arr1[i] ^= mask;
//                 arr2[i] ^= mask;
//             }
//             mask <<= 1;
//         }
//     }
// }
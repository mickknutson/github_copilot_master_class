// Description: Condistional bit swap
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

using System;
using System.Diagnostics;

namespace chapter03
{
    public class BitSwapBenchmark
    {
        public static void conditionalBitSwap(char[] arr1, char[] arr2, char m, int arrLen)
        {
            for (int i = 0; i < arrLen; i++)
            {
                char mask = (char)(1 << i);
                if ((m & mask) != 0)
                {
                    char bit1 = (char)(arr1[i] & mask);
                    char bit2 = (char)(arr2[i] & mask);
                    if (bit1 != bit2)
                    {
                        arr1[i] ^= mask;
                        arr2[i] ^= mask;
                    }
                }
            }
        }

        public static void Main(string[] args)
        {
            char[] arr1 = { 0b1010, 0b1100 };
            char[] arr2 = { 0b0110, 0b0011 };
            char m = 0b1010;
            int arrLen = 2;

            conditionalBitSwap(arr1, arr2, m, arrLen);

            Debug.Assert(arr1[0] == 0b0010);
            Debug.Assert(arr1[1] == 0b0110);
            Debug.Assert(arr2[0] == 0b1110);
            Debug.Assert(arr2[1] == 0b1001);
        }
    }
}

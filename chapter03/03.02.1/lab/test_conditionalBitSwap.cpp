#include <cassert>
#include <vector>

void test_conditionalBitSwap() {
    std::vector<char> arr1 = {0b1010, 0b1100};
    std::vector<char> arr2 = {0b0110, 0b0011};
    char m = 0b1010;

    conditionalBitSwap(arr1, arr2, m);

    assert(arr1[0] == 0b0010);
    assert(arr1[1] == 0b0110);
    assert(arr2[0] == 0b1110);
    assert(arr2[1] == 0b1001);
}

int main() {
    test_conditionalBitSwap();
    return 0;
}
def test_sort():
    # Test that sort function sorts the array in ascending order
    array = [17, 9, 13, 8, 7, -5, 6, 11, 3, 4, 1, 2]
    expected_result = [-5, 1, 2, 3, 4, 6, 7, 8, 9, 11, 13, 17]
    sort(array)
    assert array == expected_result
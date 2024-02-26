import sys

sys.path.append('src')

from index import hello_world

def test_hello_world():
    # Test that hello_world function returns the correct message
    expected_message = "Hello, World!"
    result = hello_world()
    assert expected_message == result

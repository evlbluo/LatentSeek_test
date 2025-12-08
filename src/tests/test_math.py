from src.my_tool import my_super_add  # this is my tests

def test_add_positive():
    assert my_super_add(1, 2) == 3

def test_add_negative():
    assert my_super_add(-1, -1) == -2
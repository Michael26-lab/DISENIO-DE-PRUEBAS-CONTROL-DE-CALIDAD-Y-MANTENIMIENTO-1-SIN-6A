from src.binary_search import binary_search

def test_found_beginning():
    assert binary_search([1,2,3,4], 1) == 0

def test_found_middle():
    assert binary_search([1,2,3,4], 3) == 2

def test_found_end():
    assert binary_search([1,2,3,4], 4) == 3

def test_not_found():
    assert binary_search([1,2,3,4], 5) == -1

from src.binary_search import binary_search

def test_empty():
    assert binary_search([], 1) == -1

def test_one_element_found():
    assert binary_search([7], 7) == 0

def test_one_element_not_found():
    assert binary_search([7], 1) == -1

def test_duplicates():
    arr = [1,2,2,2,3]
    idx = binary_search(arr, 2)
    assert idx in [1,2,3]

def test_even_length_list():
    arr = [10,20,30,40]
    assert binary_search(arr, 20) == 1

def test_negative_numbers():
    arr = [-10, -5, 0, 5, 10]
    assert binary_search(arr, -5) == 1

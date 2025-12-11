def binary_search(arr, target):
    """
    Búsqueda binaria clásica.
    Devuelve el índice del elemento si lo encuentra, -1 si no.
    """
    lo = 0
    hi = len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

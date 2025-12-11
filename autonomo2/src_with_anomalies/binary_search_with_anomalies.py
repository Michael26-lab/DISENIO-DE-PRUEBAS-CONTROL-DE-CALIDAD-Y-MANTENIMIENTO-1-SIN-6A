def binary_search_bad(arr, target):
    """
    Versión con anomalías intencionales:
    - anomalía 1: hi se modifica incorrectamente en una rama (bug)
    - anomalía 2: variable asignada y no usada (unused_var)
    """
    unused_var = 10  # anomalía 1: variable asignada y nunca usada

    lo = 0
    hi = len(arr) - 1
    result = None
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            result = mid
            break
        elif arr[mid] < target:
            lo = mid + 1
        else:
            # anomalía 2: bug intencional (debería ser hi = mid - 1)
            hi = hi - 1
    # resultado puede ser None en vez de -1 -> comportamiento defectuoso
    return result


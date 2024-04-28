def bubblesort(arr):
    # Teie kood läheb siia
    pass


def test_bubblesort():
    assert bubblesort([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]
    assert bubblesort([5, 1, 4, 2, 8]) == [1, 2, 4, 5, 8]
    assert bubblesort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    print('All tests passed.')


if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(bubblesort(arr))
    test_bubblesort()

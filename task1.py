def bubble_sort(arr):
    n = len(arr)
    # Если не было пререстановок, то массив отсортирован
    swapped = False
    for i in range(n - 1):
        # Все элементы меньше i будут отсортированны с помощью второго loop
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if not swapped:
            return


arr = [i for i in range(100)]

arr.reverse()

print(arr)

bubble_sort(arr)

print(arr)
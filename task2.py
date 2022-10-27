def three_n(arr1, const):
    for i in range(len(arr1)):
        arr1[i] += const

    for i in range(len(arr1)):
        arr1[i] += const

    for i in range(len(arr1)):
        arr1[i] += const


# алгоритм quicksort
def nlogn(array):

    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return nlogn(less)+equal+nlogn(greater)
    else:
        return array


# Алгоритм пермутаций
def factorial(lst):
    # Если массив пустой, то нет пермутаций
    if len(lst) == 0:
        return []

    # 1 элемент - 1 пермутация
    if len(lst) == 1:
        return [lst]

    l = []  # будет хранить пермутации

    for i in range(len(lst)):
        m = lst[i]

        remLst = lst[:i] + lst[i + 1:]

        for p in factorial(remLst):
            l.append([m] + p)
    return l

def n_to_the_power_of_3(cube_array_3d, const):
    for x in range(len(cube_array_3d)):
        for y in range(len(cube_array_3d)):
            for z in range(len(cube_array_3d)):
                cube_array_3d[x][y][z] *= const

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    iterations = 0
    while low <= high:
        mid = (high + low) // 2
        # Если x больше, игнорируй левую часть
        if arr[mid] < x:
            low = mid + 1
            iterations += 1
        # Если x меньше, игнорируй правую часть
        elif arr[mid] > x:
            high = mid - 1
            iterations += 1
        # x означает что индекс x является mid
        else:
            return mid, iterations
    # Если тут, то элемент не находится в массиве.
    return -1, iterations

def three_logn(arr1, x, y, z, const):
    _, idx = binary_search(arr1, x)
    arr1[idx] *= const

    _, idx = binary_search(arr1, y)
    arr1[idx] *= const

    _, idx = binary_search(arr1, z)
    arr1[idx] *= const
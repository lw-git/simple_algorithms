def countdown(i):
    print(i)
    if i <= 0:
        return
    else:
        countdown(i - 1)


countdown(5)


def summ(arr):
    if arr == []:
        return 0
    else:
        return arr[0] + summ(arr[1:])


print(summ([1, 2, 3, 4, 5, 6, 7]))


def counter(arr):
    if arr == []:
        return 0
    else:
        return 1 + counter(arr[1:])


print(counter([1, 2, 3, 4, 5, 6, 7, 8, 9]))


def maxn(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        m = maxn(arr[1:])
        return m if m > arr[0] else arr[0]


print(maxn([1, 2, 3, 4, 5, 6, 7, 8, 9]))


def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort([10, 5, 2, 3]))

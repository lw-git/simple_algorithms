def binary_search(list_, item):
    low = 0
    high = len(list_) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list_[mid]
        if guess == item:
            return mid

        if guess > item:
            high = mid - 1
        else:
            low = mid + 1


my_list = [i for i in range(1000)]

print(binary_search(my_list, 5))
print(binary_search(my_list, -1))
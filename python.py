def binary_search(list1, item):
    first, last = 0, len(list1) - 1
    while first <= last:
        mid = (first + last) // 2
        if list1[mid] == item:
            return True
        elif item > list1[mid]:
            first = mid + 1
        else:
            last = mid - 1
    return False


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(binary_search(list1, 4))
print(binary_search(list1, 0))

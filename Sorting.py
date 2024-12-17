
#--------------------------------QUICK SORT----------------------
import random
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = random.choice(arr)
        left = [x for x in arr if x < pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)

quick_sort([1,3,4,2,8,5,9,6])
quick_sort([1,3,4,2,8,5,9,6,10,17,18,15,14,20])

# quick_sort ---> O(n log n) worst case --> O(n^2)


# -----------------------MERGE SORT------------------------------------
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1

            else:
                arr[k] = right[j]
                j += 1

            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

        return arr

merge_sort([2,5,8,1,4,0])

# merge_sort ---> O(n log n)


# --------------------BUBLE SORT--------------------------
def buble_sort(lst):
    n = len(lst)
    for x in range(n):
        for i in range(x+1,n):
            if lst[x] > lst[i]:
                lst[x], lst[i] = lst[i], lst[x]
    return lst

buble_sort([2,-1,0,4,7,4,9,3])
buble_sort([-1,2,0,4,7,4,9,3])
buble_sort([-1,0,2,4,7,4,9,3])
buble_sort([-1,0,2,3,4,7,4,9])
buble_sort([-1,0,2,3,4,4,7,9])

# buble_sort ---> O(n^2)


# -------------------------SELECTION SORT--------------------------------
def Selection_sort(arr):
    n = len(arr)
    for index in range(n):
        min_index = index
        for j in range(index + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        (arr[index], arr[min_index]) = (arr[min_index], arr[index])
    return arr

Selection_sort([7,4,1,6,2,8])


# --------------------------INSERTION SORT-------------------------------
def insertion_sort(arr):
    n = len(arr)
    if n <= 1:
        return

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

insertion_sort([12, 11, 13, 5, 6])


# -----------------------COUNTING SORT------------------------------
def count_sort(arr):
    m = max(arr)
    count_array = [0] * (m + 1)
    for num in arr:
        count_array[num] += 1

    for i in range(1, m + 1):
        count_array[i] += count_array[i - 1]

    output_array = [0] * len(arr)

    for i in range(len(arr) - 1, -1, -1):
        output_array[count_array[arr[i]] - 1] = arr[i]
        count_array[arr[i]] -= 1

    return output_array

count_sort([3,4,2,5,1])



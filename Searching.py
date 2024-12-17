
#------------------------------BINARY SEARCH----------------------
def binarySearch(arr, x):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = low + (high - low) // 2 # Kelgan index ni teng yarimga bolib turadi
        if arr[mid] == x:
            return mid

        elif arr[mid] < x: # Qidirayotgan sonimiz mid dan katta bosa mid dan tepani qidirish uchun
            low = mid + 1

        else:              # Qidirayotgan sonimiz mid dan kichik bosa mid dan pasgi taraf qidirish uchun
            high = mid - 1

    return -1

binarySearch([1,2,3,4,5,6,7],6)


#------------------------------LINEAR SEARCH------------------
def linear_search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index

    return -1

linear_search([1,2,3,4,5,6,7],6)


#------------------------------LINEAR SEARCH------------------
def interpolation_search(data, arr):
    low = 0
    high = len(arr) - 1
    index = -1
    while low <= high:
        mid = low + ((high - low) * (data - arr[low]) // (arr[high] - arr[low]))
        if arr[mid] == data:
            index = mid
            break
        else:
            if arr[mid] < data:
                low = mid + 1
            else:
                high = mid - 1
    return index

interpolation_search(33, [10, 14, 19, 26, 27, 31, 33, 35, 42, 44])
interpolation_search(6, [1,3,4,5,6,9])


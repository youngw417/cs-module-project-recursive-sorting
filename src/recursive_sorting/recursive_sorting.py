# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [] 
    left_index = 0
    right_index = 0

    # Your code here
    while left_index < len(arrA) and right_index < len(arrB):
        if arrA[left_index] < arrB[right_index]:
            merged_arr.append(arrA[left_index])
            left_index += 1
        else:
            merged_arr.append(arrB[right_index])
            right_index += 1

    merged_arr += arrA[left_index:] + arrB[right_index:]
    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Your code here
    if len(arr) == 1 or len(arr) == 0:
        return arr
    mid_index = len(arr) // 2
    left = arr[: mid_index]
    right = arr[mid_index:]
    print('left', left)
    print('right', right)

    return merge(merge_sort(left), merge_sort(right))

# my_arr = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
# # print(len(my_arr))
# print(merge_sort(my_arr))


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here
    start_r = mid + 1

    if arr[mid] < arr[start_r]:
        return
    
    while start <= mid and start_r <= end:
        if arr[start] < arr[start_r]:
            start += 1
        else:
            temp = arr[start_r]
            temp_ind = start_r
            #shifting elements to right by 1
            while temp_ind is not start:
                arr[temp_ind] = arr[temp_ind - 1]
                temp_ind -= 1

            arr[start] = temp

            start += 1
            mid += 1
            start_r += 1



    return arr



def merge_sort_in_place(arr, l, r):
    # Your code here
    
    if l < r:
        mid = (l + r) // 2

        merge_sort_in_place(arr, l, mid)
        merge_sort_in_place(arr, mid + 1, r)
        merge_in_place(arr, l, mid, r)


    return arr

my_arr = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
# print(len(my_arr))
print(merge_sort_in_place(my_arr, 0, len(my_arr) - 1))

# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr

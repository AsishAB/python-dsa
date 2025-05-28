list_of_num = [5,7,99,1,3,8]

def bubble_sort(num):
    print(f"Original Array = {num}")
    num = list(num) # Replace nums, with a copy of nums , to avoid changing the original array
    for j in range(len(num) - 1):
        for i in range(len(num) - 1):
            if num[i] > num[i+1]:
                # temp = num[i+1]
                # num[i+1] = num[i]
                # num[i] = temp
                num[i], num[i+1] = num[i+1], num[i]
                print(num)
                
                
     
    return num

# print(bubble_sort(list_of_num))

# Insertion Sort
def insertion_sort(num):
    num = list(num)
    for i in range(len(num)):
        cur = num.pop(i)
        j = i - 1
        while j >= 0 and num[j] > cur:
            j -= 1
        num.insert(j + 1 , cur)
    return num

# print(insertion_sort(list_of_num))

def merge(num1, num2):
    # For Ascending Order
    # Compare the smallest of the number of two arrays. 
    # Create a new array and keep pushing the smallest number to the new array

    merged = []
    i, j = 0, 0 # For iteration
    while i < len(num1) and j < len(num2):
        if num1[i] < num2[j]:
            merged.append(num1[i])
            i += 1
        else:
            merged.append(num2[j])
            j += 1

    # get the remaining parts of the array. 
    # if there are no elements left to be compared, we get out of the loop and merge them with the already sorted merged[]
    num1_tail = num1[i:]
    num2_tail = num2[j:]

    return merged + num1_tail + num2_tail

def merge_sort(num):
    # Merge Sort , assuming we have a helper function called merge()
    if len(num) <= 1:
        return num
    mid = len(num) // 2
    left = num[:mid] # this also means num[0:mid]
    right  = num[mid:]

    left_sorted, right_sorted = merge_sort(left), merge_sort(right)
    sorted_num = merge(left_sorted, right_sorted)
    return sorted_num


# print(merge_sort(list_of_num))
# Merge Sort has better computational speed, but higher memory consumption. Memory consumption is costlier


# Quick Sort
# Pick a random element from the list, preferrably the last, called the pivot
# Put all the elements smaller than this number, to the left
# Put all the elements larger than this number to the right.
# Repeat the process for left and right lists
# Merge all the arrays

def partition(num, start, end):
    # pivot  = num[len(num)-1]
    if end is None:
        end = len(num) - 1
    # Initiate left and right pointers
    l, r = start, end - 1 # end - 1 => We take the last element as pivot, so we take comparison for all the array elements, excluding the last element
    while r > l:
        # Increment left pointer if number is less than or equal to pivot
        if num[l] <= num[end]: 
            l += 1
        # Decrement right pointer if number is greater than pivot
        if num[r] > num[end]:
            r -= 1
        else:
            # Two out-of-place elements found, swap them
            num[l], num[r] = num[r], num[l]
            l += 1
            r -= 1

    # Place the pivots between the two parts
    if num[l] > num[end]:
        num[l], num[end] = num[end], num[l]
        return l
    else:
        return end
    
    

def quick_sort(num, start=0, end=None):
    # Something is wrong in the code or partition(). Fix it
    if end is None:
        num = list(num)
        end = len(num) - 1

    if start  < end:
        pivot = partition(num, start, end)
        quick_sort(num, start, pivot - 1)
        quick_sort(num, pivot + 1, end)

    return num



print(quick_sort(list_of_num))
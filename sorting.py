list_of_num = [5,7,99,1,3,8]

def bubble_sort(num):
    print(f"Original Array = {num}")
    nums = list(nums) # Replace nums, with a copy of nums , to avoid changing the original array
    for j in range(len(num) - 1):
        for i in range(len(num) - 1):
            if num[i] > num[i+1]:
                # temp = num[i+1]
                # num[i+1] = num[i]
                # num[i] = temp
                num[i], num[i+1] = num[i+1], num[i]
                print(num)
                
                
     
    return num

print(bubble_sort(list_of_num))
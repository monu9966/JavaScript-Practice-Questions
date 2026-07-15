# arr = [ 1, 2, 3, 4, 5]
# for i in arr:
#     print(i, end=" ")

# res = arr[:]
# print(res)
# Array Problems

#1. Second Largest Element in an Array
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# arr.sort()
# print("Second Largest:", arr[-2])

largest = -1
second_largest = -1

for num in arr:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num < largest:
        second_largest = num

print("Second Largest:", second_largest)

#2 Third Largest Element in an Array
# arr.sort()
# print("Third Largest:", arr[-3])
largest = -1
second_largest = -1
third_largest = -1 

for num in arr:
    if num > largest:
        third_largest = second_largest
        second_largest = largest
        largest = num

    elif num > second_largest and num < largest:
        third_largest = second_largest
        second_largest = num

    elif num > third_largest and num < second_largest:
        third_largest = num

print("Third Largest:", third_largest)

arr = [10, 20, 30, 40, 50]

#3. Array Reverse
# arr.reverse()
# print(arr)

# solution2
left = 0
right = len(arr) - 1

while left < right:
    arr[left], arr[right] = arr[right], arr[left]

    left += 1
    right -= 1

print(arr) 

#4. Rotate an Array by d - Counterclockwise or Left
# Given an array of integers arr[] of size n, the task is to rotate the array elements to the left by d positions.

# Method 1 using slicing.
arr = [1, 2, 3, 4, 5, 6]
d = 2

d = d % len(arr)

arr = arr[d:] + arr[:d]
print(arr)

#Method 2 one rotation at a time.
arr = [1, 2, 3, 4, 5, 6]
d = 2

for i in range(d):
    first = arr[0]

    for j in range(len(arr) - 1):
        arr[j] = arr[j + 1]

    arr[-1] = first

print(arr)


#6. Maximum product of a triplet (subsequence of size 3) in array.
arr = [-10, -9, 50, 20]

arr.sort()
product1 = arr[-1] * arr[-2] * arr[-3]
product2 = arr[0] * arr[1] * arr[-1]

print(max(product1, product2))

#7. Maximum consecutive one’s (or zeros) in a binary array
#Given a binary array arr[] consisting of only 0s and 1s, find the length of the longest contiguous sequence of either 1s or 0s in the array.

arr = [1, 1, 0, 0, 0, 1, 1, 1]

count = 1
maximum = 1

for i in range(1, len(arr)):
    if arr[i] == arr[i - 1]:
        count += 1
    else:
        count = 1

    if count > maximum:
        maximum = count

print("Longest Sequence:", maximum)

#8. Move all Zeros to End of Array
# Given an array of integers arr[], move all the zeros to the end of the array while maintaining the relative order of all non-zero elements.

arr = [1, 0, 5, 0, 6, 0, 8]

index = 0

for i in range(len(arr)):
    if arr[i] != 0:
        arr[index] = arr[i]
        index += 1
    
while index < len(arr):
    arr[index] = 0
    index += 1

print(arr)

#9. Sort an array in wave form
#Given a sorted array arr[] of integers (in ascending order), rearrange the elements in-place to form a wave-like array.
#An array is said to be in wave form if it satisfies the following pattern: arr[0] ≥ arr[1] ≤ arr[2] ≥ arr[3] ≤ arr[4] ≥ ...
#In other words, every even-indexed element should be greater than or equal to its adjacent odd-indexed elements (if they exist).

def sort_in_wave(arr):

    n = len(arr)

    #swap adjacent elements
    for i in range(0, n -1, 2):
        arr[i], arr[i+1] = arr[i+1], arr[i]
    
arr = [1, 2, 3, 4, 5]
sort_in_wave(arr)
for i in range(0, len(arr)):
    print(arr[i], end=" ")
print()

# 10. adding one to number represented as array of digits

#iven a non-negative number represented as an array of digits. The task is to add 1 to the number (increment the number represented by the digits by 1). The digits are stored such that the most significant digit is the first element of the array.]

def add_one(arr):

    carry = 1

    for i in range(len(arr) -1, -1, -1):
        sum = arr[i] + carry
        arr[i] = sum % 10
        carry = sum // 10

    if carry:
        arr.insert(0, carry)
    
    return arr
arr = [9, 9, 9]
res = add_one(arr)

for i in res:
    print(i, end="")

print()
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


# Alternate elements of an array

elements = [10, 20, 30, 40, 50]

#solution 1
for i in range(0, len(elements), 2):
    print(elements[i], end=" ")

print()

#solution 1
ailternate_ele = elements[::2]
print(*ailternate_ele)


# Find all leaders
arr = [16, 17, 17, 4, 3, 5, 2]

#time complexity O(n*2), sc : O(K) where k is the leaders
# leaders = []
# #solution 1
# for i in range(len(arr)):
#     is_leader = True
#     for j in range(i + 1, len(arr)):
#         if arr[i] < arr[j]:
#             is_leader = False
#             break
#     if is_leader:
#         leaders.append(arr[i])

# print(*leaders)

#solution 2
# for i in range(len(arr) - 1):
#     if arr[i] >= max(arr[i+1::]):
#         leaders.append(arr[i])
    
# print(leaders)

# solution 3

current_Index = 0
leaders = []
while(current_Index < len(arr)):
    is_leader = True
    for i in range(current_Index+1, len(arr)):
        if arr[current_Index] < arr[i]:
            current_Index = i 
            is_leader = False
            break
    if is_leader:
        leaders.append(arr[current_Index])
        current_Index += 1

print(leaders)

#Remove duplicates from Sorted Array

#solution 1
arr = [1, 3, 3, 4, 5]

result = list(set(arr))

print(result)

# Generating All Subarrays
arr = [1, 2, 3]
for i in range(len(arr)):
    for j in range(len(arr) - 1):
        print(arr[j: j + i + 1], end=" ")
print() # mt print function for next line

# Array Reverse
arr = [1, 4, 3, 2, 6, 5]
for i in range(len(arr) - 1 , -1, -1):
    print(arr[i], end=" ")


print("Hello")

#Rotate an Array - Clockwise or Right
arr = [1, 2, 3, 4, 5, 6]
d = 2

def rotatrArr(arr:list):
    temp = arr[-1]

    for i in range(len(arr) -1, 0, -1):
        arr[i] = arr[i-1]
        arr[0] = temp
        print(arr)

#swapper two elements

position1 = "Monu"
position2 = "Ritu"

print(position1, position2)
temp = position1
position1 = position2
position2 = temp
print(position1, position2)

position1, position2 = position2, position1
print(position1, position2)

# rotate array elements clockwise d times
def rotateArr(arr:list)-> None:
    temp = arr[-1]

    for i in range(len(arr) -1, 0, -1):
        arr[i] = arr[i-1]

    arr[0] = temp

n = 4

print("Original Array")
arr = [1,2,3,4,5,6]

temp = 1
print(arr)
l = len(arr)

for _ in range(n):
    rotateArr(arr=arr)
    print(arr)

step = n%len(arr)
print(step)

position = [-1]*len(arr)

print("Position")
print(position)

for i in range(len(arr)):
    p = (i+step)%len(arr)
    position[i] = p

print(position)
# temp = arr[-1]

# for i in range(len(arr) -1, 0, -1):
#     arr[i] = arr[i-1]

# arr[0] = temp

# print(arr)

# print("Rotation 2")
# temp = arr[-1]

# for i in range(len(arr) -1, 0, -1):
#     arr[i] = arr[i-1]
# arr[0] = temp
# print(arr)


# Zeros to End
arr = [0, 0, 0, 2, 0, 4, 0, 5]
index = 0
#solution 1
# Move all non-zero elements to the front
for i in range(len(arr)):
    if arr[i] != 0:
        arr[index] = arr[i]
        index += 1

# Fill the remain+
# ing positions with 0
while index < len(arr):
    arr[index] = 0
    index += 1

print(arr)

#Solution 2
arr = [1, 2, 0, 4, 3, 0, 8, 0, 0, 9]
j = 0

for i in range(len(arr)):
    if arr[i] != 0:
        arr[i], arr[j] = arr[j], arr[i]
        j += 1
    
print(arr)


# solution 3
arr = [0, 2, 0, 4, 2]
for i in range(len(arr)):
    if arr[i] == 0:
        arr.pop(i) #0(n)
        arr.append(0) #0(1)
print(arr)

# Solution 4
# Two Pointer
arr = [0, 0, 1,3,5, 0,9, 5]
zero_index = 0
for i in range(len(arr)-1):
    if arr[i] == 0 and arr[i+1] != 0:
        #swap
        arr[i+1], arr[zero_index] = arr[zero_index], arr[i+1]
        zero_index +=1
    elif arr[i] == 0 and arr[i+1] == 0:
        pass
    else:
        zero_index += 1
    
print(arr)

#s4
temp = [0]*len(arr)
print(temp)

curr = 0
for i in arr:
    if i != 0:
        temp[curr] = i
        curr += 1
    print(temp)

#Palindrome
# s1
data = "mam" 
if data == data[::-1]:
    print("palindrome")
else:
    print("Not a palindrome")

#s2
if data[:len(data)//2] == data[len(data)//2:][::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

#s3
i = 0
j = len(data)-1

is_palindrome = True
while(i<=j):
    if data[i] == data[j]:
        i+=1
        j-=1
    else:
        is_palindrome = False
        break

if is_palindrome:
    print("Palindrome")
else:
    print("Not a Palindrome")

#Q.  Minimum increment by k operations to make all equal

arr = [4, 7, 19, 16]

k = 3

highest = max(arr)
operations = 0
for i in arr:
    if (highest - i)%k == 0:
        operations += (highest - i)// k
    else:
        operations = -1
        break

print(operations)


#Minimum cost to make array size 1 by removing larger of pairs
#s1
"""
arr = [4,3,2] # non repeating integers
 i=j
  j  4      3      2
i 4 (4,4)  (4,3)  (4,2)
  3 (3,4)  (3,3)  (3,2)
  2 (2,4)  (2,3)  (2,2)


arr = [1,2,3,4]
  j 4,   3,     2     1
i 1 (1,1) (1,2) (1,3) (1,4)
  2 (2,1) (2,2) (2,3) (2,4)
  3 (3,1) (3,2) (3,3) (3,4)
  4 (4,1) (4,2) (4,3) (4,4)

sort arr in descending order
i from 0->2
j from i+1, 2


total_cost = 0 # 1+2+3 = 6

i from 0->2
  cost = 1 # 1
  j from i+1 , 2
    curr_cost = min(arr[i], arr[j])
    cost = min(cost, curr_cost) # 1
  total_cost += cost




cost = min(arr[i], arr[j])

(4,3) => 3
(4,2) => 2
(3,2) => 2

"""


#s2

arr = [3,5,6]
arr = sorted(arr, reverse=True) #descending
total_cost = 0
print(arr)
for i in range(len(arr)-1):
  cost = arr[i]
  for j in range(i+1, len(arr)):
    cost = min(cost, arr[j])
  total_cost += cost
print(total_cost)


# s3
arr = [10,2,5,1,4,3] # non repeating

min_cost = min(arr) #1
total_cost = 0
for i in arr:
  if i!=min_cost:
    total_cost += min_cost
print(total_cost)

# s4
arr = [10, 2,5,1,4,3]

min_cost = min(arr)  # 0(n)

total_cost = min_cost * (len(arr)-1)

print(total_cost)

 

# find if the array contains any duplicate
a = [1, 2, 2, 1, 4, 5]

def check_duplicate(arr:list)->bool:
  for i in range(len(arr)-1):
    for j in range(i+1, len(arr)):
      if arr[i]==arr[j]:
        return True
  return False
# has_duplicate = False
# for i in range(len(a)-1):
#   for j in range(i+1, len(a)):
#     if a[i]==a[j]:
#       has_duplicate = True
#       break

# print(has_duplicate)


# s2

#     0, 1, 2, 3, 4, 5
a =  [1, 2, 8, 0,5,3,6,1]
#     i----i+k

k = 6

has_duplicate = False
for i in range(len(a)-k+1):
  window_start = i
  window_end = i+k # end is exlcusive
  for j in range(window_start, window_end-1):
    for k in range(j+1, window_end):
      if a[j]==a[k]:
        has_duplicate = True
        break
    if has_duplicate:
      break
  if has_duplicate:
    break

print(has_duplicate)

#s3

#     0, 1, 2, 3, 4, 5
a =  [1, 2, 8,8, 0,5,3,6,1]
#        i----i+k

k = 6
def check_duplicate(arr:list)->bool:
  for i in range(len(arr)-1):
    for j in range(i+1, len(arr)):
      if arr[i]==arr[j]:
        return True
  return False

has_duplicate = False
for i in range(len(a)-k+1):
  window_start = i
  window_end = i+k # end is exlcusive
  window = a[window_start: window_end]
  result = check_duplicate(window)
  if result:
    has_duplicate = True
    break

if has_duplicate:
  print("Duplicate")
else:
  print("No duplicates")



#duplicates in array 
#10 Duplicates problem of an array

arr = [1,2,3,4, 2, 4]
has_duplicate = False

for i in range(len(arr)-1):
    for j in range(i+1, len(arr)):
        if arr[i] == arr[j]:
            has_duplicate = True
            break

print(has_duplicate)

# Count Duplicates
has_duplicate = False
count = 0

for i in range(len(arr)-1):
    for j in range(i+1, len(arr)):
        if arr[i] == arr[j]:
            has_duplicate = True
            count += 1

print(count)

# Print All duplicate elements
arr = [1,2,3,4, 2, 4]

has_duplicate = False
duplicate_element = []

for i in range(len(arr)-1):
    for j in range(i+1, len(arr)):
        if arr[i] == arr[j]:
            has_duplicate = True
            duplicate_element.append(arr[i])
            

print(has_duplicate)
print(duplicate_element)

# Find the First Duplicate Element 
arr = [1,2,3,2,4]

has_duplicate = False

for i in range(len(arr)-1):
    for j in range(i+1, len(arr)):
        if arr[i] == arr[j]:
            print("First duplicate:", arr[i])
            has_duplicate = True
            break
    
#Remove duplicates from an array
print("Remove Element")
arr = [1, 2, 3, 2,4,3]

has_duplicate = False

for i in range(len(arr)-1):
    # print(i)
    for j in range(i+1, len(arr)):
        if arr[i] == arr[j]:
            has_duplicate = True
            arr.pop(j)
            break

print(arr)

#Count frequency of each element
print("Count Frequency")
#s1

arr = [1,2,3,2,4,4,]
visited = []
for i in range(len(arr)):
    if arr[i] in visited:
        continue

    count = 0 

    for j in range(len(arr)):
        if arr[i] == arr[j]:
            count += 1

    print(arr[i], "->", count)
    visited.append(arr[i])

#2
arr = [1,2,3,2,4,4,2]
freq = {}
counter = 0
for i in arr:
    if i in freq:
        freq[i] += 1
        counter += 1
    else:
        freq[i] = 1

for i, count in freq.items():
        print(f"{i}: {count} {counter}")

# Find the highest frequency element
arr = [1,2,2,3,3,3,4]

max_count = 0
max_element = arr[0]

for i in range(len(arr)):
    count = 0

    for j in range(len(arr)):
        if arr[i] == arr[j]:
            count += 1

    if count > max_count:
        max_count = count
        max_element = arr[i]

print("Highest Frequency Element:", max_element)
print("Frequency:", max_count)

#Find All Unique Elements
arr = [1,2,3,3,2,4,5,4]
unique_element = set(arr)
print(unique_element)

#check common elements in two arrays
a = [1,2,3,4,5,6,7,8,9]
b = [1,2,3,4,5, 6,7]

# common_elements = list(set(a) & set(b))
common_elements = list(set(a).intersection(b))
print(common_elements)
 
duplicate = -1
print(duplicate)
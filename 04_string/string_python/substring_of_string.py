# 1. Print a Substring
#Print the substring from index `2` to `5`.
text = input("Enter a string: ")
print(text[2:6])

# 2. Print the First 5 Characters
print(text[:5])

## 3. Print the Last 4 Characters
print(text[-4:])

# 4. Check if a Substring Exists
# Check whether a given substring exists in a string.
string = input("Enter a string: ")
substring = input("Enter a substring: ")
if substring in string:
    print("Substring found")
else:
    print("Substring does not exists")

# 5. Count How Many Times a Substring Appears
count = string.count(substring)
print("Substring appears",count, "times")

# 6. Find the First Occurrence of a Substring
found = False

for i in range(len(string) - len(substring) + 1):
    if string[i:i + len(substring)] == substring:
        print("First occurence at index:", i)
        found = True
        break

if found == False:
    print("substring not found")

# 7. Find the Last Occurrence of a Substring
last_index = -1

for i in range(len(string) - len(substring) + 1):
    if string[i:i  + len(substring)] == substring:
        last_index = i

if last_index != -1:
    print("Last occurrence at index", last_index)
else:
    print("Substring not found") 

# 8. Replace a Substring
# Replace one substring with another.
string = input("Enter a string: ")
old_substring = input("Enter the old substring: ")
new_substring = input("Enter the new substring: ")

result = string.replace(old_substring, new_substring)

print("Update string:", result)

# 9. Remove a Substring
# Remove a given substring from a string.
string = input("Enter a string For Remove Substring: ")
remove = input("Enter a remove substring:")

result = string.replace(remove, "")

print(result)

# 10. Print All Substrings of a String
string = input("Enter a string: ")
for i in range(1, len(string) + 1):
    for j in range(len(string) - i + 1):
        print(string[j:j + i])
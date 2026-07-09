#1. Check if a character exists in a string.
text = input("Enter s string:")
ch = input("Enter a character:")

if ch in text:
    print(f"{ch} exists in string.")
else:
    print(f"{ch} does not exists in string.")

#2. Check if a character does not exist in a string.
#3. Find the last occurrence of a character.
index = text.find(ch)

if index != -1:
    print("First occurrence at index:", index)
else:
    print("Character not found")

#### 4. Find the last occurrence of a character.
last_index = -1
for i in range(len(text)):
    if text[i] == ch:
        last_index = i

if last_index != -1:
    print("Last index at index", last_index)
else:
    print("Character not found")



# for i in range(len(text)):
#     print(i, text[i])

### 5. Count how many times a character appears.
count = 0
for i in range(len(text)):
    if text[i] == ch:
        count = count + 1

if count != 0:
    print("Total character appears is:", count) 
else:
    print("Character dont found") 


### 6. Print all indexes where a character appears.
found = False
for i in range(len(text)):
    if text[i] == ch:
        print(i)
        found = True
    
if found == False:
    print("Character not found")


found = False
### 7. Print the first matching character's index using a loop.
for i in range(len(text)):
    if text[i] == ch:
        print("The first matching character's index is:",i)
        found = True
        break
if found == False:
    print("Character not found")

### 8. Print the last matching character's index using a loop.
last_index = -1
for i in range(len(text)):
    if text[i] == ch:
        last_index = i

if last_index != -1:
    print("last matching character at index:", last_index)
else:
    print("Character not found")

### 9. Check whether a character appears exactly once.
count = 0
for i in range(len(text)):
    if text[i] == ch:
        count = count + 1
if count == 1:
    print("Character appears exactly once.")
else:
    print("Character does not appear exactly once.")

### 10. Check whether a character appears more than once.
count = 0
for i in range(len(text)):
    if text[i] == ch:
        count += 1
if count != 1:
    print("Character appears more than once")
else:
    print("Character does not appears more than once")
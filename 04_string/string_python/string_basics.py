# Part 1: String Basics (1–20)

#1. Print a string
print("Monu")

#2. Take a string as input and print it.
name = "Monu"
print(name)

#3. Find the length of string.
a = "Monu Kumar"
print(len(a))

#4. Print the first character of a string.
b = "Mouse"
print(b[0])

#5. Print the last character of a string.
c = "Computer"
print(c[-1])

#6. Print all character one by one.
d = "Laptop"
for e in d:
    print(e)

#7. Count the number of characters.
f = "Price"
count = 0
for g in f:
    count = count + 1
print(count)
    
#8. Check if a string is empty.
h = "q"
if h == "":
    print("A string is empty")
else:
    print("A string is not empty")

#9. Convert a string to uppercase.
i = "board"
print(i.upper())

#10. Convert a string to lowercase.
j = "HELLO"
print(j.upper())

#11. Capitalize the first letter.
k = "world"
print(k.capitalize())

#12. Convert every word to title case.
l = "this is a book"
print(l.title())

#13. Remove leading spaces.
m = "   The sky is clear  "
print(m.lstrip()) # left space

#.14 Remove trailing spaces.
n = "The dog is barking   "
print(n.rstrip())
 
 #15. Remove spaces from both sides.
o = "   Birds    "
print(o)

#16. Replace one character with another.
p = "apple"
print(p.replace("a", "g"))

#17. Replace a word in a string.
q = ("This is a laptop")
print(q.replace("This", "That"))

#18. Concatenate two strings.
first = "Hello"
second = "World"
result = first + " " + second
# result = f"{first} {second}"
print(result)

#19. Repeat a string 5 times.
s = "Light"
print(s * 5)
# for i in range(1, 6):
#     print(s)

#20. Print every character with its index.
string= "Python"
for str in range(len(string)):
    print(f"index: {str} Character: {string[str]}")

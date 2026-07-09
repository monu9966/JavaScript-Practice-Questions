#1. Find the length of a string.
n = input("Enter a string:")

print(len(n))

#2. Check if a string is empty.
if n == "":
    print("String is empty")
else:
    print("String is not empty")

#3. Check if a string has exactly 5 characters.
if len(n) == 5:
    print("The string has exactly 5 characters.") 
else:
    print("The string does not have exactly 5 characters.")

#4. Check if the string length is even or odd.
if len(n) % 2 == 0:
    print("Even")
else:
    print("Odd")

#5. Check if the string has more than 10 characters.
if len(n) >= 10:
    print("String has more than 10 characters")
else:
    print("String dont have more than 10 characters")

#6. Print the last index of a string.
last_index = len(n) -1
print("last index:", last_index)

#7. Print the first half of a string.
half = len(n) // 2
print("First half Character:",n[:half])

#8. Print the second half of a string.
print("First half Character:",n[half:])

#9. Print the middle character of a string.
middle = len(n) // 2
print("middle character",n[middle])

#10. Check whether two strings have the same length.
str1 = "Dog"
str2 = "cat"

if len(str1) == len(str2):
    print("Both string have same length")
else:
    print("Both string do not  have same length")


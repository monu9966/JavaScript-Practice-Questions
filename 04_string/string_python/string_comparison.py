# Part 2: String Comparison (21–40)

# 21. Compare two strings
str1 = input("Enter a first string: ")
str2 = input("Enter a second string: ")

print(str1 == str2)

#22. Check if two strings are equal.
if str1 == str2:
    print("Strings are equal")
else:
    print("Strings are not equal")

#23. Check if two strings are equal (ignore case).
if str1.lower() == str2.lower():
    print("Strings are equal")
else:
    print("Strings are not equal")
    
#24. Check if a string starts with a given character.
text = input("Enter a string: ")
ch = input("Enter a character: ")

if text.startswith(ch):
     print(f'"{text}" start with "{ch}" ')
else:
      print(f'"{text}" does not start with "{ch}" ')

#25. Check if a string ends with a given character.
if text.endswith(ch):
     print(f'"{text}" ends with "{ch}" ')
else:
     print(f'"{text}" does not ends with "{ch}" ')


#26. Check if a string starts with a given word.
text = input("Enter a string:")
word = input("Enter the word:")

if (text.startswith(word)):
     print(f' "{text}" starts with "{word}" ')
else:
     print(f' "{text}" does not starts with "{word}" ')

#27. Check if a string ends with a given word.
if (text.endswith(word)):
     print(f'"{text}" ends with "{word}"')
else:
          print(f'"{text}" does not ends with "{word}"')
       
#28. Check if a substring exists.
text = input("Enter a string:")
substring = input("Enter a substring:")

if substring in text:
    print(f'"{substring}" exists in the string.')
else:
    print(f'"{substring}" does not exists in the string.')
 
#29. Check if a character exists.
text = input("Enter a string:")
char = input("Enter a char:")
if char in text:
    print(f'"{char}" exists in the string.')
else:
    print(f'"{char}" exists in the string.')

#30. Count how many times a character appears.
text = input("Enter a string:")
cha = input("Enter a character:")
count = 0
for char in text:
    if char == cha:
        count = count + 1

print(count)
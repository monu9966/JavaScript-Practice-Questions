#1. Check if a number is positive, negative, or zero.
n = 11
if n > 0:
    print(f"{n} is Positive")
elif n < 0:
    print(f"{n} is Negative")
else:
    print(f"{n} is Zero")

#2. Check if a number is even or odd.
n = 12
if n % 2 == 0:
    print(f"{n} is Even")
else:
    print(f"{n} is Odd")

#3. Find the maximum of two numbers.
a = 100
b = 15
if a >= b:
    print(f"{a} is greater")
else:
    print(f"{b} is greater")

#4. Find the maximum of three numbers.
x = 1
y = 20
z = 3
if x >= y and x >= z:
    print(f"{x} is greater")
elif y >= x and y >= z:
    print(f"{y} is greater")
else:
    print(f"{z} is greater")

#5. Check if a number is divisible by 5 and 11.
c = 110
if c % 5 == 0 and c % 11 == 0:
    print(f"{c} is divisible by both 5 and 11.")
else:
    print(f"{c} is not divisible by both 5 and 11.")

#6. Check if a character is an alphabet or not. 
# ch = input("Enter a character: ")
ch = "A"
if (ch >= "A" and ch <= "Z") or (ch >= "a" and ch <= "z"):
    print(f"{ch} is an alphabet")
else:
    print(f"{ch} is not an alphabet")

#7. Check if a character is a vowel or consonant.
cha = "d"
if (cha == "a" or cha == "e" or cha == "i" or cha == "o" or cha == "u" or cha == "A" or cha == "E" or cha == "I" or cha == "O" or cha == "U"):
    print(f"{cha} is a vowel")
else:
    print(f"{cha} is a constant")

#8 Check if a character is an uppercase or lowercase alphabet.
char = "A"
if (char >= "A" and char <= "Z"):
    print(f"{char} is a uppercase alphabet")
else:
    print(f"{char} is a lowercase alphabet")

#9 Check if a year is a leap year.
year = 1928
if year % 4 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

#10. Check if a student is eligible to vote (age ≥ 18).
student = 8
if student >= 18:
    print("This student is a eligible to vote")
else:
    print("This student is not a eligible to vote")

#11. Find the minimum of two numbers.
num1 = 111
num2 = 21
if num1 <= num2:
    print(f"{num1} is minimum number")
else:
    print(f"{num2} is minimum number")

#12. Find the minimum of three numbers.
n1 = 11
n2 = 2
n3 = 3
if (n1 <= n2 and n1 <= n3):
    print(f"{n1} is minimum number")
elif (n2 <= n1 and n2 <= n3):
    print(f"{n2} is minimum number")
else:
    print(f"{n3} is minimum number")

#13. Calculate the absolute value of a number.
numb = -1
if numb < 0:
    print(f"Absolute value =  {-numb}")
else:
    print(f"Absolute value = {numb}")

#14. Determine if a number is a multiple of 3.
number = 11
if number % 3 == 0:
    print(f"{number} is a multiple of 3")
else:
    print(f"{number} is not  a multiple of 3")

#15. Check if a given number is between 10 and 50.
number1 = 10
if number1 >= 10 and number1 <= 50:
    print(f"{number1} Number is a between 10 and 50")
else:
    print(f"{number1} Number is not a between 10 and 50")
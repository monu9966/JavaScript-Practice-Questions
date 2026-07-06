#1. Print Numbers from 1 to 10
i = 1
while i <= 10:
    print(i)
    i += 1

#2. Print Numbers from 10 to 1
i = 10 
while i >= 1:
    print(i)
    i -= 1

#3. Print Even Numbers from 2 to 20
i = 2
while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1

#4. Print Odd Numbers from 1 to 19
i = 1
while i <= 19:
    if i % 2 != 0:
        print(i)
    i += 1

#5. Print the Multiplication Table of 8
i = 1
n = 8
while i <= 10:
    print(f"{n} x {i} = {n * i}")
    i += 1

#6. Find the Sum of Numbers from 1 to 10
sum = 0
i = 1
while i <= 10:
    sum = sum + i
    i += 1
print(sum)

#7. Count from 1 to N
i = 1
num = 10
while i <= num:
    print(i)
    i += 1

#8. Print Squares of Numbers from 1 to 10
i = 1
while i <= 10:
    print(i ** 2)
    i += 1

#9. Print All Numbers Divisible by 4 from 1 to 40
i = 1
while i <= 40:
    if i % 4 == 0:
        print(i)
    i += 1

#10. Count Down from N to 1
n = 10

while n >= 1:
    print(n)
    n -= 1
    
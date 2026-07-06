#1. Print Numbers from 1 to 10
for i in range(1, 11):
    print(i)

#2. Print Numbers from 10 to 1
for i in range(10, 0, -1):
    print(i)

#3. Print Even Numbers from 2 to 20
for i in range(2, 21):
    if i % 2 == 0:
        print(i)

#4. Print Odd Numbers from 1 to 19
for i in range(1, 20):
    if i % 2 != 0:
        print(i)

#5. Print the Multiplication Table of 8
n = 8
for i in range(1, 11):
    print(f"{n} x {i} = {8 * i}")

#6. Find the Sum of Numbers from 1 to 10
sum = 0
for i in range(1, 11):
    sum = sum + i

print(sum)

#7. Count from 1 to N
num = 10
for i in range(1, num+1):
    print(i)

#8. Print Squares of Numbers from 1 to 10
for i in range(1, 11):
    print(i ** 2)


#9. Print All Numbers Divisible by 4 from 1 to 40
for i in range(1, 41):
    if i % 4 == 0:
        print(i)

#10. Count Down from N to 1
m = 10
for i in range(m, 0, -1):
    print(i)
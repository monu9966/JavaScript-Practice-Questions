arr = [10, 5,2,1]
 
amount = 36
result = []

for i in arr:
    while amount >= i:
        result.append(i)
        amount = amount - i

print("Coins used:", result)
print("Total coins:", len(result))

# Assign Cookies
greed = [1,3,10]
cookies = [1,2,3]

i = 0
j = 0

count = 0
while i < len(greed) and j < len(cookies):
    if greed[i] <= cookies[j]:
        count += 1
        i += 1
        j += 1
    else:
        j += 1
    
print(count)

# Largest Number
arr = [1,4,2,3]
arr.sort(reverse=True)

num = ''.join(map(str, arr))
print(num) 


# Can Place Flowers
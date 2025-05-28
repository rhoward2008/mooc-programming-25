# Write your solution here
limit = int(input("Limit:"))
result = 0
i = 1

while result < limit:
    result = result + i
    i += 1
    #print(f'Result: {result}, i: {i}')

print(result)

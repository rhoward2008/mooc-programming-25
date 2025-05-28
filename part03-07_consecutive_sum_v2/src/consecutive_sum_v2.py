# Write your solution here
# Write your solution here
limit = int(input("Limit:"))
result = 0
i = 1
text = "The consecutive sum: 1 "

while result < limit:
    result = result + i
    i += 1
    if result < limit:
        text += f"+ {i} "

text += f" = {result}"

#print(result)
print(text)

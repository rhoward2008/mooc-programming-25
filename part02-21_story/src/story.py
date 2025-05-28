# Write your solution here

story = []

while True:
    word = input("Please enter a word:")

    if word == "end":
        break

    if [word] == story[-1:]:
        break
    else:
        story.append(word)

for i in story:
    print(i,"", end="")
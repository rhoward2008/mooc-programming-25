# Write your solution here

attempts = 0

while True:
    guess = input("PIN:")
    attempts += 1

    if guess == "4321":
        break
    else:
        print("Wrong")


if attempts == 1:
    print("Correct! It only took you one single attempt!")
else:
    print(f'Correct! It took you {attempts} attempts')
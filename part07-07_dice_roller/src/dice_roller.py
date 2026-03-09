import random

def roll(die: str) -> int:
    die_a = [3,3,3,3,3,6]
    die_b = [2,2,2,5,5,5]
    die_c = [1,4,4,4,4,4]

    
    if die == 'A':
        return random.choice(die_a)
    elif die == 'B':
        return random.choice(die_b)
    elif die == 'C':
        return random.choice(die_c)
    else:
        return None

def play(die1: str, die2: str, times:int) -> int:
    die1_wins = 0
    die2_wins = 0
    ties = 0

    for _ in range(times):
        roll1 = roll(die1)
        roll2 = roll(die2)
        if roll1 > roll2:
            die1_wins += 1
        elif roll2 > roll1:
            die2_wins += 1
        elif roll1 == roll2:
            ties += 1
    
    return die1_wins,die2_wins,ties

if __name__ == '__main__':
    
    for i in range(20):
        print(roll("A"), " ", end="")
    print()
    for i in range(20):
        print(roll("B"), " ", end="")
    print()
    for i in range(20):
        print(roll("C"), " ", end="")
    print()
    
    result = play("A", "C", 1000)
    print(result)
    result = play("B", "B", 1000)
    print(result)
    
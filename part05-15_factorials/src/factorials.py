# Write your solution here

def calc(num: int) -> int:
    fact = 1
    for i in range(1,num+1):
        fact *=i

    return fact

def factorials(n: int):
    facts = {}
    for i in range(1,n+1):
        facts[i] = calc(i)
    
    return facts




if __name__ == "__main__":
    k = factorials(5)
    print(k)
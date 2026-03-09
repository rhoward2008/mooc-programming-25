import math

def hypotenuse(leg1: float, leg2:float) -> float:
    return math.sqrt(leg1**2 + leg2**2)

if __name__ == '__main__':
    print(hypotenuse(3,4))
    print(hypotenuse(5,12))
    print(hypotenuse(1,1))

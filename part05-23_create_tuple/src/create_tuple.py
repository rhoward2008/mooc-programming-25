# Write your solution here
def create_tuple(x: int, y: int, z: int) -> tuple:
    sorted_list = sorted([x,y,z])
    return sorted_list[0], sorted_list[2], x+y+z 

if __name__ == '__main__':
    print(create_tuple(5,3,-1))
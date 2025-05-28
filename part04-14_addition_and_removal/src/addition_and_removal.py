# Write your solution here
mylist = []
print(f'The list is now {mylist}')

while True:
    choice = input('a(d)d, (r)emove or e(x)it: ')

    if choice == 'x':
        print('Bye!')
        break
    
    if choice == 'd':
        if mylist:
            mylist.append(mylist[-1]+1)
        else:
            mylist.append(1)
 
    if choice == 'r':
        if mylist:
            mylist.pop()
    
    if choice not in ['x','d','r']:
        print("Invalid choice")
    
    print(f'The list is now {mylist}')
    


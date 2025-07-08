# Write your solution here

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


count = int(input('Layers:'))

alphabet = alphabet[0:count]

#length = 2*count -1 

#This is the middle line
result = [alphabet[1::][::-1] + alphabet]

#print(f'length: {length}')
#print(f'lettters: {alphabet}')
#print(f'middle line: {result}')

for i in range(0,count-1):
    #print(f'i: {i}, i+1 = {i+1}')
    new_line = result[0].replace(alphabet[i],alphabet[i+1])
    result = [new_line] + result[:] + [new_line]
    #print(new_line)

#Now print the result from the list result[]
for line in result:
    print(line)
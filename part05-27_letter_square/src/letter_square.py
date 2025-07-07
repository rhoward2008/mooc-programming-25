# Write your solution here

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


count = int(input('Layers:'))

alphabet = alphabet[0:count]

length = 2*count -1 


word = 'A'

for i in range(2,count+1):
    #print(i-1)
    word = alphabet[i-1] + word + alphabet[i-1]

matrix = [word]

for i in
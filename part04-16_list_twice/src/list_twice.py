# Write your solution here
list_items = []
list_sorted = []

while True:
    item = int(input('New item: '))

    if item == 0:
        print('Bye!')
        break

    list_items.append(item)
    list_sorted.append(item)
    list_sorted.sort()

    print(f'The list now: {list_items}')
    print(f'The list in order: {list_sorted}')

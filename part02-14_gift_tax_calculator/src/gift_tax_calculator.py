# Write your solution here
gift = float(input("Value of gift"))

tax = 0

if gift < 5000:
    pass
elif gift >= 5000 and gift < 25000:
    tax = 100 + .08 * (gift - 5000)
elif gift >= 25000 and gift < 55000:
    tax = 1700 + .1 * (gift - 25000)
elif gift >= 55000 and gift < 200000:
    tax = 4700 + .12 * (gift - 55000)
elif gift >= 200000 and gift < 1000000:
    tax = 22100 + .15 * (gift - 200000)
elif gift >= 1000000:
    tax = 142100 + .17 * (gift - 1000000)


if tax == 0:
    print('No tax!')
else:
    print(f'Amount of tax: {tax} euros')
from random import randrange

a = randrange(-1, 37)
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]

abc = []
bcd = []
efg = []
if 0 <= a <= 10:
    if a % 2 == 0:
        abc = ['black']
        bcd = ['even']
        efg = ['1 to 18']
    else:
        abc = ['red']
        bcd = ['odd']
        efg = ['1 to 18']
elif 10 <= a <= 18:
    if a % 2 == 0:
        abc = ['red']
        bcd = ['even']
        efg = ['1 to 18']
    else:
        abc = ['black']
        bcd = ['odd']
        efg = ['1 to 18']
elif 18 < a <= 28:
    if a % 2 == 0:
        abc = ['black']
        bcd = ['even']
        efg = ['19 to 36']
    else:
        abc = ['red']
        bcd = ['odd']
        efg = ['19 to 36']
elif 28 < a < 37:
    if a % 2 == 0:
        abc = ['red']
        bcd = ['even']
        efg = ['19 to 36']
    else:
        abc = ['black']
        bcd = ['odd']
        efg = ['19 to 36']
print(f'''
the spin is result in {a}
pay {a}
pay {abc[0]}
pay {bcd[0]}
pay {efg[0]}
     ''')
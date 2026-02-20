a=[3,2,0,5]
col=len(a)
row=max(a)
for i in range(row):
    for j in a:
        if row-j<=i:
            print('*    ',end='')
        else:
            print('       ',end='')
            print()   

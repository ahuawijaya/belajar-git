i=1
while i<11:
    print(i)
    i=i+1

#flag=1
#while(flag):print('Python')
#print('Good bye')

i=2
while(i<30):
    j=2
    while (j<=(i/j)):
        if not(i%j): break
        j=j+1
    if (j>i/j): print(i,'adalah bilangan prima')
    i=i+1

import random
for i in range (10):
    a=random.randint(1,4)
    b=random.randint(1,100)
    C=random.randint(1,100)
    if a == 1:
        print(str(i+1)+'.'+str(b)+'+'+str(c))
    elif a == 2:
        c=b+ random.randint(1,100)
        print(str(i+1)+'.'+str(c)+'+'+str(b))
    elif a == 3:
        print(str(i+1)+'.'+str(random.randint(0,10))+'x'+str(random.randint(0,10)))
    elif a==4:
        c=random.randint(1,10)
        b=random.randint(1,10)*c
        print(str(i+1)+','+str(b)+'/'+str(c))

    

num=int(input('masukan sebuah angka:'))
if num%2 == 0:
    print('{0}is even number'.format(num))
else:
    print('{0} is Odd number'.format(num))

num=12

for i in range(1,11):
    print(num,'x',i,'=',num+1)


num= 7
factorial=1

if num < 0:
    print('What are u doing')
elif num == 0:
    print('The factorial of 0 is 1')
else:
   for i in range(1,num+1):
       factorial=factorial * i
       print('The factorial of',num,'is',factorial)

num=16
if num < 0:
    print('enter a positive number')
else:
    sum=0
    while(num>0):
        sum+=num
        num-=1
    print('The sum is',sum)

date=input('Enter the date:')
dd,mm,yy= date.split('/')
dd=int(dd)
mm=int(mm)
yy=int(yy)
if(mm == 1 or mm == 3 or mm == 5 or mm==7 or mm==8 or mm == 10 or mm == 12):
    max1=31
elif(mm == 4 or mm == 6 or mm == 9 or mm == 11):
    max1=30
elif(yy%4==0 and yy%100!=0 or yy%400== 0):
    max1=29
else:
    max1=28
if(mm<1 or mm>12):
    print('date is invalid')
elif(dd==max1 and mm!=12):
    dd=1
    mm=mm+1
    print('The incremented date is:',dd,mm,yy)
elif(dd==31 and mm == 12):
    dd=1
    mm=1
    yy=yy+1
    print('The incremented date is:',dd,mm,yy)
else:
    dd=dd+1
    print('The incremented date is:',dd,mm,yy)

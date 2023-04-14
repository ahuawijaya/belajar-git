year=2000
if(year%4)==0:
    if(year%100)==0:
        if(year%400)==0:
            print('{0} is a leap year'.format(year))
        else:
            print('{0} is not a leap year'.format(year))
    else:
        print('{0} is a leap year'.format(year))
else:
    print('{0} is not a leap year'.format(year))

nterms=10
n1=0
n2=0
count=0

if nterms<=0:
    print('Please enter a positive integer')
elif nterms == 1:
    print('Fibonacci sequence upto',nterms,':')
    print(n1)
else:
    print('Fibonacci sequence upto',nterms,':')
    while count<nterms:
        print(n1,end=',')
        nth = n1 + n2
        n1=n2
        n2=nth
        count+=1

def recur_fibo(n):
    print('Fibonacci sequence')
    if n<=1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))

nterms=10

if nterms<=0:
    print('Please enter a positive integer')
else:
    print('Fibonacci sequence')
    for i in range(nterms):
        print(recur_fibo(i))

def add(x,y):
    return x + y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y

print('Pilih operasi:')
print('1)Add')
print('2)Subtract')
print('3)Multiply')
print('4)Divide')

choice=int(input('Pilih nomor yang anda inginkan'))
num1=int(input('Masukkan bilangan pertama:'))
num2=int(input('Masukkan bilangan kedua:'))
if choice == 1:
    print(num1,'+',num2,'=',add(num1,num2))
elif choice == 2:
    print(num1,'-',num2,'=',subtract(num1,num2))
elif choice == 3:
    print(num1,'*',num2,'=',multiply(num1,num2))
elif choice == 4:
    print(num1,'/',num2,'=',divide(num1,num2))
else:
    print('salah input')


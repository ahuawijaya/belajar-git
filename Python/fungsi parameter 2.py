print('Fungsi yang menjumlahkan 2 integer')
def f(a,b):
    f=a+b
    print(f)
a=int(input('a='))
b=int(input('b='))
f(a,b)

print('Fungsi yang menukar isi 2 buah variabel string')
def v(a,b):
    c=a
    d=b
    a=d
    b=c
    print('a=',a,'dan','b=',b)
a=int(input('Masukkan a='))
b=int(input('Masukkan b='))
v(a,b)

print('Fungsi yang mengembalikan nilai KPK dari 2 bilangan')
def g(a,b):
    k=a*b
    n=1
    sw=0
    while n<=k:
        if sw==0:
            sisa1=n%a
            sisa2=n%b
            if(sisa1==0) and (sisa2==0):
                print('KPK dari',a,'dan',b,'=',n)
                sw=1
            else:
                    n=n+1
        else:
                print('------selesai------')
                n=k+1
a=int(input('Masukkan a='))
b=int(input('Masukkan b='))
g(a,b)

print('Fungsi yang mengembalikan jumlah huruf vokal dari suatu kalimat')
def h(x):
    m1=0
    m2=0
    m3=0
    m4=0
    m5=0
    m6=0
    for i in (x):
        if(i=='a'):
            m1=m1+1
        if(i=='i'):
            m2=m2+1
        if(i=='u'):
            m3=m3+1
        if(i=='e'):
            m4=m4+1
        if(i=='o'):
            m5=m5+1
        else:
            m6=0
            print('Jumlah huruf vokalnya ada:',m1+m2+m3+m4+m5+m6)
x=str(input('Masukkan kalimat:'))
h(x)

bil=int(input('Input bilangan :'))
for i in range(1,bil+1):
    for j in range(1,bil+1):
        if i==j:
            print(i,end='  ')
        else:
            print(end='   ')
    print()
    
def prompt():
    print('Please enter an integer value:',end='')
print('This program adds together two integers.')
prompt()
value1=int(input())
prompt()
value2=int(input())
sum=value1 + value2
print(value1,'+',value2,'=',sum)

for i in range(1,11):
    print(i)

def count_to_10():
    for i in range(1,11):
        print(i)
print('Going to count to ten. . .')
count_to_10()
print('Going to count to ten again. . .')
count_to_10()
        
def count_to_n(n):
    for i in range(1,n+1):
        print(i)
print('Going to count to ten. . .')
count_to_n(10)
print('Going to count to five. . .')
count_to_n(5)

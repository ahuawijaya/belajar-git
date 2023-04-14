bil1=int(input('1Masukkan bilangan pertama:'))
bil2=int(input('Masukkan bilangan kedua:'))

jumlah=bil1+bil2

print('Jumlah',bil1,'+',bil2,'=',jumlah)

num=int(input('Masukkan bilangan:'))

if num > 1:
    for i in range(2,num):
        if (num%i)==0:
            print(num,'bukan bilangan prima')
            print(i,'kali',i,'=',num)
            break
        else:
            print(num,'adalah bilangan prima')
else:
    print(num,'bukan bilangan prima')

def print_faktor(x):
    print('Faktor dari',x,'adalah')
    for i in range(1,x+1):
        if x % 1 == 0:
            print(i)

num=int(input('Masukkan bilangan:'))
print_faktor(num)

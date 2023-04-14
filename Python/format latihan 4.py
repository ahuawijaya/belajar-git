def add(x,y):
    return x + y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y

print('Pilih operasi:')
print('1)Penjumlahan')
print('2)Pengurangan')
print('3)Perkalian')
print('4)Pembagian')

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

lower=200
upper=300
print('Bilangan prima antara',lower,'and',upper,':')
for num in range(lower,upper + 1):
    if num == 1:
        for i in range (2,num):
            if num%i == 0:
                break
            else:
                print(num)

def kalkulator():
    def tambah():
        print('1.Penjumlahan')
        a=input('Masukkan nilai x:')
        b=input('Masukkan nilai y:')
        c=a+b
        print('x+y=',c)
        print('')
        tanya()
    def kurang():
        print('2.Pengurangan')
        a=input('Masukkan nilai x:')
        b=input('Masukkan nilai y:')
        c=a-b
        print('x-y=',c)
        print('')
        tanya()
    def perkalian():
        print('3.Perkalian')
        a=input('Masukkan nilai x:')
        b=input('Masukkan nilai y:')
        c=a*b
        print('x*y=',c)
        print('')
        tanya()
    def Pembagian():
        print('4.Pembagian')
        a=input('Masukkan nilai x:')
        b=input('Masukkan nilai y:')
        c=a/b
        print('x/y=',c)
        print('')
        tanya()
    def tanya():
        choose=str(input('Ulangi lagi?(y/t):'))
        if choose =='Y' or choose =='y':
            kalkulator()
        elif choose =='T' or choose == 't':
            print('Terima kasih telah menggunakan program ini')
        else:
            print('Maaf,input yang anda masukkan salah')
            print('Silakan masukkan y atau t')
            tanya()
print('Program Kalkulator sederhana')
print('#'*20)
print('1)Penjumlahan')
print('2)Pengurangan')
print('3)Perkalian')
print('4)Pembagian')
print('#'*20)
print('Silahkan pilih 1-4')
print('')
pil=int(input('Silahkan pilih:'))
if pil == 1:
    tambah()
elif pil == 2:
    kurang()
elif pil == 3:
    perkalian()
elif pil == 4:
    pembagian()
else:
    print('Maaf anda salah menginput')
    tanya()
    kalkulator()

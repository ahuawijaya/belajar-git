def kalkulator():
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
        
    
def tambah():
    print('1.Penjumlahan')
    a=int(input('Masukkan nilai x:'))
    b=int(input('Masukkan nilai y:'))
    c=a+b
    print('x+y=',c)
    print('')
    tanya()
def kurang():
    print('2.Pengurangan')
    a=int(input('Masukkan nilai x:'))
    b=int(input('Masukkan nilai y:'))
    c=a-b
    print('x-y=',c)
    print('')
    tanya()
def perkalian():
    print('3.Perkalian')
    a=int(input('Masukkan nilai x:'))
    b=int(input('Masukkan nilai y:'))
    c=a*b
    print('x*y=',c)
    print('')
    tanya()
def Pembagian():
    print('4.Pembagian')
    a=int(input('Masukkan nilai x:'))
    b=int(input('Masukkan nilai y:'))
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

def awal():
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

awal()

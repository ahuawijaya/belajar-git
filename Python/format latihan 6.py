def menu():
    print('--Menu------')
    print('1.Kasir')
    print('2.Kalkulator')
    print('------------')
    pilih=input('Pilih menu:')
    if pilih == '1':
        kasir()
    elif pilih == '2':
        kalkulator()
    else:
        exit
    tanya()

def kasir():
    brg=input('Masukkan nama barang:')
    harga=int(input('Masukkan harga barang:'))
    jlh=int(input('Masukkan jumlah barang:'))
    cash=int(input('Masukkan pembayaran:'))
    total=harga*jlh
    kemb=cash - total
    hu= total - cash
    if cash>total:
        print('Total kembalian anda adalah:',kemb)
    else:
        print('Hutang lu ',hu)
    tanya()

def kalkulator():
    print('--Kalkulator--')
    print('1.(+) 4.(*)')
    print('2.(-) 5.(/)')
    print('3.(%) 6.(**)')
    print('--------------')
    operasi=input('Pilih operasi:')
    a=int(input('a='))
    b=int(input('b='))
    if operasi == '1':
        print('Hasil=',a+b)
    elif operasi == '2':
        print('Hasil=',a-b)
    elif operasi == '3':
        print('hasil=',a%b)
    elif operasi == '4':
        print('Hasil=',a*b)
    elif operasi == '5':
        print('Hasil =',a/b)
    elif operasi == '6':
        print('Hasil =',a**b)
    else:
        print('Lu bisa liat angka gak?')
    tanya()

def tanya():
    tanya=input('Kembali ke menu(y/t):')
    if tanya =='y':
        menu()
    elif tanya == 't':
        exit
    else:
        print("Salah input")

def awal():
    username=input('Username:')
    password=input('Password:')
    if username == 'mahend' and password == '123456789':
        menu()
    else:
        print('Login gagal')
          

awal()

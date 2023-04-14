celsius=float(input('Tuliskan suhu dalam derajat Celcius:'))
farenheit=(celsius*1.8)+32
print('%0.2f Derajat Celcius sama dengan %0.2f derajat Farenheit'%(celsius,farenheit))
print(celsius,'Derajat Celcius sama dengan',farenheit,' derajat Farenheit')


angka=float(input('Ketik sebuah angka:'))
if angka > 0:
    print('Angka positif')
elif angka==0:
    print('Angka 0')
else:
    print('Angka Negatif')

angka1=float(input('Ketik sebuah angka:'))
if angka1%2==0:
    print(angka1,'Angka genap')
else:
    print(angka1,'Angka ganjil')

tahun=float(input('Ketik sebuah tahun:'))
if (tahun % 4)== 0:
    if(tahun % 100)==0:
        if(tahun % 400)==0:
            print(tahun,'adalah tahun kabisat')
        else:
            print(tahun,'bukan tahun kabisat')
    else:
        print(tahun,'adalah tahun kabisat')
else:
    print(tahun,'bukan tahun kabisat')

import calendar
yy=int(input('Masukkan Tahun:'))
mm=int(input('Masukkan Bulan:'))

print(calendar.month(yy,mm))

kalimat=input('Tulis sebuah kalimat:')
kata=kalimat.split()
kata.sort()
print('Berikut urutan kata kata:')
for urut in kata:
    print(urut)

tugas=float(input('Masukkan nilai tugas:'))
uts=float(input('Masukkan nilai UTS:'))
uas=float(input('Masukkan nilai UAs:'))

nilai=(0.15 * tugas)+(0.35*uts)+(0.5*uas)

if nilai > 80:
    grade='A'
elif nilai >70:
    grade='B'
elif nilai >60:
    grade='c'
elif nilai >50:
    grade='D'
else:
    grade='E'

if nilai >60:
    status='Lulus'
else:
    status='Tidak lulus'

print('Nilai Akhir: %0.2f'%nilai)
print('Grade:{}'.format(grade))
print('Status:{}'.format(status))

angka=int(input('Menampilkan tabel perkalian dari:'))
for i in range(1,11):
    print(angka,'x',i,'=',angka*1)

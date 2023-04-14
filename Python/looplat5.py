#Program 5.1
def input_data():
    print('Fungsi pertama')
    nama=input('Nama:')
    nrp=input('NRP:')

def cetak_string():
    print('Ini adalah fungsi ysng mencetak string')
    print('Silahkan masukkan data')
    input_data()


cetak_string()

#Program 5.2
def cetak_string(par1,par2):
    print('Nama mahasiswa adalah',par1)
    print('NRP mahasiswa adalah',par2)

def hitung(a,b):
    print('Hasil penjumlahan',a,'+',b,'adalah',(a+b))

#main_program
nama=input('Nama:')
nrp=input('NRP:')
cetak_string(nama,nrp)
bil1=10
bil2=12
hitung(bil1,bil2)

#Program 5.
def tambah(a,b):
    jum=a+b
    return jum
def kurang(c,d):
    kur=c-d
    return kur
bil1=int(input('Masukkan nilai A:'))
bil2=int(input('Masukkan nilai B:'))
hasil=tambah(bil1,bil2)
print('Hasil jumlah:',hasil)
print('Hasil kurang:',kurang(bil1,bil2))

#Program 5.4
def tambah_kurang(a,b):
    return[a+b,a-b]
bil1=int(input('Masukkan nilai A:'))
bil2=int(input('Masukkan nilai B:'))
[plus,minus]=tambah_kurang(bil1,bil2)
print('Hasil penjumlahan:',plus)
print('Hasil pengurangan:',minus)

#Program 5.5
def faktoria(nn):
    if nn<=1:
        return 1
    else:
        f=nn*faktoria(nn-1)
        return f
N=int(input('Masukkan integer ='))
print('Faktorial dari',N,'adalah',faktoria(N))

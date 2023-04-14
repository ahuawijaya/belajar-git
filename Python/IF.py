varAngka1 = 123
varAngka2 = 0
if varAngka1 :
    print('Nilai : TRUE')
    print('varAngka1')

if varAngka2 :
    print('Nilai : TRUE')
    print('varAngka2')

varAngka = 123

if varAngka==200:
    print('Nilai : True')
    print('varAngka')

elif varAngka==123:
    print('Nilai : True')
    print('varAngka')

else :
    print('Nilai : False')
    print('varAngka')

varAngka = 89
if varAngka<100:
     print('Nilai : True')
     print('varAngka')
if varAngka<80:
    print('Nilai  : A')
elif varAngka<60:
    print('Nilai  : B')
elif varAngka<40:
    print('Nilai  : C')
elif varAngka<20:
    print('Nilai  : D')
else    :
    print('Nilai : E')
    print('Nilai : False')
    print('varAngka')
  
print('Progam Menghitung umur')
print('ketik nama anda disini')
print('='*25)
tgl=0
bln=0
thn=0
print('='*25)
thn=int(input('Masukkan tahun lahir anda = '))
bln=int(input('Masukkan bulan lahir anda = '))
tgl=int(input('Masukkan tanggal lahir anda = '))
print('='*25)
tgls=0
blns=0
thns=0
thns=int(input('Masukkan tahun sekarang anda = '))
blns=int(input('Masukkan bulan sekarang anda = '))
tgls=int(input('Masukkan tanggal sekarang anda = '))
print('='*25)
umur=thns-thn
if(thns>thn and blns>=bln and tgls>=tgl):
   print('Umur anda saat ini adalah = ',umur,'tahun')
elif(thns>thn and blns==bln and tgls<tgl):
    print('Umur anda saat ini adalah =',umur-1,'tahun')
elif(thns>thn and blns<bln):
    print('Umur anda saat ini adalah =',umur-1,'tahun')
else :
    print('Sadar bang')

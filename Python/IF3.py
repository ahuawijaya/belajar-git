jack=int(input('Masukkan nilai anda = '))
nama1=str(input('Masukkan nama anda = '))
course=str(input('Masukkan course anda(S.engineering,R.engineering) = '))

print('Id = 1')
print('Name :',nama1)
print('Course :',course)
print('Marks :',jack)
print('Grade :')
if 90<=jack<=100 :
    print('A')
elif 80<=jack<=89 :
    print('B')
elif 70<=jack<=79 :
    print('C')
elif 60<=jack<=60 :
    print('D')
else:
    print('E')

    
print('Status :')   
if jack>=75:
   print('Complete')
else :
    print('Failed')

print('='*40)
nama=str(input('Masukkan nama anda = '))
jadwal=str(input('Masukkan jadwal sip anda = '))
print('Nama :',nama)
print('Jadwal masuk :',jadwal)
if jadwal=='sip1' :
           print('Jam masuk 06:00')
elif jadwal=='sip2' :
           print('Jam masuk 10:00')
elif jadwal=='sip3' :
           print('Jam masuk 14:00')
elif jadwal=='sip4' :
           print('Jam masuk 18:00')
else :
    print('nipu')
if jadwal=='sip1' :
           print('Jam pulang 10:00')
elif jadwal=='sip2' :
           print('Jam pulang 14:00')
elif jadwal=='sip3' :
           print('Jam pulang 18:00')
elif jadwal=='sip4' :
           print('Jam pulang 22:00')
else :
    print('nipu')
print('='*40)
kode=str(input('Masukkan kode anda(eko,eks,bis) : '))
waktu=str(input('Masukkan waktu berangkat anda (ml,sg,pg): '))
ekon=250000
bisn=300000
eksn=350000
print('Tiket kereta api indonesia')
print('Kode tiket : ',kode)
print('waktu berangkat :',waktu)
print('Kelas:')
if kode=='eko' :
    print('Ekonomi',ekon)
elif kode=='bis' :
   print('Bisnis',bisn)
elif kode=='eks' :
    print('Eksekutif',eksn)
print('waktu berangkat')
if waktu=='ml' :
    print('malam')
elif waktu=='sg' :
   print('siang')
elif waktu=='pg' :
    print('pagi')
else :
    print('nipu')
print('='*40)
no=str(input('no.='))
nama=str(input('nama ='))
tglpinjam=int(input('tanggal pinjam ='))
tglkembali=int(input('tanggal kembali ='))
lamapinjam=tglkembali-tglpinjam
print('Lama pinjam : ',lamapinjam)
if 20>=lamapinjam>=14 :
   print('Besar denda :',(lamapinjam - 14) * 500)
elif 29>=lamapinjam>=21 :
    print('Besar denda :',((lamapinjam - 20)*1000)+(20 - 14)* 500)
elif lamapinjam>30 :
    print('Besar denda :',((lamapinjam - 30) * 1500)+((lamapinjam - 20)*1000)+(20 - 14)* 500) 
else :
    print('bebas denda')


           
           



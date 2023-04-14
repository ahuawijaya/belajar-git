tempat2=[]
nama=[]
print('Pemesanan Tiket Online')
tempat=str(input('Pilih tempat duduk:'))
pesa=str(input('Ingin memesan tiket tambahan?(y/t): '))
while pesa == 'y':
   te=str(input('Pilih tempat duduk:'))
   tempat2.append(te)
   pesa=str(input('Ingin memesan tiket tambahan?(y/t): '))

jumlah=int(input('Ketik jumlah pesanan anda:'))
for j in range (jumlah):
    print('Nama pemesan ',j+1)
    nam=str(input('='))
    nama.append(nam)
print('Pemesanan tiket online:')
b=0
for a,n in zip(tempat2,nama):
    b=b+1
    print(b,format(n),format(a))

total=jumlah*25000
print('total',total)
bayar=int(input('Bayar='))
kembalian=bayar-total
print('kembalian',kembalian)

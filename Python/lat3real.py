name=[]
tempat=[]
hitung=0
while(True):
    hitung+=1
    s=str(input('Pilih tempat duduk='))
    tempat.append(s)
    jawab=str(input('Apakah anda ingin memesan tiket tambahan? y/n='))
    if jawab=='n':
        break
for h in range(hitung):
    ns=str(input('Isilah nama pemesan:'))
    name.append(ns)
    
print('Total='+str(hitung))
print('\n')
print('Pemesanan Tiket Online:')
n=0
for s,a in zip(name,tempat):
    n=1
    print(n,'{}',format(s),'{}',format(a))

jumlah=hitung
total=jumlah*25000
print('total',total)
bayar=int(input('Bayar='))
kembalian=bayar-total
print('kembalian',kembalian)


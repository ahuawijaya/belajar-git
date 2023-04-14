ayam=[]
ikan=[]
sapi=[]
listj=[]

kode=int(input('Masukkan kode bil:'))
kasir=str(input('Kasir:'))
tanggal=input('Masukkan tanggal:')
meja=input('No meja:')
tipe=input('Masukkan tipe (regular,premium,vip):')

while(True):
    menu=str(input('Menu yang dipesan(ayam,ikan,sapi):'))
    if menu =='ayam':
        ayam.append(menu)
    elif menu=='ikan':
        ikan.append(menu)
    else:
        sapi.append(menu)
    jum=int(input('Jumlah pesanan:'))
    listj.append(jum)
    ul=str(input('Ada lagi pesanannya(y/n):'))
    if ul =='n':
        break
if tipe=='regular':
    pajak=50000
elif tipe =='premium':
    pajak=100000
else:
    pajak=150000

print('Cafe prot')
print('Jalan gayung')
print('='*30)
print('Kode:',kode)
print('Kasir:',kasir)
print('Tanggal:',tanggal)
print('No meja:')
print('Dine in')

for a in (ayam):
        print(format(a))
hay=listj[0]*50000
print(listj[0],':',hay)
for b in (ikan):
         print(format(b))
hik=listj[1]*35000
print(listj[1],':',hik)
for c in (sapi):
         print(format(c))
hsa=listj[2]*75000
print(listj[2],':',hsa)

print('Pajak:',pajak)
total=hay+hik+hsa+pajak
print('Total :',total)
bayar=int(input('Bayar:'))
kembalian=bayar-total
print('Kembalian:',kembalian)





            
    
    

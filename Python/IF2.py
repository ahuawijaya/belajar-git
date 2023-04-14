kode=str(input('Masukkan kode kamar anda(eco,exc,lux) = '))
lama=int(input('Masukkan berapa hari anda menginap = '))
econ=300000
excn=550000
luxn=800000

print('Output:')
print('Hotel Kembang Mawar')
print('='*25)
print('Pesanan Pelanggan')
if kode=='eco' :
    print('Kode Type Kamar : eco')
    print('Lama menginap :',lama)
    print('Total tagihan:',econ*lama)
elif kode=='exc' :
    print('Kode Type Kamar : exc')
    print('Lama menginap :',lama)
    print('Total tagihan:',excn*lama)
elif kode=='lux' :
    print('Kode Type Kamar : eco')
    print('Lama menginap :',lama)
    print('Total tagihan:',luxn*lama)
else:
 print('nipu')

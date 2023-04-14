total=int(input('Total belanja : RP'))
bayar=total

if total > 100000:
    print('Kamu mendapat bonus minuman dingin')
    print('dan diskon 5%')
    diskon=total * 5/100
    bayar= total - diskon

print('Total yang harus dibayar:Rp%s'%bayar)
print('Terima kasih telah berbelanja')
print('Datang lagi ya')

umur=int(input('Berapa umurmu:'))

if umur >= 18 :
    print('Kamu boleh membuat sim:')
else:
    print('Tunggu sampai kamu 18 tahun atau lebih')


nilai=int(input('Input nilaimu:'))

if nilai >= 90:
    print('grade=A')
elif nilai >= 80:
    print('grade=B+')
elif nilai >= 70:
    print('grade=B')
elif nilai >= 60:
    print('grade=C+')
elif nilai >= 50:
    print('grade=C')
elif nilai >= 40:
    print('grade=D')
else:
    print('grade=E')
    
    

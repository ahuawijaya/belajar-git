jumlah_barang=24
jumlah_barang_dalam_lusin =jumlah_barang/12
print(jumlah_barang,'=',jumlah_barang_dalam_lusin,'lusin')

if jumlah_barang_dalam_lusin % 1 == 0:
    jumlah_barang_dalam_lusin=int(jumlah_barang_dalam_lusin)

print({jumlah_barang},'=',{jumlah_barang_dalam_lusin},'lusin')
    
jumlah_barang=60
jumlah_barang_dalam_kodi =jumlah_barang/20
print(jumlah_barang,'=',jumlah_barang_dalam_kodi,'kodi')

if jumlah_barang_dalam_kodi % 1 == 0:
    jumlah_barang_dalam_kodi=int(jumlah_barang_dalam_kodi)

print({jumlah_barang},'=',{jumlah_barang_dalam_kodi},'kodi')

jumlah_barang=216
jumlah_barang_dalam_gross =jumlah_barang/144
print(jumlah_barang,'=',jumlah_barang_dalam_gross,'gross')

if jumlah_barang_dalam_gross % 1 == 0:
    jumlah_barang_dalam_gross=int(jumlah_barang_dalam_gross)

print({jumlah_barang},'=',{jumlah_barang_dalam_gross},'gross')

jumlah_barang=int(input('Masukkan jumlah barang:'))

satuan_lusin=round(jumlah_barang/12,2)
satuan_kodi=round(jumlah_barang/20,2)
satuan_gross=round(jumlah_barang/144,2)

if satuan_lusin % 1 == 0:
    satuan_lusin = int(satuan_lusin)
if satuan_kodi % 1 == 0:
    satuan_kodi = int(satuan_kodi)
if satuan_gross % 1 == 0:
    satuan_gross = int(satuan_gross)

print({jumlah_barang},'=',{satuan_lusin},'lusin')
print({jumlah_barang},'=',{satuan_kodi},'kodi')
print({jumlah_barang},'=',{satuan_gross},'gross')

random_randint=100

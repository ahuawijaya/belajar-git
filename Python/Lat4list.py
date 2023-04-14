warna=['merah','hijau','kuning','biru','pink','ungu']
print(warna[1:5])

list_lagu=['No women','No Cry','Dear God']
playlist_favorite=['Break out','Now loading']

semua_lagu=list_lagu+playlist_favorite

print(semua_lagu)

ulangi=5
now_playing=playlist_favorite*ulangi
print(now_playing)

list_minuman=[ ['Kopi','Susu','Teh'],['Jus apel','Jus melon','Jus jeruk'],['Es Kopi','Es campur','Es teler']]
print(list_minuman[2][0])

for menu in list_minuman:
    for minuman in menu:
        print(minuman)
               

my_friends=['Anggun','Dlan','Agung','Adi','Adam']
print('Isi my_friends indeks ke-3 adalah :{}',format(my_friends[3]))
print('Semua teman: ada{} orang',format(len(my_friends)))
for friend in my_friends:
      print(friend)

buah=['jeruk','apel','mangga','duren']
buah[2]='kelapa'
buah.append('manggis')
print(buah)

buah=['jeruk','apel','mangga','duren']
buah[2]='kelapa'
buah.insert(3,'manggis')
print(buah)

deret=[1,2,3,4,5,6,7,8,9,10,11]
print('\nakses list per indeks:')
print(deret[1])
print(deret[6])
print(deret[10])

print('\nmencacah isi list:')
for x in deret:
    print(x)

print('\npanjang list:'+str(len(deret)))
print('\nbanyaknya angka 11:'+str(deret.count(11)))
print('\nmenambah elemen list dengan append:')
deret.append(15)
deret.append(16)
deret.append(17)
deret.append(18)
deret.append(19)
deret.append(20)
print(deret)



print('menambah elemen dengan insert:')
deret.insert(2,35)
deret.insert(2,36)
deret.insert(2,37)
deret.insert(2,38)
deret.insert(2,39)
deret.insert(2,40)
print(deret)

print('membuang elemen dengan pop:')
deret.pop()
deret.pop()
deret.pop()
print(deret)

print('membuang elemen dengan remove')
deret.remove(35)
deret.remove(36)
deret.remove(37)
deret.remove(38)
deret.remove(39)
deret.remove(40)
print(deret)

print('\nmenambah elemen list dengan extend')
deret2=[1,2,3,4,5]
deret.extend(deret2)

print(deret)

print('\membalik list dengan reverse')
deret.reverse()
print(deret)

print('mengurut list dengan sort')
deret.sort()
print(deret)

print('mencari nilai max dari deret')
print(max(deret))

print('mencari nilai min dari deret')
print(min(deret))

print('mencari nilai sum dari deret')
print(sum(deret))
    

ulang=10

for i in range(ulang):
    print('perulangan ke-',i)

item=['kopi','nasi','teh','jeruk']
for i in item:
    print(i)


jawab='ya'
hitung=0
while(jawab == 'ya'):
    hitung+=1
    jawab = input('Ulangi lagi tidak?:')
    print('Total perulangan :',hitung)

jawab='ya'
hitung=0
while(True):
    hitung+=1
    jawab = input('Ulangi lagi tidak?:')
    if jawab =='tidak':
        break
    print('Total perulangan :',hitung)

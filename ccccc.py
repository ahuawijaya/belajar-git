print('Berikut ini source code mengubah skala celcius menjadi farehnheit:')
celcius=int(input('Masukkan nilai celcius:'))
farenheit=float(celcius*9/5+32)
print('nilai',celcius,'dalam skala farenheit sebesar:',farenheit)

print('Progam mencari bilangan prima')
n=int(input('masukkan nilai:'))
print('Bilangan prima sampai nilai',n,'adalah:')
for x in range(2,n+1):
    if(x%2==1 or x ==2):
        print(x,'merupakan bilangan prima')

if(n<2):
    print('Eror,nilai untuk bilangan prima harus lebih besar dari 1')

r=int(input('Masukkan jari jari lingkaran:'))
l=22/7 * r * r
k=22/7 * 2 * r
print('Besar keliling:',k)
print('Besar Luas :',l)

a=int(input('Masukkan angka a:'))
b=int(input('Masukkan angka b:'))
print('Penjumlahan =',a,'+',b,'=',a+b)
print('Pengurangan =',a,'-',b,'=',a-b)
print('Perkalian =',a,'x',b,'=',a*b)
print('Pembagian =',a,'/',b,'=',a/b)

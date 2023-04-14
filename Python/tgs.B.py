kalimat=input('Tulis kalimat:')
kata=kalimat.split()
kata.sort()

print('Berikut urutan kata kata:')
for urut in kata:
    print(urut)

alas=float(input('Isi alas:'))
tinggi=float(input('Isi tinggi:'))

luas=(alas*tinggi)/2

print('Berikut ini adalah luasnya:',luas)


p=int(input('Isi panjang:'))
l=int(input('Isi lebar:'))
t=int(input('Isi tinggi:'))


L=2*((p*l)+(p*t)+(l*t))
V=p*l*t
print('Jadi balok dengan ukuran panjang:',p,'lebar:',l,'tinggi:',t,' Mempunyai luas:',L,'dan volume:',V)

      


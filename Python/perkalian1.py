x=1
y=int(input('Masukkan angka dibawah 10:'))
z=int(input('Sampai dengan:'))
for n in range (y,z+1):
        for m in range (y,11):
           print(n,'x', m,'=', m * n)
        x=x+1



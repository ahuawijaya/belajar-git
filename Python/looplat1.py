for x in range (1,3):
    for y in range (1,3):
        print(x,y,x*y)

        
banyakMhs= int(input('Banyak Mahasiswa:'))
for M in range (banyakMhs):
    print('Mahasiswa ke-',M+1)
    banyakMk=int(input('Banyak Matakuliah yang diambil:'))
    totalnilai=0
    for N in range (banyakMk):
            nilai=int(input('Input Nilai ke %d='%(N+1)))
            totalnilai=totalnilai+nilai
            rata=totalnilai/banyakMk
            print('Rata=rata :',rata)


for i in [12,16,17,24,29]:
    if i % 2==1:
        break
    print(i)
    print('selesai')

nilaiawal=int(input('Input nilai awal:'))
nilaiakhir=int(input('Input nilai akhir:'))
for i in range (nilaiawal,nilaiakhir+1):
   if i%2==0:
       print(i,'adalah bilangan genap')
   else :
        print(i,'adalah bilangan ganjil')

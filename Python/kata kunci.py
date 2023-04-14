name=[]
nilai=[]
hitung=0
while(True):
    hitung+=1
    ns=str(input('Isilah nama peserta yang ikut lomba?'))
    name.append(ns)
    s=int(input('Nilainya='))
    nilai.append(s)
    jawab=str(input('Apakah anda ingin menambah peserta lain? y/n'))
    if jawab=='n':
        break
print('Total='+str(hitung))
print('\n')
print('No.  Nama   Nilai')
print('='*30)
n=0
for s,a in zip(nilai,name):
    n=1
    print(n,'{}',format(a),'{}',format(s))
    
print('')

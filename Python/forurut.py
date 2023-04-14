listnm=[]
n=0
while(True):
    nama=str(input('Input nama siswa:'))
    listnm.append(nama)
    ulg=str(input('Lanjut input ?(y/n)'))
    if ulg =='n':
        break
    elif ulg=='':
        ulg1=str(input('Anda belum menjawabnya , input ?(y/n)'))
        if ulg1 =='n':
            break
        
daf=str(input('Tampilkan Daftar siswa di urutkan berdasarkan abjad(y/n):'))
if daf =='y':
    listnm.sort()
    for i in listnm:
        n=n+1
        print(n,format(i))
        
    

kerja=[]
hari=[]
while(True):
        nk=str(input('List kegiatan hari:'))
        hari.append(nk)         
        while(True):
                ns=str(input('Apa saja kegiatannya:'))
                kerja.append(ns)
                ulg=str(input('Ada lagi kegiatannya(y/n):'))
                if ulg=='n':
                       break
                nh=str(input('Isi list kegiatan hari lain(y/n):'))
                if nh =='n':
                        break
hub=str(input('Tampilkan daftar list kegiatan tadi(y/n):'))
if hub =='y':
    print('Daftar kegiatan dalam seminggu(Senin S/d Minggu:')
    for nk,ns in zip(kerja,hari):
        print(format(ns),format(nk))
    

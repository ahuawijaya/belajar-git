list1=[]
list2=[]
list3=[]
list4=[]
list5=[]
list6=[]
list7=[]

har=[]
hari=['senin','selasa','rabu','kamis','jumat','sabtu','minggu']
for h in hari:
        print('List kegiatan hari:',h)
        nk=h
        har.append(nk) 
        while(True):
                ns=str(input('Apa saja kegiatannya:'))
                if h =='senin':
                        list1.append(ns)
                elif h=='selasa':
                        list2.append(ns)
                elif h=='rabu':
                        
                ulg=str(input('Ada lagi kegiatannya(y/n):'))
                if ulg=='n':
                       break
    
hub=str(input('Tampilkan daftar list kegiatan tadi(y/n):'))
if hub =='y':
    print('Daftar kegiatan dalam seminggu(Senin S/d Minggu):')
    for nk,ns in zip(har,list):
        print(format(nk),format(ns))
              
              
              

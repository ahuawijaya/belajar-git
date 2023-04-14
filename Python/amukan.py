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
                    list3.append(ns)
                elif h=='kamis':
                        list4.append(ns)
                elif h=='jumat':
                        list5.append(ns)
                elif h=='sabtu':
                        list6.append(ns)
                else:
                    list7.append(ns)
                ulg=str(input('Ada lagi kegiatannya(y/n):'))
                if ulg=='n':
                       break
    
hub=str(input('Tampilkan daftar list kegiatan tadi(y/n):'))
if hub =='y':
    print('Daftar kegiatan dalam seminggu(Senin S/d Minggu):')
    print(hari[0])
    for ns in (list1):
            print(format(ns))
    print(hari[1])
    for ns in (list2):
            print(format(ns))
    print(hari[2])
    for ns in (list3):
            print(format(ns))
    print(hari[3])
    for ns in (list4):
            print(format(ns))
    print(hari[4])
    for ns in (list5):
            print(format(ns))
    print(hari[5])
    for ns in (list6):
            print(format(ns))
    print(hari[6])
    for ns in (list7):
            print(format(ns))
            


    
              


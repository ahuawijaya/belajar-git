kerja=[]
hari=['senin','selasa','rabu','kamis','jumat','sabtu','minggu']
while(True):
    for h in hari:
        print('List kegiatan hari:',h)
        ns=str(input('Apa saja kegiatannya:'))
        kerja.append(ns)
        ulg=str(input('Ada lagi kegiatannya(y/n):'))
        if ulg=='n':
            break
        
        
        
    
    

list1=[]
list2=[]
list3=[]
list4=[]
list5=[]
list6=[]
x=1

list7=[]
list8=[]
list9=[]
list10=[]
list11=[]
list12=[]
list13=[]
list14=[]
list15=[]
list16=[]
rap=['Pengetahuan','Ketrampilan','HTPS']
pelua=['Agama','PPKN','Bahasa Indonesia','Matematika','Sejarah Indonesia','Bahasa Inggris',
       'Seni budaya','PJOK','Prakarya','TIK','Matematika P','Biologi','Fisika','Kimia',
       'Bahasa Inggris','Bahasa Mandarin']
sekolah=str(input('Nama Sekolah:'))
alamat=str(input('Alamat:'))
nama=str(input('Nama siswa:'))
induk=int(input('No.Induk/NISN:'))
k=input('Kelas :')
s=input('Semester :')
print('Tahun Pelajar: 2021 - 2022')


for a in pelua:
    print(a)
    while(True):
        ns=int(input('Nilai pengetahuan:'))
        if a =='Agama':
                        list1.append(ns)
        elif a=='PPKN':
                        list2.append(ns)
        elif a=='Bahasa Indonesia':
                    list3.append(ns)
        elif a=='Matematika':
                        list4.append(ns)
        elif a=='Sejarah Indonesia':
                        list5.append(ns)
        elif a=='Bahasa Inggris':
                        list6.append(ns)
        elif a =='Seni budaya':
                        list7.append(ns)
        elif a=='PJOK':
                        list8.append(ns)
        elif a=='Prakarya':
                    list9.append(ns)
        elif a=='TIK':
                list10.append(ns)
        elif a=='Matematika P':
                        list11.append(ns)
        elif a=='Biologi':
                        list12.append(ns)
        elif a =='Fisika':
                        list13.append(ns)
        elif a=='Kimia':
                        list14.append(ns)
        elif a=='Bahasa Inggris':
                    list15.append(ns)
        else :
                list16.append(ns)
        nk=int(input('Nilai ketrampilan:'))
        if a =='Agama':
                        list1.append(nk)
        elif a=='PPKN':
                        list2.append(nk)
        elif a=='Bahasa Indonesia':
                    list3.append(nk)
        elif a=='Matematika':
                        list4.append(nk)
        elif a=='Sejarah Indonesia':
                        list5.append(nk)
        elif a=='Bahasa Inggris':
                        list6.append(nk)
        elif a =='Seni budaya':
                        list7.append(nk)
        elif a=='PJOK':
                        list8.append(nk)
        elif a=='Prakarya':
                    list9.append(nk)
        elif a=='TIK':
                list10.append(nk)
        elif a=='Matematika P':
                        list11.append(nk)
        elif a=='Biologi':
                        list12.append(nk)
        elif a =='Fisika':
                        list13.append(nk)
        elif a=='Kimia':
                        list14.append(nk)
        elif a=='Bahasa Inggris':
                    list15.append(nk)
        else :
                list16.append(nk)
        np=int(input('Nilai HTPS:'))
        if a =='Agama':
                        list1.append(np)
        elif a=='PPKN':
                        list2.append(np)
        elif a=='Bahasa Indonesia':
                    list3.append(np)
        elif a=='Matematika':
                        list4.append(np)
        elif a=='Sejarah Indonesia':
                        list5.append(np)
        elif a=='Bahasa Inggris':
                        list6.append(np)
        elif a =='Seni budaya':
                        list7.append(np)
        elif a=='PJOK':
                        list8.append(np)
        elif a=='Prakarya':
                    list9.append(np)
        elif a=='TIK':
                list10.append(np)
        elif a=='Matematika P':
                        list11.append(np)
        elif a=='Biologi':
                        list12.append(np)
        elif a =='Fisika':
                        list13.append(np)
        elif a=='Kimia':
                        list14.append(np)
        elif a=='Bahasa Inggris':
                    list15.append(np)
        else :
                list16.append(np)
        ket=(ns+nk)/2
        if 93<ket<100:
            print('Keterangan = A')
        elif 84<ket<92:
            print('Keterangan = B')
        elif 75<ket<84:
            print('Keterangan = C')
        else :
            print('Keterangan = D')
        if x==1:
            break
print('='*40)
hi=str(input('Apakah anda ingin menampilkannya?(y/n):'))
if hi =='y':
        print(pelua[0])
        for x,ns in zip(rap,list1):
                    print(x,'=',format(ns))
        print(pelua[1])
        for x,ns in zip(rap,list2):
                    print(x,'=',format(ns))
        print(pelua[2])
        for x,ns in zip(rap,list3):
                    print(x,'=',format(ns))
        print(pelua[3])
        for x,ns in zip(rap,list4):
                    print(x,'=',format(ns))
        print(pelua[4])
        for x,ns in zip(rap,list5):
                    print(x,'=',format(ns))
        print(pelua[5])
        for x,ns in zip(rap,list6):
                    print(x,'=',format(ns))
        print(pelua[6])
        for x,ns in zip(rap,list7):
                    print(x,'=',format(ns))       
        print(pelua[7])
        for x,ns in zip(rap,list8):
                    print(x,'=',format(ns))       
        print(pelua[8])
        for x,ns in zip(rap,list9):
                    print(x,'=',format(ns))
        print(pelua[9])
        for x,ns in zip(rap,list10):
                    print(x,'=',format(ns))
        print(pelua[10])
        for x,ns in zip(rap,list11):
                    print(x,'=',format(ns))
        print(pelua[11])
        for x,ns in zip(rap,list12):
                    print(x,'=',format(ns))
        print(pelua[12])
        for x,ns in zip(rap,list13):
                    print(x,'=',format(ns))
        print(pelua[13])
        for x,ns in zip(rap,list14):
                    print(x,'=',format(ns))
        print(pelua[14])
        for x,ns in zip(rap,list15):
                    print(x,'=',format(ns))
        print(pelua[15])
        for x,ns in zip(rap,list16):
                    print(x,'=',format(ns))





                  

def fungsi_total_nilai(var_harian,var_uts,var_uas):
    var_harian=int(var_harian)*0.3
    var_uts=int(var_uts)*0.3
    var_uas=int(var_uas)*0.4

    var_total=var_harian+var_uts+var_uas
    return var_total

def fungsi_percabangan(var_nilai):
    var_huruf=""
    if(var_nilai>=0 and var_nilai<20):
        var_huruf='E'
    elif (var_nilai>= 20 and var_nilai<40):
        var_huruf='D'
    elif(var_nilai >=40 and var_nilai<60):
        var_huruf='C'
    elif(var_nilai >=60 and var_nilai<80):
        var_huruf='B'
    elif(var_nilai>=80 and var_nilai<100):
        var_huruf='A'
    return var_huruf

def fungsi_perulangan():
    var_hasil_perulangan=0
    for i in range(1,3):
        print('---Nilai ke',i,'---')
        var_harian=input('Nilai Harian:')
        var_uts=input('Nilai UTS:')
        var_uas=input('Nilai UAS:')
        var_hasil_perulangan+=(int(fungsi_total_nilai(var_harian,var_uts,var_uas)))
        return var_hasil_perulangan/i
var_total=fungsi_perulangan()

print('---Total Nilai ---')
print('Total nilai yang didapat:',var_total)
print('Total Nilai Dalam Huruf:',fungsi_percabangan(var_total))

nama=[]
gaji=[]
emas=[]
zakat=[]
pertahun=[]
perbulan=[]
nisab=[]
print('+----------------------------+')
print('|Penghitung Zakat Penghasilan|')
print('+----------------------------+')
data=int(input('Masukkan banyak data:'))
print('='*25)

for i in range(data):
    a=input('Masukkan nama:')
    nama.append(a)
    b=int(input('Masukkan harga emas saat ini:'))
    emas.append(b)
    c=int(input('Masukkan penghasilan Anda per bulan:'))
    gaji.append(c)
    print('')

for i in range(data):
    d= 12 * gaji
    pertahun.append(d)
    e=0.025 * pertahun[i]
    zakat.append(e)
    f=85* emas[i]
    nisab.append(f)
    g=zakat[i]/12
    perbulan.append(g)

for i in range(data):
    print("")
    print('-----------------------')
    print('Zakat Penghasilan (Brutto)')
    print('-----------------------')
    print('Nama:',nama)
    print('Harga 1 gram emas:','RP',emas[1])
    print('Penghasilan per bulan:','Rp',gaji[i])
    print('Penghasilan per tahun:','Rp',pertahun[i])
    print('harga nisab(85 gram emas):','Rp',pertahun[i])
    print('Zakat penghasilan:','2,5% x',pertahun[i],'=','Rp,zakat')

if pertahun[i]>= nisab[i]:
    print('Keterangan:Wajib Zakat Rp',zakat[i],'/tahun')
    print('atau Rp',perbulan[i],'/bulan')
    print("")
if pertahun[i]<=nisab[i]:
    print('keterangan:Anda belum termasuk wajib zakat')
    

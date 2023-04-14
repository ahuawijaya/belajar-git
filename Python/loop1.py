#Measure some strings:
words = ('cat','window','defenestrate')
for w in words:
    print(w, len(w))

a =['Mary','had','a','little','lamb']
for i in range (len(a)):
    print(i,a[i])


c=''
while c != 'Great':
    a = int(input('Masukkan angka ='))
    if a < 10 :
         c='Lebih banyak'
    elif a > 10:
         c='Lebih kecil'
    else:
        c='Great'
    print(c)

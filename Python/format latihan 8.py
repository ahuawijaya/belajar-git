a=int(input('Masukkan nilai total belanja:Rp.'))
b=int(input('Masukkan uang yang dibayar:Rp.'))
c=b-a
print('Kembaliannya sebesar Rp.',c,'dengan rincian kembalian')
d=[100000,50000,20000,10000,5000,1000,500,200,100,50]
for x in range(0,10):
    i=0
    while c>=d[x]:
        c=c-d[x]
        i=i+1
        if i>0:
            print('uang Rp.%d sebanyak  %d lembar'%(d[x],i))
        else:
            print('Selesai')
x=5
y=10

temp=x
x=y
y=temp

print('The value of x after swapping:{}'.format(x))
print('The value of y after swapping:{}'.format(y))

kilometers=int(input('Enter value of kilometer:'))
conv_fac=0.621371

miles=kilometers * conv_fac
print('%0.3f kilometers is equal to %0.3f miles'%(kilometers,miles))

c='p'
print('The ASCII value of"'+c+'"is',ord(c))


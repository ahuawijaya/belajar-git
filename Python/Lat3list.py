hobi=[]
stop=False
i=1

while(not stop):
    hobi_baru = input('Inputkan hobi yang ke-{}:'.format(i))
    hobi.append(hobi_baru)
    i+=1
    tanya=input('Mau isi lagi?(y/t):')
    if (tanya =='t'):
        break

print('='*10)
print('Kamu memiliki () hobi ',format(len(hobi)))
for hb in hobi:
    print('-{}',format(hb))

todo_list=['Belajar Python','Belajar Django','Belajar MongoDB','Belajar Sulap','Belajar Flask']
del todo_list[3]

print(todo_list)

a=['a','b','c','d']
a.remove('b')
print(a)

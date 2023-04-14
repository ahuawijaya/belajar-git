print('Geeks : %2d, Portal:%5.2f'%(1,05.333))

print('Total students : %3d,Boys:%2d'%(240,120))

print('%7.30a'%(25))
print('%10.3E'%(356.08977))

print('I love {} , and "{}!",'.format('Akari','Shiori'))
print('{0} and {1}'.format('AK','KA'))
print('{1} and {0}'.format('AK','KA'))

print('Number one portal is {0},{1},and{other}'.format('AKUn','Fot',other='JOK'))
print('Geeks :{0:2d},Portal:{1:8.2f}'.format(12,00.546))
print('Geeks:{a:5d}, Portal :{p:8.2f}'.format(a=453,p=59.058))

tab={"geeks":4127,'for':4098,'geek':8637678}

print('Geeks:{0[geeks]}:d; For:{0[for]:d};''Geeks:{0[geek]:d}'.format(tab))

data=dict(fun ='GeeksForGeeks',adj ='Portal')
print('I love {fun} computer {adj}'.format(**data))

cstr='I love geeksforgeeks'
print('Center aligned string with fillchr:')
print(cstr.center(40,'#'))
print('The left aligned string is:')
print(cstr.ljust(40,'-'))
print('The right aligned string is:')
print(cstr.rjust(40,'-'))

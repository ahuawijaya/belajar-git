username=input('Hello!Welcome to FaceSnap!\n\nUsername:')
password=input('Masukkan password:')

count=0
count+=1

while username == username and password == password:
    if count == 3:
        print('\nThree Username and Password Attempts used.Goodbye')
        break
    elif username == 'elmo' and password == 'blue':
        print('Welcome')
        break
    elif username!='elmo' and password == 'blue':
        print('Your username and password is wrong!')
        break
    elif username == 'elmo' and password != ' blue':
        print('Your password is wrong')
        username=input('Username:')
        password=input('Password:')
        count+=1
        continue
    elif username != 'elmo' and password == ' blue':
        print('Your username is wrong')
        username=input('Username:')
        password=input('Password:')
        count+=1
        continue

        

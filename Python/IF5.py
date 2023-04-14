#Python Program to
#show range() basics
#printing a number
for i in range(10) :
 print(i, end=' ')
#performing sum of first 10 numbers
sum = 0
for i in range (1,10) :
 sum = sum + 1
print('\nSum of first 10 numbers :', sum)

#Python program to demonstrate
#for-else loop
for i in range(1,4):
 print(i)
else : #Executed because no break in for
 print('No Break\n')
#Prints all letters except 'e' and 'e'
for letter in 'geeksforgeeks':
 if letter == 'e' or letter == 's':
     continue
 print('Current Letter :',letter)

#Iterating over dictionary
print('Dictionary Iteration')
d = dict( )
d['xyz'] = 123
d['abc'] = 345
for i in d :
    print(' % s % d' % (i, d[i]))

#Iterating over a String
print('String Iteration')
s = 'Geeks'
for i in s :
    print(i)
 


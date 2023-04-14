count=0
while count<5:
    print(count,'is less than 5')
    count = count+1
else:
    print(count,'is not less than 5')

letter ='z'
for letter in 'abc':
    print(letter)
print('after the loop, letter is',letter)

print(len('aeiou'))

word='oxygen'
for banana in word:
    print(banana)

newstring=''
oldstring='Newton'
for char in oldstring:
    newstring = char + newstring
print(newstring)

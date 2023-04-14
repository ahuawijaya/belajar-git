import random
from collections import Counter

sameWords='''apple banana mango strawberry orange grape pineapple apricot lemon coconat
coconut watermelon cherry papaya berry peaxh lychee muskmelon'''

sameWords=sameWords.split(' ')
word=random.choice(sameWords)

if __name__ == '__main__':
    print('Guess the word! Hint:word is name of a fruit')
    for i in word:
        print('_',end='.')
    print()
    playing=True
    letterGuessed=''
    chances=len(word) + 2
    correct= 0
    try:
        while(chances != 0):
            print()
            chances-=1
            try:
                guess=str(input('Enter a letter to guess:'))
            except:
                print('Enter only a letter!')
                continue
            if not guess.isalpha():
                print('Enter only a LETTER!')
                continue
            elif len(guess)>1:
                    print('Enter only a single letter')
                    continue
            elif guess in letterGuess:
                print('You have already guessed that letter')
                continue
            if guess in word:
                letterGuessed += guess
            for char in word:
                if char in letterGuessed:
                    print(char,end='')
                    correct+=1
                else:
                    print('_',end='')
            if (Counter(LetterGuessed) == Cunter(word)):
                print()
                print('Congratulation!,YOu won!')
                break
        if chances == 0:
            print()
            print('You lost , Try again')
            print('The word was {}'.format(word))
    except KeyboardInterrupt:
        print()
        print('Bye! Try again.')
        exit()

print('Welcome to Quiz Game ')

playing= input('do u want to play:  ? ')

if playing.lower() !='yes':
    quit()
print('Lets begin the game :) ')
score=0

answer=input('Which ocean is the largest on Earth? ')
if answer.lower()=='pacific':
    print('Correct') 
    score=score+1 
else:
    print('Incorrect')

answer=input('what is national animal of India?  ')
if answer.lower()=='tiger':
    print('Correct')
    score=score+1
else:
    print('Incorrect')

answer=input('what is the currency of India?  ')
if answer.lower()=='indian rupee':
    print('Correct')
    score=score+1
else:
    print('Incorrect')

answer=input('which language is mostly spoken in india?  ')
if answer.lower()=='hindi':
    print('Correct')
    score=score+1
else:
    print('Incorrect')

answer=input('which is the smallest state in india?  ')
if answer.lower()=='goa':
    print('Correct')
    score=score+1
else:
    print('Incorrect')

answer=input('what is the name of indian national anthem? ')
if answer.lower()=='jana gana mana':
    print('Correct')
    score=score+1
else:
    print('Incorrect')

print('You Got ' + str(score) + ' Questions Correct !!!')






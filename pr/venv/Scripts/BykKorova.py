import random

a=[0,1,2,3,4,5,6,7,8,9]
digits=int(input('How many digits u want'))
count=digits*5-5
comp=''
for i in range(digits):
    comp=comp+str(a[i])
repeated=[]
random.shuffle(a)
while True:
    keyword=[]
    me=input('Guess the number: ').strip()
    if me in repeated:
        print('\nYou have inserted it already\n')
        continue
    repeated.append(me)
    if len(me)!=digits:
        print('Only {} digits are allowed!'.format(digits))
        continue #ignore this operation
    """if me[0]==me[1]  or me[1]==me[2] or me[0]==me[2]:
        print('Digits cannot be repeated')
        continue"""
    """#1
    for i in range(digits):
        for j in range(i+1,digits):
            if me[i]==me[j]:
                print('digit cannot be repeated!')
                continue"""
    #2
    z=0
    for i in me:
        if me.count(i)>1:
            print('digit cannot be repeated!')
            z=1
            break
    if z==1:
        continue
    if me==comp:
        print('You won!')
        ans=input('Do u wanna play again(Y/N):').strip().lower()
        if ans=='y':
            random.shuffle(a)
            digits = int(input('How many digits u want'))
            comp = ''
            for i in range(digits):
                comp = comp + str(a[i])
            count=digits*5-5
            continue
        else:
            print('It was great game!')
            break
    for i in range(len(comp)):
        if comp[i]==me[i]:
            keyword.append('Byk')
        elif me[i] in comp:
            keyword.append('Korova')
    keyword.sort() #by alf
    if len(keyword)==0:
        print('No matches!')
    else:
        for i in keyword:
            print(i,end=' ')
    count-=1
    print('\nTries left:',count,'\n')
    if count==0:
        print('Game over, my number was',comp)
        ans = input('Do u wanna play again(Y/N):').strip().lower()
        if ans == 'y':
            random.shuffle(a)
            comp = str(a[0]) + str(a[1]) + str(a[2])
            count = 10
            continue
        else:
            print('It was great game!')
            break





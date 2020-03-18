import random
signs=['+','-','*']
def isCorrect(a,b,s,ans):
    if s=='+' and ans==a+b:
        return True
    elif s=='-' and ans==a-b:
        return True
    elif s=='*' and ans==a*b:
        return True
    else:
        return False
for i in range(5):
    a=random.randint(0,15)
    b=random.randint(0,15)
    s=random.choice(signs)
    zadacha=str(a)+' '+s+' '+str(b)+' '+'='
    ans=int(input(zadacha))
    if isCorrect(a,b,s,ans):
        print('Correct!')
    else:
        print('Incorrect')
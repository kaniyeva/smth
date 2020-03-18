import time
toDo=['wake up','study','swim','go home']
now=['lesson']
done=['breakfast','work','movie']
while True:
    time.sleep(1)
    print('todo',toDo)
    print('now',now)
    print('done',done,'\n')
    print('1. Start task')
    print('2. Add task')
    print('3. skip task') #in todo list
    print('4. edit task')
    print('5. search task')
    print('6. show task to do')
    print('7. show task in progress')
    print('8. show finished tasks')
    print('9. Finish task')
    print('10. Exit\n')
    option=int(input('Choose option: '))
    if option==1:
        for i in range(len(toDo)):
            print(i,'-',toDo[i])
        ans=int(input('Enter # of task: '))
        now.append(toDo[ans]) #add task by index from toDo
        del  toDo[ans]
    elif option==2:
        ans=input('Enter a task: ')
        toDo.append(ans)
    elif option==3:
        for i in range(len(toDo)):
            print(i,'-',toDo[i])
        ans=int(input('Enter # of task:'))
        del  toDo[ans]
    elif option==4:
        for i in range(len(toDo)):
            print(i,'-',toDo[i])
        ans=int(input('Enter # of task:'))
        newOne = input('New task: ')
        for i in range(len(toDo)):
            if i==ans:
                toDo[i]==newOne
    elif option==5:
        ans=input('Task: ')
        if ans in toDo:
            print(ans,'in toDo')
        elif ans in now:
            print(ans,'in now')
        elif ans in done:
            print(ans,'in done')
        else:
            print('Not found')
    elif option==6:
        for i in range(len(toDo)):
            print(i,'',toDo[i])
    elif option==7:
        for i in range(len(now)):
            print(i,'',now[i])
    elif option==8:
        for i in range(len(done)):
            print(i,'',done[i])
    elif option==9:
        for i in range(len(now)):
            print(i,'-',now[i])
        ans=int(input('Enter # of task:'))
        for i in range(len(now)):
            if ans==i:
                done.append(now[ans])
                del now[ans]
            else:
                print('Choose id from now')
    elif option==10:
        print('Bye!')
        break
    else: print('Invalid option')


print('********************CALCULATOR********************')
def mainfun():
    print('1. press a for addition\n2. press s for subtraction\n3. press m for multiplication\n4. press d for division\n5. press e to exit\nSelect: ',end='')

    n=input()
    if(n=='a'):
        add()
    if(n=='s'):
        sub()
    if(n=='m'):
        mul()
    if(n=='d'):
        div()
    if(n=='e'):
        exit()
        
def add():
    print('Addition\nEnter a number=')
    a=int(input())
        
    n1='y'
    while(n1=='y'):
        print('Enter another number=')
        b=int(input())
        c=a+b
        a=c
        print('Addition Result:',c)
        print('Enter more (y/n):',end='')
        n1=input()
    else:
        print('Answer=',c)
        mainfun()

def sub():
    print('subtraction\nEnter a number=')
    a=int(input())
        
    n1='y'
    while(n1=='y'):
        print('Enter another number=')
        b=int(input())
        c=a-b
        a=c
        print('Subtraction Result:',c)
        print('Enter more (y/n):',end='')
        n1=input()
    else:
        print('Answer=',c)
        mainfun()

def mul():
    print('Multiplication\nEnter a number=')
    a=int(input())
        
    n1='y'
    while(n1=='y'):
        print('Enter another number=')
        b=int(input())
        c=a*b
        a=c
        print('Addition Result:',c)
        print('Enter more (y/n):',end='')
        n1=input()
    else:
        print('Answer=',c)
        mainfun()
def div():
    print('Division\nEnter a number=')
    a=int(input())
        
    n1='y'
    while(n1=='y'):
        print('Enter another number=')
        b=int(input())
        c=a//db
        a=c
        print('Division Result:',c)
        print('Enter more (y/n):',end='')
        n1=input()
    else:
        print('Answer=',c)
        mainfun()
    

mainfun()
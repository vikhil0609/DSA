def insert():

    if len(queue) >=size:
        print('[QUEUE IS FULL]')
    

    else:
        num = input(print('[ENTER A ELEMENT TO ADD IN QUEUE]'))
        queue.append(num)
        show()

def delete():
    if len(queue) <=0:
        print("[QUEUE IS EMPTY CANNOT DELETE ITEMS]")
    
    else:
        print(f'[DELETED ITEM IS {queue.pop(0)}]')
        show()

def show():
    if len(queue) <=0 :
        print('[QUEUE IS EMPTY]')
    else:
        print('[ELEMENTS IN QUEUE]')
        for i in range(len(queue)):
            print (queue[i])

queue = []
run = True
size = int(input('[ENTER THE SIZE OF QUEUE]'))

while run:
    print('1.insert\n2.delete\n3.show\n4.quit')
    choice = int(input("[ENTER THE CHOICE]"))

    if choice == 1:
        insert()
    elif choice == 2:
        delete()
    elif choice == 3:
        show()
    elif choice == 4:
        run = False
    else:
        print('[ENTER A VALID CHOICE BETWEEN 1~4]')

print('[THANK YOU]')
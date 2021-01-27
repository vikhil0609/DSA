def insert(front,rear):    
    if False:

        pass
    
    else:
        if front == -1 and rear == -1:
            front = 0
            rear = 0
        print('REAR BEFORE',rear)
        num = int(input('[ENTER THE NUMBER]'))
        queue[rear] = num
        rear = rear + 1
        print('REAR AFTER',rear)


def delete(front,rear):
    pass

def display(front,rear):
    print("[ELEMENTS IN CIRCULAR QUEUE]")
    for j in range(0,size):
        if queue[j] == None:
            pass
        else:
            print(queue[j])

run = True
front = -1
rear = -1
size = int(input('[ENTER THE SIZE]'))
queue = [None for i in range(size)]

while run:
    print("1.insert\n2.delete\n3.display\n4.quit")
    choice = int(input("[ENTER THE CHOICE]"))

    if choice == 1:
        insert(front,rear)
    elif choice == 2:
        delete(front,rear)
    elif choice == 3:
        display(front,rear)
    elif choice == 4:
        run = False
    else:
        print('[ENTER A VALLID NUMBER BETWEEN 1~4]')

print(('[THANK YOU]'))
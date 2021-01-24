
def insert():
    if len(stack) >= size :
        print("[STACK IS FULL CANNOT ENTER ELEMENTS]")
    
    else:
        number = int(input("ENTER A NUMBER TO BE INSERTED "))
        stack.append(number)
        show()

def delete():
    if len(stack) == 0:
        print("[STACK IS EMPTY CANNOT DELETE ITEMS]")
    else:
        print(f"[DELETED ELEMENT IS {stack.pop()}] ")
        show()

def show():
    if len(stack) <= 0:
        print("[STACK IS EMPTY]")

    else:
        print("[ELEMENTS IN STACK]")
        for i in range(len(stack)):
            print(stack[i])



stack = []
top = -1
size = int(input("[ENTER THE SIZE OF THE STACK]"))
run = True
print("[STACK PROGRAM IN PYTHON]")
while run:
    print('1.insert\n2.delete\n3.show\n4.exit')
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
        print("[ENTER A VALID NUMBER]")

print("[THANK YOU]")
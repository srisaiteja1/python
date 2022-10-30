import random
svarga_dwara=[0]*3
naraka_dwara=[0]*2
swap=0
no_swap=0
j=0
while(j<10):
    x=random.randint(0, 2)
    svarga_dwara[x]="gandiva"
    for i in range(0,3):
        if(i!=x):
            svarga_dwara[i]="kapala"
            naraka_dwara.append(i)
    choice=int(input("enter your choice"))
    door_open=random.choice(naraka_dwara)
    while(door_open==choice):
        door_open=random.choice(naraka_dwara)
    ch=input("do you want to swap?  if yes enter'y',if no enter 'n' ")
    if(ch=='y'):
        if(svarga_dwara[choice]=="kapala"):
            print("player wins")
            swap=swap+1
        else:
            print("player lost")
    else:
        if(svarga_dwara[choice]=="gandiva"):
            print("player wins")
            no_swap=no_swap+1
        else:
            print("player lost")
    j=j+1
print(swap,no_swap)
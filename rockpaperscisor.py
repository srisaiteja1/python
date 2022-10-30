def game(num1,num2,bit1,bit2):
    p1=num1[bit1]%3
    p2=num2[bit2]%3
    if(playerone[p1]==playertwo[p2]):
        print("draw")
    elif(playerone[p1]=="rock" and playertwo[p2]=="scissor"):
        print(player1,"wins")
    elif(playerone[p1]=="rock" and playertwo[p2]=="paper"):
        print(player2,"wins")
    elif(playerone[p1]=="scissor" and playertwo[p2]=="rock"):
        print(player2,"wins")
    elif(playerone[p1]=="scissor" and playertwo[p2]=="paper"):
        print(player1,"wins")
    elif(playerone[p1]=="paper" and playertwo[p2]=="rock"):
        print(player1,"wins")
    elif(playerone[p1]=="paper" and playertwo[p2]=="scissor"):
        print(player2,"wins")

playerone={0:"rock",1:"paper",2:"scissor"}
playertwo={0:"paper",1:"rock",2:"scissor"}
player1=input("Please, enter your name:")
player2=input("Please, enter your name:")
while(1):
    print(player1,"enter your choice")
    num1=input()
    print(player2,"enter your choice")
    num2=input()
    print(player1,'enter your secret bit position')
    bit1=int(input())
    print(player2,'enter your secret bit position')
    ch=input("do you want to continue  y/n")
    if(ch==n):
        break
    else:
        game(num1,num2,bit1,bit2)
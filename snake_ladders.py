from PIL import Image
import random
end=100
def showboard():
    img=Image.open("python\snake and ladder.png")
    img.show()
def check_ladder(points):
    if(points==8):
        print("you have got a ladder")
        return 26
    elif(points==21):
        print("you have got a ladder")
        return 82
    elif(points==43):
        print("you have got a ladder")
        return 77
    elif(points==50):
        print("you have got a ladder")
        return 91
    elif(points==54):
        print("you have got a ladder")
        return 93
    elif(points==62):
        print("you have got a ladder")
        return 96
    elif(points==66):
        print("you have got a ladder")
        return 87
    elif(points==80):
        print("you have got a ladder")
        return 99
    else:#not any ladder
        return points

def check_snake(points):
    if(points==44):
        print("you stepped on a pit viper,it bit you with nuerotoxin venom")
        return 19
    elif(points==46):
        print("you stepped on a death adder,it bit you with nuerotoxic venom")
        return 5
    elif(points==48):
        print("you have stepped on Boomslang, it bit you with hemotoxin venom")
        return 9
    elif(points==55):
        print("you have stepped on sea snake, it bit you with myotoxin venom")
        return 7
    elif(points==59):
        print("you have stepped on puff adder, it bit you with cytotoxin venom")
        return 17
    elif(points==64):
        print("you have stepped on a european asp, it bit you with heamotoxin venom")
        return 36
    elif(points==69):
        print("you have stepped on a black krait, it bit you with nuerotoxin venom")

        return 33
    elif(points==73):
        print("you have stepped on a rattle snake, it bit you with mixture of heamotoxin and nuerotoxin venom ")
        return 1
    elif(points==83):
        print("you have stepped on an Indian cobra, it bit you with nuerotoxin venom")
        return 19
    elif(points==92):
        print("you have stepped on a black mamba, it bit you with nuerotoxin venom")
        return 51
    elif(points==95):
        print("you stepped on a naagini, she bit you with kaala visham")
        return 24
    elif(points==98):
        print("you stepped on nag raja, he bit you with kaalakuta visham ")
        return 28
    else:
        return points
def thank(player1,point1,player2,point2):
    print("thank you for playing my game,",player1,',',player2)
    if(point1>point2):
        print(player1,"is the winner, you are at:",point1,"and ",player2,'is at:',point2)
    elif(point1==point2):
        print("dear ",player1,player2,"it is a draw",'both of you are at:',point1)
    else:
        print(player2,"is the winner, you are at:",point2,"and ",player1,'is at:',point1)
def play():
    #input of names
    p1_name=input("player1,please enter your name:")
    p2_name=input("player2,please enter your neme:")
    #initial points
    pp1=0
    pp2=0
    turn=0
    while(1):
        if(turn%2==0):
            print(p1_name,"it is your turn")
            #asking player`s choice to continue
            c=input("do you want to continue? if yes enter 'y',if not enter 'n'")
            if(c=='n'):
                thank(p1_name,pp1,p2_name,pp2)
                break
            #it is just like rolling a dice it generates a random integer from 1 to 6
            dice=random.randint(1, 6)
            print("your dice value is",dice)
            pp1=pp1+dice
            pp1=check_ladder(pp1)
            pp1=check_snake(pp1)
            if((pp1>end) or (pp1==end)):
                pp1=end
                thank(p1_name,pp1,p2_name,pp2)
                break
        else:
            print(p2_name,"it is your turn")
            #asking player`s choice to continue
            c=input("do you want to continue? if yes enter 'y',if not enter 'n'")
            if(c=='n'):
                thank(p1_name,pp1,p2_name,pp2)
                break
            #it is just like rolling a dice it generates a random integer from 1 to 6
            dice=random.randint(1, 6)
            print("your dice value is",dice)
            pp2=pp2+dice
            pp2=check_ladder(pp2)
            pp2=check_snake(pp2)
            if((pp2>end) or (pp2==end)):
                pp2=end
                thank(p1_name,pp1,p2_name,pp2)
                break
        turn=turn+1
showboard()
play()
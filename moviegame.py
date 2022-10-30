import random

movies=['annamayya','nayak','arjun suravaram','rama rama krishna krishna','hyper','mathu vadalara','game over','rangasthalam','bharath ane nenu','mahanati','awe!','arjun reddy','bahubali','janatha garage','srimanthudu','race gurram','oohalu gusagusalade','attarintiki daredi','business man','julayi','andhala rakshasi','mirapakai','mr perfect','rebel','gaganam','khaleja','brindavanam','darling','mirchi','run raja run','temper','nannaku prematho','kshanam','pelli choopulu','psv garuda vega','kanche','patas','uppena','roudhram ranam rudhiram','acharya','sarkaru vari pata','radheshyam','kgf','bangarraju','dj tillu','bheemla nayak','khiladi','ghani','good luck sakhi','hero','ramarao on duty','the warrior','ante sundaraniki','major','stand up rahul','sebastian','athidhi devo bhava','rocketry','pakka comercial','narappa','akhanda','uppena','pogaru','geetha govidham','baadshah','aravindha sametha','chaavu kaburu challaga','gopala gopala','sreekaram','valimai','wild dog','pushpa','shaadi mubarak','naandi','zombie reddy','adbutham','vakeel saab','jathi rathnalu','virata parvam','seeti mar','meastro','drushyam','drushyam2','most eligible bachelor','sky lab','love story','republic','konda polam','krack','shyam singha roy','raja raja chora','varudu kavalenu','rowdy boys','maha samudram','rang de','tuck jagadish','master','paagal','check','ala vaikuntapuramlo','sarileru neekevaru','nishabdham','maharshi','gaddalakonda ganesh','evaru','venky mama','ismart shankar','sita','seven','saaho','gang leader','kaithi','vikram','vikrant rona','kanchana','saakshyam']

def create_question(movie):
    n=len(movie)
    lite=list(movie)
    temp=[]
    for i in range(n):
        if(lite[i]==' '):
            temp.append(' ')
        else:
            temp.append('*')
    ques=''.join(str(x) for x in temp)
    return ques


def is_present(letter,picked_movie):
    coun=picked_movie.count(letter)
    if(coun==0):
        return False
    else:
        return True

def unlock(qn,movie,letter):
    ref=list(movie)
    qnlist=list(qn)
    temp1=[]
    n1=len(movie)
    for i in range(n1):
        if(ref[i]==' ' or ref[i]==letter):
            temp1.append(ref[i])
        else:
            if(qnlist[i]=='*'):
                temp1.append('*')
            else:
                temp1.append(qnlist[i])
    ques1=''.join(str(x) for x in temp1)
    return ques1

def thank(p1name,p2name,pp1,pp2):
    print(p1name,"your final score:",pp1)
    print(p2name,"your final score:",pp2)
    if(pp1<pp2):
        print('Congrats',p2name,'you are the winner')
    elif(pp1==pp2):
        print('congrats',p1name,p2name,'both of you are winners')
    else:
         print('Congrats',p1name,'you are the winner')
    print('thank you for playing ')
    print('have a nice day, signing of Sri Sai Teja')

def play():
    p1name=input("player1, please enter your name: ")
    p2name=input("player2, please enter your name: ")
    j=0
    j=int(j)
    pp1=0
    pp1=float(pp1)
    pp2=0
    pp2=float(pp2)
    turn=0
    turn=int(turn)
    will=True
    while(will):
        if(turn % 2 == 0):
            print(p1name,"it is your turn")
            picked_movie=random.choice(movies)
            qn=create_question(picked_movie)
            print(qn)
            modified_qn=qn

            
            for j in range(9):
                if(j>=1):    
                    pp1=pp1-0.1
                letter =input("enter your letter: ")
                if(is_present(letter,picked_movie)):
                    #unlock the charecter
                    modified_qn=unlock(modified_qn,picked_movie,letter)
                    print(modified_qn)
                    d=input("press 1 to guess the movie name, 2 to unlock another letter: ")
                    if(d == '1' ):
                        ans=input('enter the movie name: ')
                        if(ans == picked_movie):
                            pp1=pp1+1
                            print('correct')
                            print(p1name,'your score is: ',pp1)
                            break
                        else:
                            print('wrong answer! the answer is',picked_movie)
                            pp1=pp1-0.2
                            break
                            
                else:
                    print(letter,"not found")
                
            print('correct answer is',picked_movie)    
            c=int(input('press 1 to continue, 0 to exit'))
            if( c == 0):
                thank(p1name,p2name,pp1,pp2)
                
                will=False
        else:
            print(p2name,'it is your turn')
            picked_movie=random.choice(movies)
            qn=create_question(picked_movie)
            print(qn)
            modified_qn=qn

            
            for j in range(4):
                if(j >= 1):
                    pp2=pp2-0.1
                letter =input("enter your letter: ")
                if(is_present(letter,picked_movie)):
                    #unlock the charecter
                    modified_qn=unlock(modified_qn,picked_movie,letter)
                    print(modified_qn)
                    d=int(input("press 1 to guess the movie name, 2 to unlock another letter: "))
                    if(d == 1):
                        ans=input('enter the movie name: ')
                        if(ans == picked_movie):
                            pp2=pp2+1
                            print('correct')
                            
                            print(p2name,'your score is: ',pp2)
                            break
                        else:
                            print('wrong answer! correct answer is:',picked_movie)
                            pp2=pp2-0.2
                       
                else:
                    print(letter,"not found")
                
            print('correct answer is:',picked_movie)
            c=int(input('press 1 to continue, 0 to exit'))
            if(c == 0 ):
                thank(p1name,p2name,pp1,pp2)
                will=False        
        turn=turn+1


play()
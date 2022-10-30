import random
def choose():
    dictionary=['arjuna','bhima','nakula','sahadeva','saaho','prabhas','yudhishtir','krishna','narayana','rudra','atala','vitala','sutala','rasatala','talatala','mahatala','patala','satya','tapoloka','janaloka','maharloka','svargaloka','bhuvarloka','satva','rajoguna','tamoguna','madhava','madhusudhana','keshava','srihari','vasudeva','radhakrishna','sitarama','meghana','associate','adventure',' architect','ambitious','accompany','ambulance',' appraisal',' available','afternoon',' advantage','abandoned',' attending','affiliate','authentic','alternate','academics','amusement','advertise','algorithm','alcoholic','addiction','adjoining','affection','animation','banana','black','berth','basket','bingo','binge','bigger','biggest','boast','beast','backfiring','background','circus','curtain','cinema','chair','coffee','calendar','coconut','crude','centre','central','control','carrot','carrier','courier','cottage','cheese','dinosaur','donkey','dance','Danger','debunk','disaster','disqualification','discrimination','earlobe','earlier','eager','Eagles','earthquake','Enthusiastic','Elegant','Earnest','Empowered','Economical','Efficient','edible','expertise','fabric','factor','factory','faculty','fabricate','fallible','famine','feasible','finite','fodder','foresight','fortress','fracture','garage','garbage','garden','garment','garnish','galvanize','gender','generalization','generation','generic','genuine','gesture','globalization','gorgeous','graduation','grandeur','graphic','gratitude','habitat','hallow','harmony','havoc','hearty','hemisphere','herbivorous','hereditary','heritage','heterogeneous','hibernate','homogeneous','horizon','hospitable','humiliation','hybrid','hypothetical','idealistic','ideological','idiom','illustrious','impartial','imperative','imperious','implicit','inaugurate','incarnation','inception','incorrigible','increment','inevitable','inherent','innovative','intimation','intrinsic','jacket','jealousy','judicious','juggernaut','jurisdiction','justify','kindled','kinetic','lassitude','latent','latter','laudable','legacy','leniency','lethal','lethargic','liability','lineage','linguistic','lucrative','lunar','magnitude','majestic','malevolent','malignant','manipulated','marital','Maternal','matrix','maturation','mediate','melodramatic','mercenary','metamorphosis','methodical','migration','monolithic','mythical','narrative','nationalism','native','navigable','necessity','necromancy','negative','neglected','negotiations','nepotism','network','neutralization','nocturnal','nomenclature','nostalgic','notorious','nursery','nutrient','obedient','objective','obligation','obtain','olfactory','Omnipotent','omnipresent','Omniscient','operative','opposition','ordinance','orientation','ornithologist','orthodox','outcome','overcome','pandemic','paradox','patriotism','perish','personification','philanthropist','placid','polarize','precedent','predator','predecessors','primitive','prodigy','proportional','prosperity','prototype','quadrilateral','qualified','quantitative','quantum','quarantine','radicals','rapport','rebellious','reciprocate','refined','rejuvenate','relentless','remote','resonating','revolutionize','ruminate','ruthless','saturated','scarce','seditious','segregation','semantic','sentient','sentiment','sequential','solvent','spectators','spectrum','spontaneous','stagnant','stamina','subordinate','superficial','supernatural','supplementary','suppression','symmetry','synchronous','tedious','temperament','terminalogy','terrestrial','threshold','topography','trajectory','transparent','trilogy','unalterable','unanimous','unattainable','unbiased','uncanny','unconditional','unconventional','unexceptionable','unilateral','universal','unprecedented','unspecified','unstable','vacate','validated','vanquished','variables','velocity','versatile','vicinity','villain','vulnerable','waive','wardrobe','warranty','welfare','withdrawn','wretched','xenophobia','yahoo','saahithi','shivatej','manitej','karthikeya','manisha','varshini','aakash','shrawan','vyshnavi','abhinavreddy','bhanulatha','sirisha','saisharath','sravani','abhiram','amulya','sairam','vamshi','akhil','nikitha','jayvardhan','bruhadeswar','bhavana','vivek','prashanth','bhanu','sathwik','varshitha','srikar','rajesh','akshay','saipriya','krunal','rishi','naveena','shashi','ruthwik','ashwini','ananya','sandeep','premvardhan','krushna','harsha','tejaswini','yamuna','lasya','sreetaj','shiva','reshma','abdullah','asifa','pranay','rohan','abhinav','shivasai','karthik','srisaiteja','vishnu','yeshwanth','sriman','navya','samhith']

    pick=random.choice(dictionary)
    return pick
def jumble(word):
    jumbled="".join(random.sample(word,len(word)))
    return jumbled
def thank(play1,play2,point1,point2):
    if(point1>point2):
        print("thank you",play1,play2,"your final scores are",point1,point2)
        print(play1,"is the winner")
    elif(point1==point2):
        print("thank you",play1,play2,"your final scores are",point1,point2)
        print("both of your scores are equal so it is tie ")
    else:
         print("thank you",play1,play2,"your final scores are",point1,point2)
         print(play2,"is the winner")

def play():
    player1=input('player1, please enter your name?')
    player2=input('player2, please enter your name?')
    p1=0
    p2=0
    turn=0
    while(1):
        #computer must create a question
        questionword=choose()
        question=jumble(questionword)
        print("the question is",question)

        if(turn%2==0):
            print(player1,'it is your turn')
            ans=input("guess the answer:")
            if(ans==questionword):
                p1=p1+1
                print("wow!right answer",player1, "your score is:",p1)
            else:
                print("better luck next time,the word is:",questionword)
                c1=int(input('press 1 to continue 0 to exit:'))
                if(c1==0):
                    thank(player1,player2,p1,p2)
                    break
        else:
            print(player2,'it is your turn')
            ans=input("guess the answer:")
            if(ans==questionword):
                p2=p2+1
                print("wow!right answer",player2, "your score is:",p2)
            else:
                print("better luck next time,the word is:",questionword)
                c2=int(input('press 1 to continue 0 to exit:'))
                if(c2==0):
                    thank(player1,player2,p1,p2)
                    break
        turn=turn+1

play()
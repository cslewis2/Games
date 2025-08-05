'''simple game of craps v computer. 7 or 11 wins'''
from random import choice
rolls=int(input('Feeling lucky? How many rolls do you wanna take chump? '))
for roll in range(0,rolls):
    def tdie():
        '''rolling the dices'''    
        for dice in range (0,rolls):
            die1=choice([1,2,3,4,5,6])
            die2=choice([1,2,3,4,5,6])
            print(die1,die2)
            if die1 + die2 == 7 or die1 + die2==11:
                print(choice(['ya got me','you win','git ya next time','are you cheating kid?']))
            else:
                print(choice(['looser','lost it all...call mama','yo money gone baby',
                              'gee your cash smells terrific!'
                              ,'boom goes da dynamite!','in yo face','run dem pockets homie']))
        return ([die1,die2])
    #print(tdie())--not necessary since printing within function already.
#save tuple pair in a list for future saving to csv or something...
data=[]
for d in range (0,rolls):
    data.append(tdie())
print (data)

#for s in range (0,rolls:
#    )

#S=[5,4,5,7]
#T=[1,2,3,6]
#print (sum(T)+sum(S))

#VERIFY COMIT AND UPLOAD

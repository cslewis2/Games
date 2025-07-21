from random import randint

#define the physical die and the number of them in use
    #how many sides on a single die
    #what range of values to use on each die facet?
#simple case--define 1 roll of 1 die of X num of facets
#random number generation of range individual facet values
#should range of values be decoupled from number of sides--e.g. 6 sided die valid values == 1-6?
    #could be decoupled to be any range or random number combination
#need to know how many rolls user wants to have-start simple with 1 roll.


def die_sides():
    '''number of dies and number of die facets on each die'''
    die_sides=int(input('how many facets on your dice?  '))
    die_num=int(input('how many dice are in use?  '))
    facet_values=randint(1,die_sides)
    die_rolls=int(input('how many rolls do u want to take?  '))
    
    dice_desc=[die_num,die_sides]       # remember fstrings use double quotation marks...
    facet_face_read=randint(1,die_sides)
    
      return dice_desc 
#possible alt:print (f"you want {die_num} dice containing {facets} factes...")
#die_def=die_sides()   #die_sides return now global list]

print (die_sides())
#print (die_def()[0])
#print(die_def()[1])



def die_rolls():
    '''die rolls'''
    for dice in range (0,dice_desc[0]):
        roll=randint(1,dice_desc[1]) 
    
die_sides()

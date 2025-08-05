'''overly simple dice simulation'''

from random import randint



#define the physical die and the number of them in use
    #how many sides on a single die
    #what range of values to use on each die facet?
#simple case--define 1 roll of 1 die of X num of facets
#random number generation of range individual facet values
#should range of values be decoupled from number of sides--e.g. 6 sided die valid values == 1-6?
    #could be decoupled to be any range or random number combination
    #number of sides is actually irrelevant, just limt
    # to number of sides eg 7 sides==range 1,7
#need to know how many rolls user wants to have-start simple with 1 roll.


'''number of dies and number of die facets on each die'''
die_sides=int(input('how many facets on your dice?  '))
#facet_values=int(randint(0,die_sides))
die_num=int(input('how many dice are in use?  '))
die_rolls=int(input('how many rolls do u want to take?  '))
#for die_roll in range (0,die_rolls):
#    for die_roll in range (0,die_rolls):
#        die_value=randint(1,die_sides)
#        print (die_value)

total_data_points=(die_rolls)*(die_num)
#calculates total number of data points generated
#for i in range(0,total_data_points):
#all_rolls_data=((randint(1,die_sides))
# print ((all_rolls_data))
#generates random number for each die in each roll
#print(list(randint,(1,die_sides)))

#    for d_sides in range(1,die_sides):
#        dice_data=randint(1,facet_values)
    #print (d_num)
#print (d)
#def a_roll():
#    i=(die_num)*(die_sides)
#    j=randint(1,i)
#    #print (j)
#    return i,j
#print(a_roll())


#print (f"parameters: facets=  {die_sides} facet values= {facet_values}
#total num dice= {die_num} total num rolls= {die_rolls}")
    #dice_desc=[die_num,die_sides]       # remember fstrings use double quotation marks...
#    facet_face_read=randint(1,die_sides)
#possible alt:print (f"you want {die_num} dice containing {facets} factes...")

#def die_rolls():
#    '''die rolls'''
#    for dice in range (0,dice_desc[0]):
#        roll=randint(1,dice_desc[1])
#die_sides()

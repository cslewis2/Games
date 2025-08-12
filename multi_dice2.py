'''overly simple dice simulation'''

from random import randint


# number of dies and number of die facets on each die
die_sides=int(input('how many facets on your dice?  '))
#facet_values=int(randint(0,die_sides))
die_num=int(input('how many dice are in use?  '))
die_rolls=int(input('how many rolls do u want to take?  '))
def new_func(die_sides, die_rolls):
    '''roll guts protocol'''
    for die_roll in range (0,die_rolls):
        for die_roll in range (0,die_rolls):
            die_value=randint(1,die_sides)
            print (list(die_value))

new_func(die_sides, die_rolls)

total_data_points=(die_rolls)*(die_num)
#calculates total number of data points generated

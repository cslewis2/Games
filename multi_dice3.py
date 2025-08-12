quicktest
from random import randint

'''simple dice simulator'''

#die_sides=int(input('how many facets on your dice?  ')
While True:
    restart=False
    try:
    die_sides=int(input('how many facets on your dice?  '))
    if die_sides < 6:
        print ('Enter value greater than 6')
    except ValueError:
    print('try again!')
    
    try:
    die_num=int(input('how many dice are in use?  '))
    if die_num <1:
        print('Please enter number of dice greater than 0')
    except ValueError:
    print ('try again')
    
    try:
    die_rolls=int(input('how many rolls do u want to take?  '))
    if die_rolls < 0:
        print('Enter a number of rolls  greater than 0')
    except ValueError:
    print('try again')#'Please enter rolls greater than 0')

turn_data = [die_sides,die_num,die_rolls]
    else
        print ('program terminated')

#total_data_points=(die_rolls)*(die_num)
#calculates total number of data points generated
#for i in range(0,total_data_points):
#    all_rolls_data=((randint(1,die_sides)))
#    print ((all_rolls_data))
#print(turn_data)

if __name__ == '__main__':
    turn_data = [die_sides,die_num,die_rolls]
        
        
    total_data_points=(die_rolls)*(die_num)
    #calculates total number of data points generated
    for i in range(0,total_data_points):
        all_rolls_data=((randint(1,die_sides)))
        print ((all_rolls_data))
    print(turn_data)
    
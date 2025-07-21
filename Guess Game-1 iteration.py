# Simple guessing game with answer defined in variable A...Can improve by
# 1.importing RND number generator in place of predefined answer
# 2.using a counter to iterate a fixed number of attempts
# 3.activate error logging for giggles 

print ('GUESS A NUMBER LESS THAN 10, Whats your guess?')
A = (int(input('What is your guess???'   )))
if A == 4:
    print('CORRECT!!!')
# != is python not equal notation
elif A < 4:
    print('Higher!!')
elif A > 4:
    print('Lower!!')
#DO NOT HAVE to have final else statement!
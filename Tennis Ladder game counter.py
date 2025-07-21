'''will eventually derive final individual player games won for each player on a court in a competetive ladder'''

from math import comb,perm
import itertools

players=['p1','p2','p3','p4']
# print (teams)
# j=comb(4,2)
# print(j)
y=set(itertools.permutations(players,2))
y1=list(itertools.permutations(players,2))
# overkill, just list the combinations, funct returns a set with no reps or reversals

print (y)
print (y1)


#RETHINK....

# INPUT PLAYER NAMES
# INPUT SET SCORES
# USE INDICES TO CALCULATE GAMES PER PLAYER,
# THEN 
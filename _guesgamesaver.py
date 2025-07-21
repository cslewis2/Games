from random import randint
import os.path
import csv
#m=0,1
#n=0,1
#if m == n:
#    print('equal')
#else:
#    print('not equal')
#m in n
#match=[]

file_exists=os.path.isfile('gamedat.csv')
for i in range (1,10):
    def ranpair():
        x,y=randint(0,1),randint(0,1)
        return (x,y)
    m=ranpair()

    def testpair():
        a,b=randint(0,1),randint(0,1)
        return (a,b)
    n=testpair()

    def capture():
        if m == n:
            capdat=[i,m,n,'win']
        else:
            capdat=[i,m,n,'loss'] 
        return capdat
    t=capture()
    
    with open('gamedat.csv','a',newline='') as csvfile:
        writerow=(['count','initval','compval','result'])
        fieldnames=['count','initval','compval','result']
        writer=csv.DictWriter(csvfile,fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()
        writer.writerow({'count':t[0],'initval':t[1],'compval':t[2],'result':t[3]})
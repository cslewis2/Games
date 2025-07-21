print("You wake up lost underground in a maze of tunnels. You have a bronze sword in your hand and torn leather armor. You light a torch with your flint and steel and try to get your bearings.")
import random
tunnelChoice = 0
dangerTunnel=random.randint(1,2)
lives=5
gold=0
dragonKills=0
tunnelSuccesses=0
armor=0
weapon=0
wetFeet=0
while tunnelChoice < 1 or tunnelChoice > 2:
    if tunnelSuccesses != 20:
        dangerTunnel=random.randint(1,2)
        if wetFeet>0:
            print("*squish* *squish* You walk up to where two tunnels intersect.")
        else:
            print("You walk up to where two tunnels intersect.")
        wetFeet=wetFeet-1
        tunnelChoice=(input("Choose tunnel 1 or tunnel 2: "))
        if tunnelChoice == "1":
            tunnelChoice=1
        elif tunnelChoice == "2":
            tunnelChoice=2
        else:
            tunnelChoice=0
        if tunnelChoice==0:
            tunnelChoice=0
        else:
            if tunnelChoice == dangerTunnel:
                dangerType=0
                dangerType=random.randint(1,5)
                dragonChoice=0
                dragonChoice1=0
                if dangerType==1:
#start combat
                    print("As you enter the tunnel a goblin jumps out from behind some old boxes!")
                    while dragonChoice1 == 0:
                        dragonChoice=(input("Will you run or attack? "))
                        if dragonChoice == "attack":
                            attackSuccess = random.randint(1,50)
                            attackChance=0
                            attackChance=weapon+armor+attackSuccess
                            if attackChance >= 5:
                                goldDrop=0
                                goldDrop=random.randint(3,10)
                                gold=gold+goldDrop
                                print("You slay the goblin and pick up", goldDrop, "gold!")
                                dragonKills=dragonKills+1
                            else:
                                lives=lives-1
                                if lives == 0:
                                    print("You are killed by the goblin. You managed to collect", gold,"gold and killed", dragonKills, "enemies!")
                                elif lives == 1:
                                    print("You are wounded but barely manage to escape! You only have", lives, "life left!!!")
                                else:
                                    print("You are wounded but manage to escape! You have", lives, "lives left!")
                            dragonChoice1=1
                        elif dragonChoice == "run":
                            runSuccess = 0
                            runSuccess=random.randint(1,5)
                            if runSuccess >=2:
                                print("You run past the goblin and jump through the door to the next tunnel")
                            else:
                                lives=lives-1
                                if lives == 0:
                                    print("You are killed by the goblin! You managed to collect", gold,"gold and killed", dragonKills, "enemies!")
                                elif lives == 1:
                                    print("You are wounded but barely manage to escape! You only have", lives, "life left!!!")
                                else:
                                    print("You are wounded but manage to escape! You have", lives, "lives left!")
                            dragonChoice1=2
                        else:
                            dragonChoice1==0
#end combat
                elif dangerType==2:
#start combat
                    print("As you enter the tunnel a troll stomps out from behind a corner!")
                    while dragonChoice1 == 0:
                        dragonChoice=(input("Will you run or attack? "))
                        if dragonChoice == "attack":
                            attackSuccess = random.randint(1,50)
                            attackChance=0
                            attackChance=weapon+armor+attackSuccess
                            if attackChance >= 10:
                                goldDrop=0
                                goldDrop=random.randint(5,12)
                                gold=gold+goldDrop
                                print("You slay the troll and pick up", goldDrop, "gold!")
                                dragonKills=dragonKills+1
                            else:
                                lives=lives-1
                                if lives == 0:
                                    print("You are killed by the troll. You managed to collect", gold,"gold and killed", dragonKills, "enemies!")
                                elif lives == 1:
                                    print("You are wounded but barely manage to escape! You only have", lives, "life left!!!")
                                else:
                                    print("You are wounded but manage to escape! You have", lives, "lives left!")
                            dragonChoice1=1
                        elif dragonChoice == "run":
                            runSuccess = 0
                            runSuccess=random.randint(1,5)
                            if runSuccess >=2:
                                print("You run past the troll and jump through the door to the next tunnel")
                            else:
                                lives=lives-1
                                if lives == 0:
                                    print("You are killed by the troll! You managed to collect", gold,"gold and killed", dragonKills, "enemies!")
                                elif lives == 1:
                                    print("You are wounded but barely manage to escape! You only have", lives, "life left!!!")
                                else:
                                    print("You are wounded but manage to escape! You have", lives, "lives left!")
                            dragonChoice1=2
                        else:
                            dragonChoice1==0
#end combat
                elif dangerType==3:
#start combat
                    print("As you creep into the tunnel a manticore leaps over a pile of armor towards you!")
                    while dragonChoice1 == 0:
                        dragonChoice=(input("Will you run or attack? "))
                        if dragonChoice == "attack":
                            attackSuccess = random.randint(1,50)
                            attackChance=0
                            attackChance=weapon+armor+attackSuccess
                            if attackChance >= 15:
                                goldDrop=0
                                goldDrop=random.randint(7,15)
                                gold=gold+goldDrop
                                print("You kill the manticore and pick up", goldDrop, "gold!")
                                dragonKills=dragonKills+1
                            else:
                                lives=lives-1
                                if lives == 0:
                                    print("You are killed by the manticore. You managed to collect", gold,"gold and killed", dragonKills, "enemies!")
                                elif lives == 1:
                                    print("You are wounded but barely manage to escape! You only have", lives, "life left!!!")
                                else:
                                    print("You are wounded but manage to escape! You have", lives, "lives left!")
                            dragonChoice1=1
                        elif dragonChoice == "run":
                            runSuccess = 0
                            runSuccess=random.randint(1,5)
                            if runSuccess >=2:
                                print("You run past the Manticore and jump through the door to the next tunnel")
                            else:
                                lives=lives-1
                                if lives == 0:
                                    print("You are killed by the Manticore! You managed to collect", gold,"gold and killed", dragonKills, "enemies!")
                                elif lives == 1:
                                    print("You are wounded but barely manage to escape! You only have", lives, "life left!!!")
                                else:
                                    print("You are wounded but manage to escape! You have", lives, "lives left!")
                            dragonChoice1=2
                        else:
                            dragonChoice1==0
#end combat
                elif dangerType==4:
#start combat
                    print("As you stroll through the tunnel a small dragon roars in your direction!")
                    while dragonChoice1 == 0:
                        dragonChoice=(input("Will you run or attack? "))
                        if dragonChoice == "attack":
                            attackSuccess = random.randint(1,50)
                            attackChance=0
                            attackChance=weapon+armor+attackSuccess
                            if attackChance >= 20:
                                goldDrop=0
                                goldDrop=random.randint(15,30)
                                gold=gold+goldDrop
                                print("You defeat the dragon and pick up", goldDrop, "gold!")
                                dragonKills=dragonKills+1
                            else:
                                lives=lives-1
                                if lives == 0:
                                    print("You are killed by the dragon. You managed to collect", gold,"gold and killed", dragonKills, "enemies!")
                                elif lives == 1:
                                    print("You are wounded but barely manage to escape! You only have", lives, "life left!!!")
                                else:
                                    print("You are wounded but manage to escape! You have", lives, "lives left!")
                            dragonChoice1=1
                        elif dragonChoice == "run":
                            runSuccess = 0
                            runSuccess=random.randint(1,5)
                            if runSuccess >=2:
                                print("You run past the dragon and jump through the door to the next tunnel")
                            else:
                                lives=lives-1
                                if lives == 0:
                                    print("You are killed by the dragon! You managed to collect", gold,"gold and killed", dragonKills, "enemies!")
                                elif lives == 1:
                                    print("You are wounded but barely manage to escape! You only have", lives, "life left!!!")
                                else:
                                    print("You are wounded but manage to escape! You have", lives, "lives left!")
                            dragonChoice1=2
                        else:
                            dragonChoice1==0
#end combat
                elif dangerType==5:
#start combat
                    print("The moment you step into the tunnel an earpiercing roar and blast of heat great you. You look up to see yourself facing an adult dragon!")
                    print(r"""   (  )   /\   _                 (     
    \ |  (  \ ( \.(               )                      _____
  \  \ \  `  `   ) \             (  ___                 / _   \
 (_`    \+   . x  ( .\            \/   \____-----------/ (o)   \_
- .-               \+  ;          (  O                           \____
                          )        \_____________  `              \  /
(__                +- .( -'.- <. - _  VVVVVVV VV V\                 \/
(_____            ._._: <_ - <- _  (--  _AAAAAAA__A_/                  |
  .    /./.+-  . .- /  +--  - .     \______________//_              \_______
  (__ ' /x  / x _/ (                                  \___'          \     /
 , x / ( '  . / .  /                                      |           \   /
    /  /  _/ /    +                                      /              \/
   '  (__/                                             /                  \
                    """)
                    while dragonChoice1 == 0:
                        dragonChoice=(input("Will you run or attack? "))
                        if dragonChoice == "attack":
                            attackSuccess = random.randint(1,50)
                            attackChance=0
                            attackChance=weapon+armor+attackSuccess
                            if attackChance >= 30:
                                goldDrop=0
                                goldDrop=random.randint(50,100)
                                gold=gold+goldDrop
                                print("You slay the dragon and pick up", goldDrop, "gold!")
                                dragonKills=dragonKills+1
                            else:
                                lives=lives-1
                                if lives == 0:
                                    print("You are killed by the dragon. You managed to collect", gold,"gold and killed", dragonKills, "enemies!")
                                elif lives == 1:
                                    print("You are wounded but barely manage to escape! You only have", lives, "life left!!!")
                                else:
                                    print("You are wounded but manage to escape! You have", lives, "lives left!")
                            dragonChoice1=1
                        elif dragonChoice == "run":
                            runSuccess = 0
                            runSuccess=random.randint(1,5)
                            if runSuccess >=2:
                                print("You run past the dragon and jump through the door to the next tunnel")
                            else:
                                lives=lives-1
                                if lives == 0:
                                    print("You are killed by the dragon! You managed to collect", gold,"gold and killed", dragonKills, "enemies!")
                                elif lives == 1:
                                    print("You are wounded but barely manage to escape! You only have", lives, "life left!!!")
                                else:
                                    print("You are wounded but manage to escape! You have", lives, "lives left!")
                            dragonChoice1=2
                        else:
                            dragonChoice1==0
#end combat
                tunnelChoice = 0
                tunnelSuccesses=tunnelSuccesses+1
            else:
                tunnelDesc=random.randint(1,10)
                tunnelSuccesses=tunnelSuccesses+1
                goldDrop=0
                goldDrop=random.randint(3,10)
                gold=gold+goldDrop
                if tunnelSuccesses!=10:
                    if tunnelDesc == 1:
                        print("You enter a tunnel with rough stone walls and a small stack of boxes. You find", goldDrop, "gold in the boxes.")
                    elif tunnelDesc == 2:
                        if armor==0:
                            print("You enter a massive tunnel with stacks of broken armor. You find a set of armor your size.")
                        else:
                            print("You find better armor that fits you. You've never felt safer")
                        armor=armor+1
                    elif tunnelDesc == 3:
                        if weapon==0:
                            print("You find a sharper sword made out of strong steel")
                        else:
                            print("You find a blade that calls out to you, as if it's meant to be in your hand")
                        weapon=weapon+1
                    elif tunnelDesc == 4:
                        print("You find a giant tunnel with a throne in the middle of it. After poking around near it, you activate a secret compartment with a diamond worth 20 gold!")
                    elif tunnelDesc == 5:
                        print("You slowly travel through cramped tunnel that at times requires you to crawl to get through it. You're thankful that you aren't too clausterphobic, but still...")
                    elif tunnelDesc == 6:
                        lives=lives+1
                        print("You enter a tunnel that smells vaguely of smoke. You find the remains of an old camp. You decide to rest and regain your strength. You gained a life. You have", lives, "lives left.")
                    elif tunnelDesc == 7:
                        print("You shuffle through a tunnel with water flowing across the floor. It's not enough to carry you away, but now your feet are wet and your shoes are making squishy noises.")
                        wetFeet=2
                    elif tunnelDesc == 8:
                        print("Enter a mysterious tunnel with runes written along the walls. You find a table and a bottle that says DRINK ME.")
                        willThey=input("Do you drink it or leave it? ")
                        drinkIt=0
                        drinkDoes=0
                        while drinkIt == 0:
                            if willThey == "drink it":
                                drinkDoes=random.randint(1,5)
                                drinkIt=1
                                if drinkDoes == 1:
                                    print("You feel weak and tired. You probably shouldn't drink random drinks in tunnels.")
                                    if lives == 0:
                                        print("The poison in the drink kills you. You managed to collect", gold,"gold and killed", dragonKills, "enemies!")
                                    elif lives == 1:
                                        print("You are weakened by the poison and are barely conscious! You only have", lives, "life left!!!")
                                    else:
                                        print("You are weakened by the poison! You have", lives, "lives left!")
                                elif drinkDoes > 1 or drinkDoes < 5:
                                    print("You feel all your aches and pains fade away as the drink enters your stomach. You gained a life. You have", lives, "lives left.")
                                else:
                                    print("You have been teleported out of the tunnels!")
                                    break
                            elif willThey == "leave it":
                                drinkIt=2
                                print("You set the drink on and continue your journey.")
                            else:
                                drinkIt=0
                    elif tunnelDesc == 9:
                        print("You pass through a tunnel that seems to go on for miles, but you can't tell if you're headed up or down.")
                    else:
                        print("You enter a tunnel full of brilliant crystals that dance in the torchlight. You enjoy their beauty as you pass through.")
                    tunnelChoice = 0
                else:
                    tunnelSuccesses = 20
    else:
        break
print("You escaped to the surface! You managed to collect", gold,"gold and killed", dragonKills, "enemies on your journey! Congratulations adventurer!")
print(r"""                        |>>>
                        |
                       /^\             
                       | |             
                   |>  |-|             
            |>    /^\  | |             
           /^\  / [_] \+-+             
   |>     |---||-------| ||>      |>      
 _/^\_    _/^\_|  [_]  |_/^\_   _/^\_  
 |___|    |___||_______||___|   |___|  
  | |======| |===========| |=====| |   
  | |      | |    /^\    | |     | |   
  | |      | |   |   |   | |     | |   
  |_|______|_|__ |   |___|_|_____|_|  """)
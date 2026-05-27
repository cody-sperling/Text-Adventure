#By Cody Sperling


#bringing in libraries
import time
import os
import random
import sys

#initializing global variables
health = 100
sack = []
trapdoor_check = 0
#this variable is used to make sure that the trap door sequence in the left room of the temple only happens once




#after every point where the user takes damage this checks whether the user has 0 or less health for game over
def check_gameover(health):
    if health <= 0:
        print("Gameover")
        print(f"Your health reached {health}")
        sys.exit()







def pick_up_sword():      



#first if statement here is to make sure the user can't pick up infinity swords

    if "rusty sword" not in sack:
        
        print("After looking in the bushes you find a rusty sword. ", end="")       
        pickup = input("Would you like to put the sword in your sack? (type 'yes' or 'no'): ")


        if pickup == "yes":
            
            print("You added the rusty sword to your collection")
            sack.append("rusty sword")
            fork_in_road(health,trapdoor_check)


        elif pickup == "no":

            print("better to leave this here...")
            fork_in_road(health,trapdoor_check)
        

        else:
            print("Let's try this again...")
            pick_up_sword()
        
        
    elif "rusty sword" in sack:
        print("You already picked this up")
        fork_in_road(health,trapdoor_check)









def look_in_sack():
#Prints contents of sack, first if is used to check that there is at least something in the sack
    if len(sack) > 0:
        n = 0
        print("You currently have:", end=" ")

        for i in sack:

#checks whether the item is in the last index so there is no extra comma

            if n+1 < len(sack):                
                print(i, end=", ")
                n += 1                

#if item is the last item in the sack end with a period
            elif n+1 == len(sack):
                print(i, end=".")

        print()
        time.sleep(2)
        print("You finish looking in your sack.")
        


#accounts for sack being empty

    else:
        print("You have nothing in your sack right now.")
        time.sleep(1)
        print("You finish looking in your sack.")
        














#room functions below






def river(health,trapdoor_check):

#used this if statement to check if the user visited this area and got the lucky charm already.
    if "lucky charm" not in sack:
#checks if boat is an option to use
        if "boat" in sack:
            decision = input("You may either 'Turn around' (back to fork), 'Boat across', 'Swim across', or 'Look in sack' \nPlease make your decision now: ")
            while True:
                if decision == "Turn around":
                    print("You decide to head back to the fork.")
                    fork_in_road(health,trapdoor_check)



                elif decision == "Boat across":
                    print("You decide to take the boat you acquired and paddle across the river. You make it across and knock on the door of the cabin.")
                    cabin(health,trapdoor_check)
        

#gives player 10% chance of making it across without losing health
                elif decision == "Swim across":
                    success_chance = random.randint(1,10)
                    if success_chance == 10:
                        print("You decide to cross the river by swimming. \nLuckily, you are a strong swimmer and you aren't swept away by the current. You reach the other side and knock on the door of the cabin.")
                        cabin(health,trapdoor_check)
#90% chance of user losing 45 health
                    elif success_chance < 10:
                        health -= 45
                        print(f"You decide to swim across the river. You are about half way across when you hear something burst out of the water behind you. \nYou turn around to see a massive serpent-like sea creature with razor sharp teeth swimming toward you. \nYou begin swimming as fast as you can, lunging for the shoreline. Just as you are almost running onto land, the creature lunges for you and takes a small chunk of your leg. \nYour health is now {health}.")
                        check_gameover(health)
                        print("You hobble onto land and the creature sinks back into the water. You decide to go and knock on the door of the cabin.")
                        cabin(health,trapdoor_check)


                elif decision == "Look in sack":
                    look_in_sack()
                    river(health,trapdoor_check)


                else:
                    print("Please choose one of the specified options.")
                    river(health,trapdoor_check)
    

#same code but without the option to use the boat because the player doesn't have it yet
        if "boat" not in sack:

            decision = input("You may either 'Turn around' (back to fork), 'Swim across', or 'Look in sack' \nPlease make your decision now: ")
            while True:
                if decision == "Turn around":
                    print("You decide to head back to the fork.")
                    fork_in_road(health,trapdoor_check)
        
                elif decision == "Swim across":
                    success_chance = random.randint(1,10)
                    if success_chance == 10:
                        print("You decide to cross the river by swimming. Luckily, you are a strong swimmer and you aren't swept away by the current. \nYou reach the other side and knock on the door of the cabin.")
                        cabin(health,trapdoor_check)

                    elif success_chance < 10:
                        health -= 45
                        print(f"You decide to swim across the river. You are about half way across when you hear something burst out of the water behind you. \nYou turn around to see a massive serpent-like sea creature with razor sharp teeth swimming toward you. \nYou begin swimming as fast as you can, lunging for the shoreline. \nJust as you are almost running onto land, the creature lunges for you and takes a small chunk of your leg. Your health is now {health}.")
                        check_gameover(health)
                        print("You hobble onto land and the creature sinks back into the water. You decide to go and knock on the door of the cabin.")
                        cabin(health,trapdoor_check)


                elif decision == "Look in sack":
                    look_in_sack()
                    river(health,trapdoor_check)


                else:
                    print("Please choose one of the specified options.")
                    river(health,trapdoor_check)
#player has already visited this area once
    elif "lucky charm" in sack:
        print("You've already visited this area enough. Choose something else.")
        fork_in_road(health,trapdoor_check)




def end_room(health,trapdoor_check):

    decision = input("You can 'Take the idol', 'Leave the room' or 'Look in sack'. Please make your decision now: ")
    while True:
    
        if decision == "Take the idol":

#user instantly dies if they don't have the lucky charm
            if "lucky charm" not in sack:
                print("You reach for the idol. But as you do, a hand reaches out to stop you. You look in front of you to see a purple tinted transluscent ghost holding your arm. \n'You cannot have my totem,' he says. 'Guards, take him away!' he shouts. \nYou look around to see several ghosts appear from the thin air of the chairs around the table. They seize your other limbs and drag you to an alter that you failed to notice earlier. It is lit with a purple flame. \nYou kick and scream but the last thing you hear from the king is...")
                time.sleep(5)
                print("Goodbye")
                health -= 101
                check_gameover(health)
#makes it so the user has to find the lucky charm to win
            elif "lucky charm" in sack:
                print("You grab the totem and you instantly feel your memories come back to you. \nYou wonder, 'Why am I sitting here playing this game?' \n'Surely there are better ways to spend my time than going on a fictional quest for digital items. You have broken your curse and completed the game.")
                sys.exit()


        elif decision == "Leave the room":
            print("You decide to leave this room for now and go to back.")
            temple(health,trapdoor_check)



        elif decision == "Look in sack":
            look_in_sack()
            end_room(health,trapdoor_check)

        else:
            print("Please choose one of the specified options.")
            end_room(health,trapdoor_check)




def soldier_room(health,trapdoor_check):
    decision = input("Your options are 'Fight' or 'Run'. Please type your decision here: ")
    while True:
        if decision == "Fight":
#user doesn't take damage if they have sword and choose to fight
            if "rusty sword" in sack:
                print("You decide to fight with your sword. You stab soldier after soldier but there are too many. \nYou decide to retreat back the way you came. The soldiers chase you but as you are running back a trap door opens just after you cross it, stranding the soldiers on the other side")
                temple(health,trapdoor_check)

            elif "rusty sword" not in sack:

                health -= 30
                print(f"You decide to fight the soldiers with your bare hands. You attempt a punch only to find out that they are made of clay so your punches are ineffective. \nYou retreat back the way you came. As you are running back, A trap door opens stranding the soldiers on the other side and leaving you back where you came from near the entrance of the temple. \nYou take moderate damage from the encounter and your health is now {health}.")
                check_gameover(health)
                temple(health,trapdoor_check)
    
        elif decision == "Run":

            health -= 20
            print(f"You decide to run away back the way you came, You suffer minor cuts from the swords and your health is now {health}. \nAs you run back a massive trap door opens just after you cross it stranding the guards chasing you on the other side")
            check_gameover(health)
            temple(health,trapdoor_check)


        else:
            print("Please choose one of the specied options")
            soldier_room(health,trapdoor_check)














def temple(health,trapdoor_check):

    decision = input("You may either 'Take a left', 'Take a right', 'Leave temple' or 'Look in sack' \nPlease make your decision now: ")
    while True:
        if decision == "Take a left":
#this if statement should only be true once so the user may only go down the left path once
            if trapdoor_check == 0:
                trapdoor_check += 1
                print("You take a left and you walk into a room full of soldiers made of clay each one carries a sword and is constructed with a different face. \nAs you peer at one, all the soldiers come to life.")
                soldier_room(health,trapdoor_check)
#code for if the user tries to go left twice
            if trapdoor_check != 0:
                print("That way is closed now")
                temple(health,trapdoor_check)


        elif decision == "Take a right":
            print("You take a right inside the temple and you walk into a large room adorned with gold and bright purple cloth lain across tables. \nOn the table there is a golden figure of a child.")
            end_room(health,trapdoor_check)        




        elif decision == "Leave temple":
            print("You decide to run away, out the temple and back to the fork in the road.")
            fork_in_road(health,trapdoor_check)


        elif decision == "Look in sack":
            look_in_sack()
            temple(health,trapdoor_check)

        else:
            print("Please choose one of the specified options")
            temple(health,trapdoor_check)

























def cabin(health,trapdoor_check):
    print("You are greeted by an old man. You tell him that you are looking for a golden idol figure. \nHe tells you to go into the temple, but be warned there are spirits guarding the idol and he gives you lucky charm to wear. \n'Wear this and you will be just fine,' he tells you. \nYou decide to cross the river and head back to the fork in the road.")
    sack.append("lucky charm")
    fork_in_road(health,trapdoor_check)





















def camp(health,trapdoor_check):

    decision = input("You may either 'Turn back to fork in the road', 'Attack the people', 'Peacefully approach' or 'Look in sack' \nPlease make your decision now: ")





    while True:



        if decision == "Turn back to fork in the road":
            print("You decide to head back toward the fork in the road")
            fork_in_road(health,trapdoor_check)

        elif decision == "Look in sack":
            look_in_sack()
            camp(health,trapdoor_check)

        elif decision == "Attack the people":
           
            if "boat" not in sack:
#outcome tree for if user didn't find the rusty sword
                if "rusty sword" not in sack:

                    success_chance = random.randint(1,10)
                    if success_chance > 6:
#40% chance of avoiding taking 45 damage by taking 10
                        health -= 10
                        print(f"You rush out from behind some bushes with nothing but your bare hands. \nYou punch and kick your way through the camp until everyone is unconscious or they've fled. \nFrom the fighting, you take minor injuries and your health is now: {health}.")
                        check_gameover(health)
                        print("You decide to steal a 'boat' and 'torch' from the camp before leaving.")
                        sack.append("torch")
                        sack.append("boat")
                        camp(health,trapdoor_check)

                    elif success_chance <= 6:


                        health -= 45
                        print(f"You attempt to sneak behind the people and steal one of their boats and a torch, but just as you are walking away. \nOne person notices you and screams, 'He's taking our boat!' The people grab their bows and arrows and begin to pepper you with arrows. \nLuckily, all miss except for 1 which pierces your back. You take heavy damage and your health is now {health}.")
                        check_gameover(health)
                        print("You are able to escape with a 'boat' and 'torch'.")
                        sack.append("torch")
                        sack.append("boat")
                        camp(health,trapdoor_check)


# outcome tree for if user found the rusty sword
                if "rusty sword" in sack:
                    success_chance = random.randint(1,10)
                    if success_chance > 2:
                        print("You rush out from behind some bushes with your rusty sword in hand and charge toward the people. \n'Please don't hurt us,' one of them screams. 'We'll give you a torch and this boat if you leave us alone.' \nYou decide to take their offer and you acquire a 'boat' and 'torch' for your collection.")
                        sack.append("torch")
                        sack.append("boat")
                        camp(health,trapdoor_check)


                    elif success_chance <= 2:

#20% chance of player losing health even with the sword
                        health -= 35 
                        print(f"You rush out from behind some bushes with your rusty sword in hand and charge toward the people. \nA man lunches for a club sitting on the ground. He grabs it and swings it at you hitting your stomach and legs. You fight back with your sword and eventually you defeat every person in the camp. \nYou receive moderate injuries from the fight and your health is now: {health}.")
                        check_gameover(health)
                        print("Before you leave you decide to take a 'boat' and 'torch' for your collection.")
                        sack.append("torch")
                        sack.append("boat")
                        camp(health,trapdoor_check)
            elif "boat" in sack:
                print("It's probably best to avoid this area now")
                camp(health,trapdoor_check)




        elif decision == "Peacefully approach":
#used to check if player has already gotten the boat by peace or fighting        
            if "boat" not in sack:
                print("You approach the people saying, 'I come in peace. I am looking for a golden idol statue.' \nThe people tell you, 'You must go to the temple. Take the path you came from and walk until you hit a fork and turn left, but first, please take this torch, it is dark in the temple.' \n'May I borrow that boat?' you ask. 'Sure,' they answer, 'Wouldn't want you to get hurt crossing the river...' You have added a 'boat' and 'torch' to your collection")
                




                sack.append("boat")
                sack.append("torch")
                camp(health,trapdoor_check)


            elif "boat" in sack:
                print("You have gotten all required items")
                camp(health,trapdoor_check)


        else:
            print("Please choose one of the specified options")
            camp(health,trapdoor_check)




















def starting_point(health,trapdoor_check):

    
    decision = input("You may either 'Look in sack' or 'Enter the forest', proceed with your decision here: ")


    if decision == "Enter the forest":
    
        print("You enter the forest and walk into the forest. To your left there is a path that appears to lead to some smoke rising in the distance. \nTo your right you can hear a rushing river. Straight ahead there is a massive pyramid shaped temple.")
        
        fork_in_road(health,trapdoor_check)
        


    elif decision == "Look in sack":
        look_in_sack()
        starting_point(health,trapdoor_check)




#user entered something that wasn't an option
    else:
        print("Please choose one of the specified options")
        starting_point(health,trapdoor_check)
















def fork_in_road(health,trapdoor_check):

    decision = input("You may either 'Enter temple', 'Approach the river', 'Approach the fire', 'Look around', 'Leave the forest' or 'Look in sack'. \nPlease make your decision now: ")

    while True:
        if decision == "Look in sack":
            look_in_sack()
            fork_in_road(health,trapdoor_check)

        elif decision == "Look around":
     
            pick_up_sword()


        elif decision == "Approach the fire":
            print("You decide to approach the fire burning in the distance. When you get close enough, you stumble upon a group of people sitting around a camp fire. \nThey have a small shelter built. You notice a small wooden boat that would be very helpful for crossing the river.")
            camp(health,trapdoor_check)
                




        elif decision == "Approach the river":
            if "lucky charm" not in sack:
                print("You decide to approach the rushing water. You walk down the trail until you see a river and beyond that a small log cabin. \nThe water looks deep and the currents look strong.")
            river(health,trapdoor_check)
            

        elif decision == "Enter temple":

            if "torch" in sack:
                print("You decide to approach the massive temple towering above the trees. Once you arrive, you see a narrow entrance and you go inside")
                temple(health,trapdoor_check)
            elif "torch" not in sack:
                print("You decide to approach the massive temple towering above the trees. Once you arrive, you see a narrow entrance and you go inside. \nIt is too dark to see anything. You run out of the temple back to the fork in the road. If only you had something to brighten the interior...")
                fork_in_road(health,trapdoor_check)
    
#used to force the player to stay in the forest
        elif decision == "Leave the forest":

            print("Just as you are going to leave the forest a giant tree comes to life and swings his branch at you.")
            health -= 10
            print(f"Your health total: {health}")
            check_gameover(health)
            print("You decide to run back into the forest.")
            fork_in_road(health,trapdoor_check)


        elif decision == "dnuora kooL":

            if "Easter egg" not in sack:
                print("You look around and find a strangely painted pastel colored egg.")
                sack.append("Easter egg")
                fork_in_road(health,trapdoor_check)
            else:
                print("Please choose one of the specified options:")
                fork_in_road(health,trapdoor_check)


        else:
            print("Please choose one of the specified options:")
            fork_in_road(health,trapdoor_check)








    



#Starting point of main program


#clears the screen before running
os.system("cls")


 
#opening monologue
print("You awake dazed and confused outside of a forest. All you have with you is an empty sack and the memory of a wizard who stole the rest of your memories \nand hid them in a golden idol statue. You have 100 health.")

starting_point(health,trapdoor_check)
    
















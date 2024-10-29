import sys
import random
from Player import Start
from Monster import Spawn
from Battle import Battle
from Misc import Misc
import random

#Booleans For the 3 loops that are used as a way to make it repeat functions

FirstLoop = True # The First Loop is for the Start and reset/restart of the program ,
                 # The player is given an option to restart there adventure if the player Dies or chooses too
SecondLoop = True # SecondLoop starts the spawning of the Mon and the battle functions
ThirdLoop = True # ThirdLoop is the fight between the player and the Mon
print("_" * 70)
print("Welcome to The Endless Fight")
print("A basic Text Turn-Based Rpg made in Python")
print("The Main goal of this game is to defeat the Demon King Minions")
print("and even the Demon King himself if you get there")
print("_" * 70)
while FirstLoop == True :
     Name = input("Whats you're Name ->")
     M = Misc(Name) # Stores the name in the Misc Class
     M.PrintRoles() # Prints the Names of the Roles  in Misc Class
     Role = M.RoleInput() # Input for the Roles in Misc Class
     print("_" * 70)
     B = Battle(Name, int(Role)) # Gives input to the Battle Class to start the fight
     while SecondLoop == True :
         B.creating() # Spawning the Mon
         while ThirdLoop == True :
             B.PlayerHealthBar() # Spawns the Player's Health bar
             B.Result() # The results of the battle
            
             
             if B.EnemyExit() == False :
                 B.xp()
                 break
             if B.PlayerExit() == False :
                 
                 break             
         if B.PlayerExit() == False :
              break


     ex = input("Do you want to Try Again y/n ->")
     if ex == 'n' :
         break     
#z.Result()
#z.xp()
#z.PlayerHealthBar()
#print(z.Exit())

sys.exit()
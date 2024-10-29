
import random
class Misc:
 #Sets the input name
  def __init__(self, Name):
        self.name = Name
        self.Level = 1
        self.Score = 0
  # The Stat Menu
  def chooseLevel(self , exp):
      loop = True
      print("-" * 70)
      stats=['Health', 'Defence', 'Attack', 'Crit chance', 'Speed']
      print("Where would you like to spend "+str(exp)+" exp on")
      z = 1
      for x in stats:
        print("["+ str(z) +"] "+ str(x))
        z= 1+z
      while loop == True :
         try:
             self.y = input("->") 
             x = int(self.y)
             if x <=0 or x > 5:
                 print("Input is unable")
             else:
                  break
         except:
             print("error wrong input try again !")
      while loop == True :
         try:
            
             self.exp = input("How Many exp points do you want to use here ->")
             x = int(self.exp)
             if x <0 or x > int(exp) :
                 print("Input unaviable")
             else:
                 break
         except:
             print("error wrong input try again !")
      print("-" * 70)
  #the amount of xp choosen
  def choosenxp(self):     
      return self.exp
 #The stat choosen
  def choosen(self):     
      return self.y
 #Prints the Roles that are available for the player
  def PrintRoles(self):

     print("What Role do you want to be")
     role = {1: {'name': 'Hero'},
                2: {'name': 'Warrior'},
                3: {'name': 'Rogue'}
              }
     for x in role:
         print("["+ str(x) +"] "+ str(role[x]['name']))
  def RoleInput(self):
     loop = True
     while loop == True :
        try:
          x = input("->") 
          self.Role = int(x) 
          if self.Role <= 3 and self.Role >= 1 : 

             break
          else:
             print("sorry that option isn't available")
        except:
         print("error wrong input try again !")     
  
     return self.Role
 #Score Function??

 #Set & Get Score,
 #It uses the  defeated Monsters score as the max for the random
  def SetScore(self, x):
      sc = random.randint(1,x)
      self.Score = self.Score + sc
  def GetScore(self):
      return self.Score

 #The Move the Player chooses
 #The loops is if the player chooses an input aside from whats available
  def MoveInput(self):
     loop = True

     while loop == True :
          try:
             x = input("->")
             self.Move = int(x)
             if self.Move <= 4 and self.Move >= 1 :
                 break
             else:
                 print("sorry that option isn't aviable")

          except:
             print("error wrong input try again !")
     return self.Move

#Set & Get for the Lvl
#Its a more of a counter on what Monster can come out rather than
# acual lv for monsters the better term would something like "rounds"
  def SetLvl(self,Lv):
      self.Level= self.Level + Lv
      if self.Level >10:
          self.Level = 10
  def GetLvl(self):
      return self.Level
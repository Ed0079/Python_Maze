from Player import Start
from Monster import Spawn
from Misc import Misc
import random
class Battle:
    def __init__(self, name, num):
        
        #Variables
        self.name = name
        self.role = num
        #starters for Player,and Misc.
        self.P =  Start(self.name)
        self.M = Misc(self.name)
        #Players Functions
        self.P.SetBS(self.role)
        self.M.SetScore(1)
    #The Spawn of the Mon , uses the Monster Class to get the info
    def creating(self):


     self.E = Spawn(self.M.GetLvl())
     self.E.SS()
     self.MR = self.E.Getrole()
     print("-" * 70)
     print(str(self.E.GetName())+" has Spawn")
     print("-" * 70)

    def PlayerHealthBar(self):
      #The Output of the HP of Both
      # Players health
      PlayerHealth = self.P.GetCH()
      PlayerMaxHealth = self.P.GetBH()
      PlayerHealthDashes = 20  # Max Displayed dashes
      PlayerDashConvert = int(PlayerMaxHealth / PlayerHealthDashes)
      PlayerCurrentDashes = int(PlayerHealth / PlayerDashConvert)
      PlayerRemainingHealth = PlayerHealthDashes - PlayerCurrentDashes
      PlayerHealthDisplay = '-' * PlayerCurrentDashes
      PlayerRemainingDisplay = ' ' * PlayerRemainingHealth
      PlayerPercent = str(int((PlayerHealth / PlayerMaxHealth) * 100)) + "%"
      
      #Enemys Health
      EnemyHealth = self.E.GetCH()
      EnemyMaxHealth =self.E.GetBH()
      EnemyDashes =int(EnemyMaxHealth / PlayerHealthDashes)
      EnemyCurrentDashes = int(EnemyHealth / EnemyDashes)
      EnemyRemainingHealth = PlayerHealthDashes - EnemyCurrentDashes      
      EnemyHealthDisplay ="-" * EnemyCurrentDashes    
      EnemyRemainingDisplay =" " * EnemyRemainingHealth
      EnemyPercent = str(int((EnemyHealth / EnemyMaxHealth)* 100)) + "%"
      #outputs
      print('{:>19}'.format( self.P.GetName())+'{:>32}'.format( self.E.GetName()))
      print('{:<30}'.format("|" + PlayerHealthDisplay + PlayerRemainingDisplay + "|")+'{:>30}'.format("|" + EnemyHealthDisplay + EnemyRemainingDisplay + "|"))
      print('{:>13}'.format(PlayerPercent)+'{:>38}'.format(EnemyPercent))

    #The Main Battle body
    def Result(self):
      #input for the moves
      print('What action do you want to take')
      self.P.Move(self.role)
      self.P.PrintMoves()
      PlayerInput = self.M.MoveInput()
      self.P.Choosen(PlayerInput)
      A = self.P.GetMovNum()


      EnemyInput = random.randint(1, 2)
      self.E.Move()
      self.E.Choosen(EnemyInput)

      #Who goes first
      print('=' * 70)
      self.speed()
      print('=' * 70)
     #End result
      if self.P.GetCH() <=0 :
          print(self.P.GetName() + " has been defeated by "+ self.E.GetName())
          print("Final Score : ", self.M.GetScore())
      if self.E.GetCH() <= 0 :
          print(self.E.GetName() + " has been defeated")
          self.M.SetScore(self.E.GetScore())
          print("The Score :" , self.M.GetScore())
          self.E.GetExp()
          self.M.SetLvl(1)
      print('='*70)
   #Check who attacks first
    def speed(self):
        PS = random.randint(0,self.P.GetCS())
        ES = random.randint(0,self.E.GetCS())

        if PS >= ES :
            AP = self.P.attack()
            self.de(AP)

            print(self.name + ' did ' + str(AP) + ' with ' + str(self.P.GetMovName()))
            if self.E.GetCH() > 0 :

                AE = self.E.attack()
                self.dp(AE)

                print(self.E.GetName() + ' did ' + str(AE) + ' with ' + str(self.E.GetMovName()))
        elif ES > PS :
            AE = self.E.attack()
            self.dp(AE)

            print(self.E.GetName() + ' did ' + str(AE) + ' with ' + str(self.E.GetMovName()))
            if  self.P.GetCH() > 0 :
                AP = self.P.attack()
                self.de(AP)

                print(self.name + ' did ' + str(AP) + ' with ' + str(self.P.GetMovName()))

#The defense stuff, damage done = A - D then Current Health =  Health - Damage
    def dp(self, A):
        attack = A - self.P.GetCD()
        if attack < 0:
            attack = 0
        self.P.SetCH(attack)
    def de(self, A):
        attack = A - self.E.GetCD()
        if attack < 0:
            attack = 0
        self.E.SetCH(attack)
    #The select menu for the skills
    def xp (self):
      #Gets the Max xp of the Monster then it rendomizes the xp gained throught the fight
      Exp = random.randint(1 , self.E.GetExp())
      
      
      
      while True :
         self.M.chooseLevel(Exp)
         s = self.M.choosen()
         if s == '1' :
          self.P.SetCH( 0 - int(self.M.choosenxp()))
          Exp = Exp - int(self.M.choosenxp())
          if Exp == 0 :          
             break
         if s == '2' :
          self.P.SetCD( 0 - int(self.M.choosenxp()))
          Exp = Exp - int(self.M.choosenxp())
          if Exp == 0 :          
             break
         if s == '3' :
          self.P.SetCA( 0 - int(self.M.choosenxp()))
          Exp = Exp - int(self.M.choosenxp())
          if Exp == 0 :          
             break
         if s == '4' :
          self.P.SetCC( 0 - int(self.M.choosenxp()))
          Exp = Exp - int(self.M.choosenxp())
          if Exp == 0 :          
             break
         if s == '5' :
          self.P.SetCS( 0 - int(self.M.choosenxp()))
          Exp = Exp - int(self.M.choosenxp())
          if Exp == 0 :          
             break  
    #A very simple Exit for both P & M
    #Basicly if P dies it finishes the game
    def PlayerExit(self):
      if self.P.GetCH() <= 0:
         return False
      else : return True 
        
    def EnemyExit(self):
      if self.E.GetCH() <=0:
         return False
      else : return True   
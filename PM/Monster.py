import random
from Misc import Misc
class Spawn:
    def __init__(self,x):

         self.Id = random.randint(1,x)


#Monster List with the Set & Gets
    def SS(self):
        role = {1: {'name': 'Rat', 'health': 20, 'Defence': 5, 'attack': 5, 'speed': 20, 'crit': 5, 'exp' : 5, 'score' : 10},
                2: {'name': "Goblin", 'health': 30, 'Defence': 5, 'attack': 15, 'speed': 15, 'crit': 5, 'exp' : 10, 'score' : 15},
                3: {'name': "Skeleton", 'health': 45, 'Defence': 3, 'attack': 18, 'speed': 20, 'crit': 10, 'exp' : 15, 'score' : 15},
                4: {'name': "Undead", 'health': 50, 'Defence': 5, 'attack': 13, 'speed': 12, 'crit': 5, 'exp' : 15, 'score' : 20},
                5: {'name': "Ghost", 'health': 35, 'Defence': 0, 'attack': 20, 'speed': 22, 'crit': 10, 'exp' : 30 , 'score' : 25},
                6: {'name': "Griffons", 'health': 65, 'Defence': 15, 'attack': 15, 'speed': 20, 'crit': 20, 'exp' : 100, 'score' : 100},
                7: {'name': "Minotaur", 'health': 75, 'Defence': 20, 'attack': 25, 'speed': 5, 'crit': 10, 'exp' : 150 , 'score' : 250},
                8: {'name': "Turtle", 'health': 100, 'Defence': 45, 'attack': 20, 'speed': 3, 'crit': 50, 'exp': 200, 'score' : 450},
                9: {'name': "Tonberry", 'health': 50, 'Defence': 10, 'attack': 25, 'speed': 85, 'crit':95, 'exp': 500, 'score' : 500},
                10: {'name': "Demon King", 'health': 200, 'Defence': 50, 'attack': 40, 'speed': 35, 'crit': 45, 'exp': 1000, 'score' : 10000}

              }
        self.name = role[self.Id]['name']
        self.BH = role[self.Id]['health']
        self.BD = role[self.Id]['Defence']
        self.BA = role[self.Id]['attack']
        self.BS =role[self.Id]['speed']
        self.BC =role[self.Id]['crit']
        self.score =role[self.Id]['score']

        self.CH = self.BH
        self.CD = self.BD
        self.CA = self.BA
        self.CS = self.BS
        self.CC = self.BC
        self.role=  self.Id
        self.exp = role[self.Id]['exp']
#Monsters Move list
    def Move(self):
        self.EnemyMoves ={
              1:{
                   1:{'name' :'Bite','attack': 7},
                   2:{'name' :'Throw shit','attack': 8},
                },
               2:{
                   1:{'name' :'Slash','attack': 10},
                   2:{'name' :'Throw Rock','attack': 7}
                },
               3:{
                   1:{'name' :'Slash','attack': 7},
                   2:{'name' :'Combo Attack','attack': 10}

                },
               4: {
                   1: {'name': 'Bite', 'attack': 7},
                   2: {'name': 'Slash', 'attack': 8},
                },
               5: {
                   1: {'name': 'Scare', 'attack': 10},
                   2: {'name': 'Throw Plasma', 'attack': 10}
                },

               6: {
                   1: {'name': 'Air Blast', 'attack': 10},
                   2: {'name': 'Claw Slash', 'attack': 15}

               },
              7: {
                  1: {'name': 'Smash', 'attack': 10},
                  2: {'name': 'Yeet', 'attack': 15}
              },
              8: {
                 1: {'name': 'Shield Bash', 'attack': 10},
                 2: {'name': 'Water Gun', 'attack': 20}
              },
              9: {
                 1: {'name': 'Stab', 'attack': 10},
                 2: {'name': 'Back Stab', 'attack': 20}

              },
              10: {
                 1: {'name': 'Victory Slash', 'attack': 25},
                 2: {'name': 'Demonic Blast', 'attack': 30}

              }
      }

#Set & Gets
    def GetName(self):
        return self.name

    def GetBH(self):
        return self.BH

    def GetBD(self):
        return self.BD

    def GetBA(self):
        return self.BA

    def SetCH(self ,D):
        self.CH= self.CH - D
    def GetCH(self):
        return self.CH

    def SetCD(self, S):
        self.CD = self.CD - S
    def GetCD(self):
     return self.CD

    def SetCA(self, S):
        self.CA = self.CA - S
    def GetCA(self):
     return self.CA
     
    def Getrole(self):
        return self.role
        
    def SetCA(self, S):
        self.CA = self.CA - S
    def GetCA(self):
     return self.CA
     
    def SetCS(self, S):
        self.CA = self.CS - S
    def GetCS(self):
     return self.CS
    
    def SetCC(self, S):
        self.CA = self.CC - S
    def GetCC(self):
     return self.CC 
    
    def GetExp(self):
     return self.exp
#A Set for the monsters choosen moves
    def Choosen(self, i):
        self.MovName = self.EnemyMoves[self.Id][i]['name']
        self.MovNum = self.EnemyMoves[self.Id][i]['attack']
#The Gets for the moves
    def GetMovName(self):
        return self.MovName

    def GetMovNum(self):
        return self.MovNum
#The Attack function
#Gets the Moves damage to uses as a min and the Monsters Basic attack as the Max to give a final attack num
#Then it checks if its a crit and if it passes the basic check then the attack is doubled
# Random = Movnum (min), BA(max) then
    # if C >= sys then Random * 2
    def attack (self):
        self.a = random.randint(self.MovNum, self.GetCA())
        chance = random.randint(1, self.BC)
        sys = random.randint(1, 100)
        if chance >= sys:

            self.a = self.a * 2
        return  self.a

    def GetScore(self):
        return self.score
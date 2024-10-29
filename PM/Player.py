from Monster import Spawn
import random
class Start:

    def __init__(self,Nam):
        self.name= Nam



# The basic set stats for each Role
    def SetBS(self, Num):
      role = {1: {'name': ' the Hero', 'health': 100, 'Defence': 5, 'attack': 40, 'speed': 20, 'crit': 10},
                2: {'name': ' the Warrior', 'health': 200, 'Defence': 10, 'attack': 20, 'speed': 15, 'crit': 5},
                3: {'name': ' the Rogue', 'health': 75, 'Defence': 2, 'attack': 30, 'speed': 50, 'crit': 10}         
              }
      self.role = Num
      self.name = self.name + role[Num]['name']
      self.BH = role[Num]['health']
      self.BD = role[Num]['Defence']
      self.BA = role[Num]['attack']
      self.BS =role[Num]['speed']
      self.BC =role[Num]['crit']
      self.CH = self.BH
      self.CD = self.BD
      self.CA = self.BA
      self.CS = self.BS
      self.CC = self.BC
#List of the moves for each Class
    def Move(self,i):
        self.PlayerMoves = {1: {1: {'name': 'Slash', 'attack': 5},
                           2: {'name': 'Kick', 'attack': 10},
                           3: {'name': 'Bash', 'attack': 15},
                           4: {'name': 'Blazing Slash', 'attack': 17}

                           },
                       2: {
                           1: {'name': 'Slash', 'attack': 10},
                           2: {'name': 'Throw Rock', 'attack': 7},
                           3: {'name': 'Uppercut', 'attack': 15},
                           4: {'name': 'Furry of Thor', 'attack': 20}

                       },
                       3: {
                           1: {'name': 'Slash', 'attack': 5},
                           2: {'name': 'Steal', 'attack': 7},
                           3: {'name': 'Back stab', 'attack': 10},
                           4: {'name': 'Night Dance', 'attack': 15}

                       }
        }
#Outputs the moves available for the class
    def PrintMoves(self):

        for x in self.PlayerMoves[self.role]:
            print("[" + str(x) + "] " + str(self.PlayerMoves[self.role][x]['name']) + "-" + str(
                self.PlayerMoves[self.role][x]['attack']))
    #Gets
    def GetName(self):
        return self.name
    def GetBH(self):
        return self.BH
    def GetBD(self):
        return self.BD
    def GetBA(self):
        return self.BA
    def GetCH(self):
        return self.CH
    def GetCD(self):
     return self.CD
    def GetCA(self):
        return self.CA
    def GetCS(self):
        return self.CS
    def GetCC(self):
        return self.CC

    def GetMovName(self):
        return self.MovName
    def GetMovNum(self):
        return self.MovNum
#Sets
    def SetCH(self ,D):
        self.CH= self.CH - D
    def SetCD(self, S):
        self.CD = self.CD - S
    def SetCA(self, S):
        self.CA = self.CA - S

    def SetCS(self, S):
        self.CA = self.CS - S

    def SetCC(self, S):
        self.CA = self.CC - S

#The Set for the current move that was choosen
    def Choosen(self,i):
        self.MovName = self.PlayerMoves[self.role][i]['name']
        self.MovNum = self.PlayerMoves[self.role][i]['attack']
#The Attack function
#Gets the Moves damage to uses as a min and the Monsters Basic attack as the Max to give a final attack num
#Then it checks if its a crit and if it passes the basic check then the attack is doubled
# Random = Movnum (min), BA(max) then
    # if C >= sys then Random * 2
    def attack (self):
        self.a = random.randint(self.MovNum, self.CA)
        chance = random.randint(0, self.CC)
        sys = random.randint(0, 100)
        if chance >= sys :

            self.a= self.a*2
        return  self.a



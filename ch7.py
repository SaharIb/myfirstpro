#Q1
'''import random
class PairOfDice:
    def __init__(self):
       self._redDie = 0
       self._blueDie = 0 
    def getRedDie(self):
      return self._redDie
    def getBlueDie(self):
      return self._blueDie
    def roll(self): 
     self._redDie = random.choice(range(1, 7))
     self._blueDie = random.choice(range(1, 7)) 
    def sum(self):
      return self._redDie + self._blueDie
    def compare (self):
      if self._redDie > self._blueDie : return f"p1 ia won {self._redDie} " 
      else : return f"p2 is won {self._blueDie}"     
color = PairOfDice()
color._redDie = int(input("Enter red "))
color._blueDie = int(input("Enter blue "))
print(color.sum())
print(color.compare())'''
#Q2
import pCard 
c = pCard.PlayingCard()
#print(c.getRank())
c.selectAtRandom()
print(c._rank)
print(c._suit)




from random import randint as rd

class RandomIgralec3:
   def __init__(self, coin_type):
      self.name = "random"
      self.coin_type = coin_type
      self.win = 0
      self.lose = 0
      self.draw = 0

   def narediPotezo(self, polje):
      return rd(0,polje.w*polje.h-1)
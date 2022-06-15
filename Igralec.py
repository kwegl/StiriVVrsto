import pygame

class Igralec:
   def __init__(self,coin_type):
      self.name = "človek"
      self.click = False
      self.coin_type = coin_type
      self.win = 0
      self.lose = 0
      self.draw = 0

   def narediPotezo(self, polje):
      if(pygame.mouse.get_pressed()[0] == 1):
         if self.click==False:
            self.click = True
            mx, my = pygame.mouse.get_pos()
            return mx//polje.size
      else:
         self.click = False
      return
import pygame

class Polje3:
   def __init__(self, win, W):
      self.win = win
      self.w = 3
      self.h = 3
      self.size = W//self.w
      self.polje = [[0 for i in range(self.h)] for i in range(self.w)]
      self.prev_polje = self.polje
      self.naVrsti = 1
      self.stPotez = 0
      

   def narišiMrežo(self):
      for i in range(self.h+1):
         pygame.draw.line(self.win, (0,0,0), (0, i*self.size), (self.w*self.size, i*self.size))
      for i in range(self.w+1):
         pygame.draw.line(self.win, (0,0,0), (i*self.size, 0), (i*self.size, self.h*self.size))

   def narišiKrogce(self):
      for i in range(self.w):
         for k in range(self.h):
            if(self.polje[i][k] == 1):
               pygame.draw.circle(self.win, (200,50,0), (i*self.size+self.size//2, k*self.size+self.size//2), self.size//2)
            elif(self.polje[i][k] == 2):
               pygame.draw.circle(self.win, (0,150,100), (i*self.size+self.size//2, k*self.size+self.size//2), self.size//2)

   def reset(self):
      self.polje = [[0 for i in range(self.h)] for i in range(self.w)]

   def get_actions(self):
      actions = []
      for i in range(self.w):
         for k in range(self.h):
            if(self.polje[i][k] == 0):
               actions.append(i+k*3)
      return actions

   def poteza(self, poteza, igralec):
      if(poteza == None):
         return 0
      k = poteza//3
      i = poteza-k*3
      if(self.polje[i][k] == 0):
         self.prev_polje = self.polje
         self.polje[i][k] = igralec.coin_type
         self.stPotez += 1
         return 3
      return 0

   def get_state(self):
      return tuple(tuple(x) for x in self.polje)

   def get_prev_state(self):
      return tuple(tuple(x) for x in self.prev_polje)

   def zmagovalec(self):

      for i in range(self.w):
         if(self.polje[i][0]==self.polje[i][1] and self.polje[i][1]==self.polje[i][2] and self.polje[i][0]!=0):
            return abs(self.naVrsti-3)
         if(self.polje[0][i]==self.polje[1][i] and self.polje[1][i]==self.polje[2][i] and self.polje[0][i]!=0):
            return abs(self.naVrsti-3)

      if(self.polje[0][0]==self.polje[1][1] and self.polje[1][1]==self.polje[2][2] and self.polje[0][0]!=0):
            return abs(self.naVrsti-3)
      if(self.polje[2][0]==self.polje[1][1] and self.polje[1][1]==self.polje[0][2] and self.polje[2][0]!=0):
            return abs(self.naVrsti-3)

      st = 0
      for i in range(self.w):
         for k in range(self.h):
            if(self.polje[i][k]==0):
               break
            else:
               st+=1
      if(st==self.w*self.h):
         return 0

import pygame

class Polje:
   def __init__(self, win, W):
      self.win = win
      self.w = 7
      self.h = 6
      self.size = W//self.w
      self.polje = [[0 for i in range(self.h+1)] for i in range(self.w+1)]
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
      self.polje = [[0 for i in range(self.h+1)] for i in range(self.w+1)]

   def get_actions(self):
      actions = []
      for i in range(self.w):
         if(self.polje[i][0] == 0):
            actions.append(i)
      return actions

   def poteza(self, stolpec, igralec):
      if(stolpec == None):
         return 0
      for i in range(1,self.h+1):
         if(self.polje[stolpec][self.h-i] == 0):
            self.prev_polje = self.polje
            self.polje[stolpec][self.h-i] = igralec.coin_type
            self.stPotez += 1
            return 3
      return 0

   def get_state(self):
      return tuple(tuple(x) for x in self.polje)

   def get_prev_state(self):
      return tuple(tuple(x) for x in self.prev_polje)

   def zmagovalec(self):
      
      for i in range(self.w-3):
         for k in range(self.h):
            if(not(self.polje[i][k]==0 or self.polje[i+1][k]==0 or self.polje[i+2][k]==0 or self.polje[i+3][k]==0)):
               if(self.polje[i][k] == self.polje[i+1][k] and self.polje[i+1][k]==self.polje[i+2][k] and self.polje[i+2][k]==self.polje[i+3][k]):# preverjanje vrstic
                  return abs(self.naVrsti-3)

      for i in range(self.w):
         for k in range(self.h-3):
            if(not(self.polje[i][k]==0 or self.polje[i][k+1]==0 or self.polje[i][k+2]==0 or self.polje[i][k+3]==0)):
               if(self.polje[i][k] == self.polje[i][k+1] and self.polje[i][k+1]==self.polje[i][k+2] and self.polje[i][k+2]==self.polje[i][k+3]):# preverjanje stolpcev
                  return abs(self.naVrsti-3)

      for i in range(self.w-3):
         for k in range(self.h-3):
            if(not(self.polje[i][k]==0 or self.polje[i+1][k+1]==0 or self.polje[i+2][k+2]==0 or self.polje[i+3][k+3]==0)):
               if(self.polje[i][k] == self.polje[i+1][k+1] and self.polje[i+1][k+1]==self.polje[i+2][k+2] and self.polje[i+2][k+2]==self.polje[i+3][k+3]):# preverjanje diagonale(levo zgoraj proti desno spodaj)
                  return abs(self.naVrsti-3)
      
      for i in range(self.w-3):
         i = self.w-i-1
         for k in range(self.h-3):
            if(not(self.polje[i][k]==0 or self.polje[i-1][k+1]==0 or self.polje[i-2][k+2]==0 or self.polje[i-3][k+3]==0)):
               if(self.polje[i][k] == self.polje[i-1][k+1] and self.polje[i-1][k+1]==self.polje[i-2][k+2] and self.polje[i-2][k+2]==self.polje[i-3][k+3]):# preverjanje diagonale(desno zgoraj proti levo spodaj)
                  return abs(self.naVrsti-3)

      for i in range(self.w):
         if(self.polje[i][0]==0):
            break
      if(i==self.w-1):
         return 0

      if(self.stPotez == self.w*self.h):
         return 0 # remi

   def preveri_3_v_vrsto(self, coin):
      for i in range(self.w-2):
         for k in range(self.h):
            if(self.polje[i][k] == coin and self.polje[i+1][k]==coin and self.polje[i+2][k]==coin):# preverjanje vrstic
               return True

      for i in range(self.w):
         for k in range(self.h-2):
            if(self.polje[i][k] == coin and self.polje[i][k+1]==coin and self.polje[i][k+2]==coin):# preverjanje stolpcev
               return True

      for i in range(self.w-2):
         for k in range(self.h-2):
            if(self.polje[i][k] == coin and self.polje[i+1][k+1]==coin and self.polje[i+2][k+2]==coin):# preverjanje diagonale(levo zgoraj proti desno spodaj)
               return True
      
      for i in range(self.w-2):
         i = self.w-i-1
         for k in range(self.h-2):
            if(self.polje[i][k] == coin and self.polje[i-1][k+1]==coin and self.polje[i-2][k+2]==coin):# preverjanje diagonale(desno zgoraj proti levo spodaj)
               return True

      return False
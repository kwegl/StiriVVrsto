import pygame
from Polje import Polje
from RandomIgralec import RandomIgralec
from Igralec import Igralec
#from AI import AI
from AIpickle import AI

from Polje3 import Polje3
from RandomIgralec3 import RandomIgralec3

squareSize = 50
W = 3*squareSize
H = 3*squareSize
win = pygame.display.set_mode((W,H))
clock = pygame.time.Clock()

def redraw(polje, igralca):
   win.fill((200,200,200))
   polje.narišiMrežo()
   x = igralca[polje.naVrsti-1].narediPotezo(polje)
   polje.naVrsti = abs(polje.naVrsti-polje.poteza(x, igralca[polje.naVrsti-1]))
   polje.narišiKrogce()
   pygame.display.update()


def main(stIger):
   polje = Polje3(win, W)
   igralec1 = AI(1, 'q.pickle')
   igralec2 = AI(2, 'q.pickle')
   igralca = (igralec1, igralec2)
   st = 0

   run = True
   while run and st<stIger:

      events = pygame.event.get()
      for event in events:
         if event.type == pygame.QUIT:
            run = False

      redraw(polje, igralca)
      zmagovalec = polje.zmagovalec()
      if(zmagovalec!=None):
         if zmagovalec==0:
            igralca[0].draw+=1
            igralca[1].draw+=1
         if zmagovalec==1:
            igralca[0].win+=1
            igralca[1].lose+=1
         if zmagovalec==2:
            igralca[0].lose+=1
            igralca[1].win+=1

         polje.reset()
         temp = igralca[0]
         temp1 = igralca[1]
         igralca = (temp1, temp)
         st+=1
         print(st)
      clock.tick(10000000)

   print("       win draw lose")
   if(igralca[0].name=="AI"):
      igralca[0].shrani()
      print(igralca[0].name+"    ", igralca[0].win," ", igralca[0].draw," ", igralca[0].lose," ")
      print(igralca[0].pametnaPoteza, igralca[0].randpoteza)
   else:
      print(igralca[0].name, igralca[0].win," ", igralca[0].draw," ", igralca[0].lose," ")
   if(igralca[1].name=="AI"):
      igralca[1].shrani()
      print(igralca[1].name+"    ", igralca[1].win," ", igralca[1].draw," ", igralca[1].lose," ")
      print(igralca[1].pametnaPoteza, igralca[1].randpoteza)
   else:
      print(igralca[1].name, igralca[1].win," ", igralca[1].draw," ", igralca[1].lose," ")

def train(display, stIger, epsilon, alpha, gamma):
   polje = Polje3(win, W)
   igralec1 = AI(1, 'q.pickle', epsilon, alpha, gamma)
   igralec2 = RandomIgralec3(2)
   igralca = (igralec1, igralec2)
   st = 0

   run = True
   while run and st<stIger:
      events = pygame.event.get()
      
      x = igralca[polje.naVrsti-1].narediPotezo(polje)
      
      polje.naVrsti = abs(polje.naVrsti-polje.poteza(x, igralca[polje.naVrsti-1]))

      zmagovalec = polje.zmagovalec()
      if zmagovalec==None:
         if igralca[polje.naVrsti-1].name == "AI":
            igralca[polje.naVrsti-1].learn(polje, x)
      
      else:
         if zmagovalec==0:
            igralca[0].draw+=1
            igralca[1].draw+=1
         if zmagovalec==1:
            igralca[0].win+=1
            igralca[1].lose+=1
         if zmagovalec==2:
            igralca[0].lose+=1
            igralca[1].win+=1

         polje.reset()
         if(st%stIger/5==0):
            if(igralca[0].name=="AI"):
               igralca[0].epsilon-=0.1
               if(igralca[0].epsilon<0):
                  igralca[0].epsilon=0
            elif(igralca[1].name=="AI"):
               igralca[1].epsilon-=0.1
               if(igralca[1].epsilon<0):
                  igralca[1].epsilon=0
         #temp = igralca[0]
         #temp1 = igralca[1]
         #igralca = (temp1, temp)
         st+=1
         print(st)

      if display:
         win.fill((200,200,200))
         polje.narišiMrežo()
         polje.narišiKrogce()
         pygame.display.update()

      clock.tick(1000000)
      
      for event in events:
         if event.type == pygame.QUIT:
            run = False

   print("       win draw lose")
   if(igralca[0].name=="AI"):
      igralca[0].shrani()
      print(igralca[0].name+"    ", igralca[0].win," ", igralca[0].draw," ", igralca[0].lose," ")
      print(igralca[0].pametnaPoteza, igralca[0].randpoteza)
   else:
      print(igralca[0].name, igralca[0].win," ", igralca[0].draw," ", igralca[0].lose," ")
   if(igralca[1].name=="AI"):
      igralca[1].shrani()
      print(igralca[1].name+"    ", igralca[1].win," ", igralca[1].draw," ", igralca[1].lose," ")
      print(igralca[1].pametnaPoteza, igralca[1].randpoteza)
   else:
      print(igralca[1].name, igralca[1].win," ", igralca[1].draw," ", igralca[1].lose," ")

train(False, 2000000, 0.7, 0.4, 1)
main(100)
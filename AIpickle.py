import random
from time import sleep
import pickle


class AI:
   def __init__(self, coin_type, brain=None, epsilon=0, alpha=0.5, gamma=0.2):
      # epsilon(0-1)-probability of trying random moves
      # alpha(0-1)-learning rate
      # gamma(0-1)-0-immediate reward
      self.q = {}
      try:
         with open(brain, "rb") as f:
            self.q = pickle.load(f)
      
      except:
         self.q={}
         print("no brain file")
      self.brain = brain

      self.name = "AI"
      self.epsilon = epsilon
      self.alpha = alpha
      self.gamma = gamma
      self.coin_type = coin_type

      self.win = 0
      self.lose = 0
      self.draw = 0

      self.randpoteza = 0
      self.pametnaPoteza = 0

   def getQ(self, state, action):
      """
      Return a probability for a given state and action where the greater
      the probability the better the move
      """
      # encourage exploration; "optimistic" 1.0 initial values
      if self.q.get((state, action)) is None:
         self.q[(state, action)] = 1.0
      return self.q.get((state, action))

   def narediPotezo(self, polje):
      """
      Return an action based on the best move recommendation by the current
      Q-Table with a epsilon chance of trying out a new move
      """
      current_state = polje.get_state()
      actions = polje.get_actions()
      if random.random() < self.epsilon: # explore!
         chosen_action = random.choice(actions)
         self.randpoteza+=1
         return chosen_action
      self.pametnaPoteza+=1
      qs = [self.getQ(current_state, a) for a in actions]
      maxQ = max(qs)

      if qs.count(maxQ) > 1:
         # more than 1 best option; choose among them randomly
         best_options = [i for i in range(len(actions)) if qs[i] == maxQ]
         i = random.choice(best_options)
      else:
         i = qs.index(maxQ)

      return actions[i]

   def learn(self, polje, chosen_action):
      """
      Determine the reward based on its current chosen action and update
      the Q table using the reward recieved and the maximum future reward
      based on the resulting state due to the chosen action
      """
      zmagovalec = polje.zmagovalec()
      reward = 0
      if (zmagovalec!=None):
         if zmagovalec == 0:
            reward = 0
         elif zmagovalec == self.coin_type:
            reward = 10
         else:
            reward = -10
      prev_state = polje.get_prev_state()
      prev = self.getQ(prev_state, chosen_action)
      result_state = polje.get_state()
      maxqnew = max([self.getQ(result_state, a) for a in polje.get_actions()])
      self.q[(prev_state, chosen_action)] = (1-self.alpha)*prev + self.alpha * ((reward + self.gamma*maxqnew))

   def shrani(self):
      with open(self.brain, "wb") as f:
         pickle.dump(self.q, f, protocol=pickle.HIGHEST_PROTOCOL)

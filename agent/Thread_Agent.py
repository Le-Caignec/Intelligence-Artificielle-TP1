import threading
from threading import *
from time import *

class Thread_Agent(Thread):

    def __init__(self, agent, time_break, sizeMentalState):
        Thread.__init__(self)
        self.agent = agent
        self.time_break = time_break
        self.sizeMentalState = sizeMentalState
        self.bool = False

    #Function that is run when the Thread Agent is start
    def run(self):
        while True:
            if self.bool:
                # Get lock to synchronize threads
                threadLock = threading.Lock()
                threadLock.acquire()

                if self.agent.captor.Detect_New_Env():
                    self.agent.objectif = self.agent.Search_Objective()
                    self.agent.plan_action = self.agent.ChoiceAlgo(self.sizeMentalState)
                    print("---------Plan d'action-------------")
                    print(self.agent.plan_action)
                    self.agent.UpdateMentalState()
                    self.agent.Action()
                    self.agent.Deplacement()
                    self.agent.Action()
                else:
                    self.agent.Deplacement()
                    self.agent.Action()

                # Free lock to release next thread
                threadLock.release()
            self.bool = True
            # Temps d'attente entre les threads afin de mettre à jour l'interface graphique
            sleep(self.time_break)

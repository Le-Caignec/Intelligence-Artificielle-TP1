import threading
from threading import *
from time import *

class Thread_Agent(Thread):

    def __init__(self, agent, time_break, sizeMentalState):
        Thread.__init__(self)
        self.agent = agent
        self.time_break = time_break
        self.sizeMentalState = sizeMentalState

    #Fonction lancée lorsque le thread est start()
    def run(self):
        while True:
            # Get lock to synchronize threads
            threadLock = threading.Lock()
            threadLock.acquire()

            #check if the environnment changed <=> self.agent.objectif == self.agent.Search_Objective()
            if self.agent.captor.Detect_New_Env:
                self.agent.objectif = self.agent.Search_Objective()
                self.agent.Action()
                self.agent.plan_action = self.agent.ChoiceAlgo(self.sizeMentalState)
                self.agent.UpdateMentalState()
                self.agent.Deplacement()
                self.agent.Action()
            else:
                self.agent.Deplacement()
                self.agent.Action()

            # Free lock to release next thread
            threadLock.release()

            # Temps d'attente entre les threads afin de mettre à jour l'intercade graphique
            sleep(self.time_break)






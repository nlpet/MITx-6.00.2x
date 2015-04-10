# 6.00.2x Problem Set 4

import numpy
import random
import pylab
from ps3b import *

#
# PROBLEM 1
#        
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    
    timeSteps = 150
    delay = 300
    numViruses = 100
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.1 
    resistances = {'guttagonol': False}
    mutProb = 0.005
    
    population = [[] for t in range(delay)]
    resistantPopulation = [[] for t in range(timeSteps)]
    
    for trial in range(numTrials):
      viruses = [ResistantVirus(maxBirthProb, clearProb, resistances, mutProb) for _ in range(numViruses)]
      patient = TreatedPatient(viruses, maxPop)
      virusPopulation = []
      for delay in range(delay):
        population[delay].append(patient.update())
        
    patient.addPrescription("guttagonol")
    resistances['guttagonol'] = True
        
    for trial in range(numTrials):
      viruses = [ResistantVirus(maxBirthProb, clearProb, resistances, mutProb) for _ in range(numViruses)]
      patient = TreatedPatient(viruses, maxPop)
      virusPopulation = []
      for timeStep in range(timeSteps):
        resistantPopulation[timeStep].append(patient.update())     
        
        
    #print 'non-resistant before avg',population
    #print 'resistant before avg',resistantPopulation

    avgPopulation = [sum(pp) / float(len(pp)) for pp in population]
    avgResistantPopulation = [sum(pp) / float(len(pp)) for pp in resistantPopulation]
    
    #print len(avgPopulation),len(avgResistantPopulation)
    #print 'non-resistant',avgPopulation
    #print 'resistant',avgResistantPopulation    
    
    pylab.plot(avgPopulation)
    pylab.plot(avgResistantPopulation)
    pylab.title("ResistantVirus simulation")
    pylab.xlabel("time Step")
    pylab.ylabel("# viruses")
    pylab.legend(("Non-resistant virus","Resistant virus"))
    pylab.show()
    
          
simulationDelayedTreatment(100)  






#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    # TODO

    

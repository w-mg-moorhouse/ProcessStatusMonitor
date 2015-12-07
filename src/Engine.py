'''
Created on 26 May 2015

@author: will
'''
from src.Action import *
from src.ManageProcess import *
from src.TimeoutCalculator import *
from src.configuration.configLoader import * 
import logging
from src.TransmissionStatus import *
from src.ActiveLogin import *

class Engine(object):
    '''
    classdocs
    '''
    configuration = None

    def __init__(self):
        try:
            self.configuration = configurationLoader.loadConfiguration("resources/wands.json")
            self.timeout = TimeoutCalculator(self.configuration.getGlobalTimeout())
            self.transStat = TransmissionStatus()
            self.activeLogins = ActiveLogin()
            self.timeout.start()
            self.manageProcess = ManageProcess()
            for proc in self.configuration.getProcesses():
                self.manageProcess.addToProcessList(proc)
        except (IOError) as e:
            logging.exception("IOERROR occurred during configuration processing.", e)
        
    def run(self):
        #could be more generic
        if self.activeLogins.areLoginsActive() == False:
            self.timeout.reset()
            return
        if self.transStat.checkQueueForCompletion() == False:
            self.timeout.reset()
            return
        if self.manageProcess.processesActive():
            self.timeout.reset()
            return
        if self.timeout.amITimedOut() == False:
            return
        logging.info("Triggering action")
        Action.action()
# static creation of engine
@staticmethod
def executingFunction():
    if executingFunction.engine == None:
        executingFunction.engine = Engine()
    executingFunction.engine.run()
executingFunction.engine = None

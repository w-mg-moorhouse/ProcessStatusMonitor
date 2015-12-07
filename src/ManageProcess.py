'''
Created on 26 May 2015

@author: will
'''
import logging
import psutil

class ManageProcess(object):
    '''
    classdocs
    '''
    


    def __init__(self):
        self.username = []
        '''
        Constructor
        '''
    def addToProcessList(self, username):
        self.username.append(username)
        pass
    
    def processesActive(self):
        for proc in psutil.process_iter():
            if proc.username() in self.username:
                status = proc.status()
                if status == psutil.STATUS_RUNNING:
                    logging.debug("Process"  + self.username + " active")
                    return True
        logging.debug("No indicated processes are running")
        return False  

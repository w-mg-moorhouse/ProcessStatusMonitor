'''
Created on 28 May 2015

@author: will
'''

import logging

class GlobalConfiguration(object):
    '''
    classdocs
    '''


    def __init__(self, process, globalTimeout=300, loglevel=10):
        self.globalTimeout = globalTimeout
        logging.basicConfig(level=loglevel)
        self.globalLoglevel = loglevel
        self.processes = process['username']
    
    def getProcesses(self):
        return self.processes
    
    def getGlobalTimeout(self):
        return self.globalTimeout
    
    

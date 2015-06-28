'''
Created on 26 May 2015

@author: will
'''

import time

import daemon
import logging

class DaemonProcess(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
    
    def runAsDaemon(self, function, timeout=60):
        with daemon.DaemonContext():
            self.__run(timeout, function) 
    
    def runAsCurrentProcess(self, function, timeout=60):
        self.__run(timeout, function)
    
    def __run(self, timeout, execFunc):
        try:
            while True:
                execFunc()
                logging.debug("Sleeping!")
                print("sleeping")
                time.sleep(timeout)
        
        except (Exception) as e:
            logging.exception("", e)
            print("Something horrible happened, should be in the log")
    
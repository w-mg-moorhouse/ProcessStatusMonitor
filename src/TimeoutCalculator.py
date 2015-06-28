'''
Created on 26 May 2015

@author: will
'''
import time
import logging
import calendar

class TimeoutCalculator(object):
    '''
    classdocs
    '''

    def __init__(self, timeout):
        self.timeout = timeout
        '''
        Constructor
        '''
    
    def start(self):
        self.startTime = calendar.timegm(time.gmtime())
    
    def reset(self):
        self.start()
    
    def amITimedOut(self):
        endTime = (self.startTime + self.timeout)
        presentTime = calendar.timegm(time.gmtime())
        logging.debug("End time calculated as:" + str(endTime))
        if presentTime > endTime:
            logging.info("Timeout Calculator: Timed out")
            return True
        else:
            logging.info("Timeout Calculator: Not Timed out")
            return False
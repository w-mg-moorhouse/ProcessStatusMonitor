'''
Created on 20 Sep 2015

@author: will
'''
import subprocess
import logging

class ActiveLogin(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
    
    def areLoginsActive(self):
        output = subprocess.getoutput("who")
        logins = [s.strip() for s in output.splitlines()]
        if len(logins) > 0:
            for l in logins:
                logging.info("Active Logins:" + l)
            return True
        logging.info("No Active logins")
        return False
        
        
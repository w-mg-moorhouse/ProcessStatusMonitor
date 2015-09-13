'''
Created on 14 Jul 2015

@author: will
'''
import transmissionrpc

class TransmissionStatus(object):
    '''
    classdocs
    '''


    def __init__(self, ip='localhost', port=9091):
        self.ip = ip
        self.port = port
        '''
        Constructor
        '''
    
    def checkQueueForCompletion(self):
        tc = transmissionrpc.Client(self.ip, port=self.port)
        torrents = tc.get_torrents()
        #toRemove = []
        state = True
        for key, value in torrents.items():
            if (value.status is "seeding") or (value.status is "stopped"):
                #toRemove.append(value.hashString)
                tc.stop_torrent(key)
            else:
                state = False
        return state
        #ßtc.remove_torrent(toRemove)

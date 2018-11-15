'''
Created on 16 Nov 2018

@author: Lyrete
'''

import datetime;

class Game(object):

    def __init__(self, goalsFor, goalsAgainst):
        self.goalsFor = goalsFor;
        self.goalsAgainst = goalsAgainst;
        self.date = datetime.datetime.now();
        
    def makeResult(self):
        if(self.goalsFor > self.goalsAgainst):
            self.result = "W"
        elif(self.goalsFor < self.goalsAgaint):
            self.result = "L"
        else:
            self.result = "D"
        
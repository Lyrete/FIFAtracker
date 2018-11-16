'''
Created on 16 Nov 2018

@author: Lyrete
'''
from game import Game;

class dataHandler():
    


    def __init__(self):
        self.dbName = "gameData.csv"
        
    def writeToDB(self, game):
        f = open(self.dbName, "a")    
        if game.result != False:    #validate that a valid result was entered, don't fill DB if not.
            f.write(game.storage())
        
        
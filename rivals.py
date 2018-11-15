'''
Created on 16 Nov 2018

@author: Lyrete
'''

from game import Game;
import datetime;

while(True):
    result = input("Result?\n");
    if(result == ""):
        break;
    goalsFor = result[0];
    goalsAgainst = result[2];
    newGame = Game(datetime.datetime.now(),goalsFor, goalsAgainst)
    f = open("gameData.csv", "a")
    f.write(newGame.storage());
    
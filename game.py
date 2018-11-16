'''
Created on 16 Nov 2018

@author: Lyrete
'''

class Game(object):

    def __init__(self, date, goalsFor, goalsAgainst, extraTime = False, pen = False, change = 0):
        self.goalsFor = goalsFor;
        self.goalsAgainst = goalsAgainst;
        self.extraTime = extraTime;
        self.date = date;
        self.pen = pen;
        self.change = change;
        self.result = self.makeResult();

    def makeResult(self):
        if(self.goalsFor == "" or self.goalsAgainst == ""):
            return False

        if(self.goalsFor > self.goalsAgainst):
            return "W"
        elif(self.goalsFor < self.goalsAgainst):
            return "L"
        elif(self.goalsFor == self.goalsAgainst):
            return "D"




    def storage(self):
        return self.date.strftime("%Y-%m-%d") + "," + self.goalsFor + "," + self.goalsAgainst + "\n";

    def __str__(self):
        return str(self.result) + " ("+ self.goalsFor + "-" + self.goalsAgainst + ")";

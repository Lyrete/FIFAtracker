'''
Created on 16 Nov 2018

@author: Lyrete
'''

from appJar import gui
from dataHandler import dataHandler;
from game import Game;
import datetime;

db = dataHandler();

app = gui();

app.setTitle("FIFA tracker v0.1")

app.setSize(200,100)
app.addLabel("title", "FIFA tracker v0.1")
app.setLabelBg("title", "red")

app.addLabelEntry("Goals For")
app.addLabelEntry("Goals Against")

def press(button):
    if button == "Close":
        app.stop();
    if button == "Submit":
        goalsFor = app.getEntry("Goals For");
        goalsAgainst = app.getEntry("Goals Against");
        newGame = Game(datetime.datetime.now(),goalsFor, goalsAgainst);
        db.writeToDB(newGame);
        
app.addButtons(["Submit", "Close"], press)

app.go()
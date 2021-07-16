from keras.models import load_model
import cv2
import numpy as np
from random import choice

REV_CLASS_MAP = {
    0: "rock",
    1: "paper",
    2: "scissors",
    3: "none"
}


def mapper(val):
    return REV_CLASS_MAP[val]


def calculate_winner(move1, move2):
    if move1 == move2:
        return "Tie"

    if move1 == "rock":
        if move2 == "scissors":
             return "User"
        if move2 == "paper":
            return "Computer"
        
     if move1 == "paper":
        if move2 == "rock":
            return "User"
         if move2 == "scissors":
                return "Computer"
            
    if move1 == "scissors":
        if move2 == "paper":
            return "User"
        if move2 == "rock":
             return "Computer"
        
        
model = load_model("rock-paper-scissors-model.h5")

cap = cv2.VideoCapture(0) 
 
  
  
  

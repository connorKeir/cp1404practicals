"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random

def main():
    score = float(input("Enter score: "))
    print(score_calculator(score))



def score_calculator(score):
    if score < 0 or score > 100:
        return("Invalid score")
    elif 0 <= score < 50:
        return("Bad")
    elif 50 <= score < 90:
        return("Passable")
    elif 90 <= score <= 100:
        return ("Excellent")

def random_score():
    score = random.randint(0,100)
    print("Below is the random score and its result:")
    print("Random score of {} and is a {} score".format(score, score_calculator(score)))



main()
random_score()
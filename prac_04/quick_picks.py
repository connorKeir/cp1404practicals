import random


RANDOM_NUMBER_MAX = 6

def main ():
    count = int(input("How many quick picks? "))  # get a count variable for how many quick picks there will be
    for i in range(0, count):
        quick_picks = [random.randint(1,45)]  # establish the first random number in the list
        for i in range(0, RANDOM_NUMBER_MAX-1):
            # for loop to generate complete list of random numbers
            random_number = (random.randint(1,45))
            while random_number in quick_picks:
                # prevent the new random number from being in quick_picks list already
                random_number = (random.randint(1,45))
            quick_picks.append(random_number)  # add the completely random number to the quick_picks list
        quick_picks.sort()  # sort the list in ascending order
        print(quick_picks)


main()
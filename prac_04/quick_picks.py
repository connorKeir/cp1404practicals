import random


RANDOM_NUMBER_MAX = 6

def main ():
    count = int(input("How many quick picks? "))  # get a count variable for how many quick picks there will be
    for i in range(0, count):
        quick_picks = [random.randint(1,45)]
        for i in range(0, RANDOM_NUMBER_MAX-1):
            random_number = (random.randint(1,45))
            while random_number in quick_picks:
                random_number = (random.randint(1,45))
            quick_picks.append(random_number)
        quick_picks.sort()
        print(quick_picks)


main()
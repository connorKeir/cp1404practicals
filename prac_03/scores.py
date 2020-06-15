import random


def main():
    score_number = int(input("Enter number of scores: "))
    random_score(score_number)


def score_calculator(score):
    if score < 0 or score > 100:
        return ("Invalid score")
    elif 0 <= score < 50:
        return ("Bad")
    elif 50 <= score < 90:
        return ("Passable")
    elif 90 <= score <= 100:
        return ("Excellent")


def random_score(score_number):
    temp_file = open("results.txt", 'a')
    for i in range(score_number):
        score = random.randint(0, 100)
        print("Random score of {} and is a {} score".format(score, score_calculator(score)), file=temp_file)
    temp_file.close()


main()

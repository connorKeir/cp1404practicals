"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

MENU = """Enter your sales
Enter a negative number to quit"""  # creating a display for the options on the main user menu

print(MENU)  # displays the menu
sales = float(input(">>>").upper())  # Lets the user input their sales amount
while sales >= 0:  # initializes a loop calculating the users bonus
    if sales < 1000:  # if sales are below $1000
        bonus_amount = sales * 0.1  # calculates bonus by multiplying sales by 10 percent
        print("Your Bonus: ${:.2f}".format(bonus_amount))
    elif sales >= 1000:  # if sales are $1000 or greater
        bonus_amount = sales * 0.15  # calculates bonus by multiplying sales by 15 percent
        print("Your Bonus: ${:.2f}".format(bonus_amount))  # displays bonus
    else:
        print("Invalid input")  # if the user doesn't enter a number it will tell them they have entered a wrong input
    print("~~~~~~~~~~~~~~~~~")
    print(MENU)  # re-displays the menu in case the user wishes to do more calculations
    sales = float(input(">>>").upper())  # retakes the sales amount for a new calculation
print("Thanks, have a nice day!")

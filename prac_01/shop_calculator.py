number_of_items = int(input("Number of Items: "))

while number_of_items < 0:  # if the number of items is invalid (less than 0) start a loop
    print("Invalid number of items!")  # tell the user that they have an invalid number of items
    number_of_items = int(input("Please re-enter the number of items: "))  # takes a new number from the user

total_price = 0  # initializes total_price as value equal to zero
for i in range(0, number_of_items, 1):  # loop to the number of items entered
    price_of_item = float(input("What did the Item Cost?: "))  # asks the user the price of an item
    total_price += price_of_item  # calculates the total price
if total_price > 100:  # if total price is over 100
    total_price -= (total_price * 0.1)  # applies a 10 percent discount to the total price
print('${:.2f} '.format(total_price))  # displays the total price to 2 decimal places to the user

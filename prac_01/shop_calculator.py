"""
CP1404 Practical
Shop Calculator that works out the total price for a number of items
If the total is greater than $100, there is a 10% discount
"""

total_price = 0
number_of_items = int(input('Number of items: '))

while number_of_items < 0:
    print('Invalid number of items!')
    number_of_items = int(input('Number of items: '))

for i in range(number_of_items):
    price_of_item = float(input('Price of item: '))
    total_price = total_price + price_of_item       # Adds the price to the total

if total_price > 100:
    total_price = total_price * 0.9     # Apply 10% discount

print('Total price for', number_of_items, 'items is ${:.2f}'.format(total_price))

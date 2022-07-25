import budget
from budget import create_spend_chart
from unittest import main

food = budget.Category("Food")
food.deposit(1000, "Deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant Invoice")
clothing = budget.Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.00, "Free")
clothing.withdraw(100)
auto = budget.Category("Utility")
auto.deposit(1000, "Deposit")
auto.withdraw(15)
print(food)
print(clothing)
print(auto)
print(create_spend_chart([food, clothing, auto]))
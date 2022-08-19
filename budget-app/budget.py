from email import header
from string import whitespace
from xml.dom.minidom import CharacterData


class Category:
    def __init__(self, category):
        self.ledger = []
        self.amount = 0
        self.category = category

    # Deposit Function
    def deposit(self, amount, desc=""):
        append_list = {"amount": amount, "description": desc}
        self.ledger.append(append_list)
        self.amount += amount

    # Withdraw Function
    def withdraw(self, amount, desc=""):

        if self.check_funds(amount) == True:
            self.amount -= amount
            append_list = {"amount": -amount, "description": desc}
            self.ledger.append(append_list)
            return True
        else:
            return False

    # Balance Function
    def get_balance(self):
        return self.amount

    # Check Funds Availability
    def check_funds(self, amount):

        if self.amount < amount:
            return False
        else:
            return True

    # Transfer Funds
    def transfer(self, amount, category):

        if self.check_funds(amount) == True:
            self.amount -= amount
            self.ledger.append({"amount": -amount, "description": "Transfer to " + category.category})
            category.deposit(amount, "Transfer from " + self.category)
            return True
        else:
            return False

    # String Display
    def __str__(self):
        category_len = len(self.category)
        max_len = 30
        asteriks = []

        for i in range(max_len - category_len):
            asteriks.append('*')
        one_side_asteriks = int(len(asteriks)/2)
        asteriks.insert(one_side_asteriks, self.category)
        header = "".join(asteriks)
        ledger_items = []

        for item in self.ledger:
            whitespace = max_len
            ledger_item = []
            ledger_item.append(item["description"][:23])
            whitespace -= len(ledger_item[0])
            ledger_item.append("{0:.2f}".format(item["amount"])[:7])
            whitespace -= len(ledger_item[1])
            ledger_item.insert(1, " " * whitespace)
            ledger_item.append("\n")
            ledger_items.append(ledger_item)
        ledger_lines = ''.join([j for i in ledger_items for j in i])
        total = self.get_balance()

        return f'{header}\n{ledger_lines}Total: {total}'

# Spend Chart
def create_spend_chart(categories):
    y_axis = ["100", "90", "80", "70", "60", "50", "40", "30", "20", "10", "0"]
    graph_content = "Percentage spent by category\n"
    category_names = []
    spent_percentage = []
    spent_list = []

    for category in categories:
        total_amount = 0

        for item in category.ledger:

            if item['amount'] < 0:
                total_amount -= item['amount']
        spent_list.append(round(total_amount, 2))
        category_names.append(category.category)

    for amount in spent_list:
        spent_percentage.append(round((amount/sum(spent_list)), 2)*100)

    for label in y_axis:
        graph_content += str(label).rjust(3)+"|"

        for percentage in spent_percentage:

            if percentage >= int(label):
                graph_content += " o "
            else:
                graph_content += "   "
        graph_content += " \n"
    graph_content += "    ----" + ("---" * (len(category_names) - 1)) + "\n    "

    longest_name_length = 0

    for name in category_names:

        if longest_name_length < len(name):
            longest_name_length = len(name)

    for val in range(longest_name_length):

        for name in category_names:

            if len(name) > val:
                graph_content += " " + name[val]+" "
            else:
                graph_content += "   "
        graph_content += " "

        if val < longest_name_length-1:
            graph_content += "\n    "

    return graph_content

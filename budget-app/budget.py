class Category:
    def __init__(self, name):
        self.ledger = []
        self.amount = 0
        self.name = name

    def deposit(self, amount, desc=""):
        self.ledger.append({"amount": amount, "description": desc})
        self.amount += amount

    def withdraw(self, amount, desc=""):
        if self.check_funds(amount):
            self.amount -= amount
            self.ledger.append({"amount": -amount, "description": desc})
            return True

        return False

    def get_balance(self):
        return self.amount

    def check_funds(self, amount):
        return not self.amount < amount

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.amount -= amount
            self.ledger.append({"amount": -amount, "description": "Transfer to " + category.name})
            category.deposit(amount, "Transfer from " + self.name)
            return True

        return False

    def __str__(self):
        header = self.name.center(30, "*")
        content = ""

        for transaction in self.ledger:
            content += transaction['description'].ljust(23, " ")[:23]
            content += "{0:>7.2f}".format(transaction['amount'])
            content += "\n"

        return f'{header}\n{content}Total: {self.get_balance()}'


def create_spend_chart(categories):
    y_axis = ["100", "90", "80", "70", "60", "50", "40", "30", "20", "10", "0"]
    graph_content = "Percentage spent by category\n"
    category_names,spent_percentage,spent_list = [],[],[]

    for category in categories:
        total_spent_amount = 0

        for transaction in category.ledger:
            if transaction['amount'] < 0:
                total_spent_amount = abs(transaction['amount'])

        spent_list.append(round(total_spent_amount, 2))
        category_names.append(category.name)
        longest_name_length = 0

        if longest_name_length < len(category.name):
            longest_name_length = len(category.name)

    for amount in spent_list:
        spent_percentage.append(round((amount/sum(spent_list)), 2)*100)

    for value in y_axis:
        graph_content += value.rjust(3)+"|"

        for percentage in spent_percentage:
            graph_content += " o " if percentage >= int(value) else "   "

        graph_content += " \n"

    graph_content += "    ----" + ("---" * (len(category_names) - 1)) + "\n    "

    def set_value(value=" "):
        return " " + value + " "

    for val in range(longest_name_length):
        for name in category_names:
                graph_content += set_value(name[val]) if len(name) > val else set_value()

        graph_content += " "

        if val < longest_name_length-1:
            graph_content += "\n    "

    return graph_content
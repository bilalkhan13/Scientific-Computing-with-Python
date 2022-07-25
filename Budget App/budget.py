from email import header
from string import whitespace
from xml.dom.minidom import CharacterData


class Category:
    def __init__(self, category):
        self.ledger = []
        self.amount = 0
        self.category = category

    def deposit(self, amount, desc=""):
        appendList = {"amount": amount, "description": desc}
        self.ledger.append(appendList)
        self.amount += amount

    def withdraw(self, amount, desc=""):
        if self.check_funds(amount) == True:
            self.amount -= amount
            appendList = {"amount": -amount, "description": desc}
            self.ledger.append(appendList)
            return True
        else:
            return False

    def get_balance(self):
        return self.amount

    def check_funds(self, amount):
        if self.amount < amount:
            return False
        else:
            return True

    def transfer(self, amount, category):
        if self.check_funds(amount) == True:
            self.amount -= amount
            appendList = {"amount": -amount,
                          "description": "Transfer to " + category.category}
            self.ledger.append(appendList)
            category.deposit(amount, "Transfer from " + self.category)
            return True
        else:
            return False

    def __str__(self):
        cat_len = len(self.category)
        max_len = 30
        asteriks = []

        for i in range(max_len - cat_len):
            asteriks.append('*')
        oneSideAsteriks = int(len(asteriks)/2)
        asteriks.insert(oneSideAsteriks, self.category)
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


def create_spend_chart(categories):
    return "-----------"

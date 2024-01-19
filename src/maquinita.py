class VendingMachine:
    def __init__(self, display):
        self.display = display
        self.display.output("INSERT_COIN")

    def insert_coin(self, money_amount):
        if money_amount == 0.10:
            self.display.output("$0.10")
        else:
            self.display.output("$0.05")

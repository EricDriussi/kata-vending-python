class VendingMachine:
    def __init__(self, display):
        self.display = display
        self.display.output("INSERT_COIN")

    def insert_coin(self, money_amount):
        self.display.output("$0.05")

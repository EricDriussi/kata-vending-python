from assertpy import assert_that

from src.maquinita import VendingMachine


class TestVendingMachine:

# The vending machine will accept valid coins (nickels, dimes, and quarters) and reject invalid ones (pennies). When a valid coin is inserted the amount of the coin will be added to the current amount and the display will be updated. When there are no coins inserted, the machine displays INSERT COIN. Rejected coins are placed in the coin return.

    def test_machine_displays_INSERT_COIN_when_no_coins_are_inserted(self):
        display = DisplaySpy()

        VendingMachine(display)

        assert_that(display.output_was_called_with("INSERT_COIN")).is_true()

    def test_machine_displays_money_amount_of_one_nickel_when_one_nickel_is_inserted(self):
        display = DisplaySpy()
        money_amount = 0.05
        vending_machine = VendingMachine(display)

        vending_machine.insert_coin(money_amount)

        assert_that(display.output_was_called_with("$0.05")).is_true()

    def test_machine_displays_money_amount_of_one_dime_when_one_dime_is_inserted(self):
        display = DisplaySpy()
        money_amount = 0.10
        vending_machine = VendingMachine(display)

        vending_machine.insert_coin(money_amount)

        assert_that(display.output_was_called_with("$0.10")).is_true()

    def test_machine_displays_money_amount_of_one_quarter_when_one_quarter_is_inserted(self):
        display = DisplaySpy()
        money_amount = 0.25
        vending_machine = VendingMachine(display)

        vending_machine.insert_coin(money_amount)

        assert_that(display.output_was_called_with("$0.25")).is_true()

    def test_machine_does_not_update_display_when_one_invalid_coin_is_inserted(self):
        display = DisplaySpy()
        invalid_money_amount = 0.01
        vending_machine = VendingMachine(display)

        vending_machine.insert_coin(invalid_money_amount)

        assert_that(display.output_was_called_with("INSERT_COIN")).is_true()

    def test_machine_displays_current_money_amount_incremented_by_one_nickel_money_amount(self):
        display = DisplaySpy()
        money_amount = 0.05
        vending_machine = VendingMachine(display)
        vending_machine.insert_coin(money_amount)
        vending_machine.insert_coin(money_amount)

        assert_that(display.output_was_called_with("$0.10")).is_true()


class DisplaySpy:

    def __init__(self):
        self.output_was_called = False
        self.called_text = ""

    def output(self, msg):
        self.output_was_called = True
        self.called_text = msg
        print(msg)

    def output_was_called(self):
        return self.output_was_called

    def output_was_called_with(self, text):
        was_called = self.output_was_called
        was_called_with = self.called_text == text
        return was_called and was_called_with

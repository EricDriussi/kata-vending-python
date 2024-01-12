from unittest import TestCase

from assertpy import assert_that

from src.narcissistic_number import VendingMachine

class DisplaySpy:
    insertCoinWasCalled = False

    def insert_coin(self):
        self.insertCoinWasCalled = True

    def assert_insert_coin_was_called(self):
        assert_that(self.insertCoinWasCalled).is_true()


class TestVendingMachine:

    def requests_coins_when_there_are_no_coins_inserted(self):
        display = DisplaySpy()

        _ = VendingMachine(display)

        display.assert_insert_coin_was_called()
        pass

    def invalid_coins_are_not_counted(self):
        # Given
        # penny = InvalidCoin()
        # maquinita = VendingMachine()
        # When
        # maquinita.insert(penny)
        # Then
        # no me lo añadió al conteo

        pass

    def invalid_coins_are_returned(self):
        # Given
        # tengo un penny
        # When
        # lo enchufo en la maquina
        # Then
        # me devolvió la moneda

        pass

    def nickels_are_counted(self):

        pass

    def nickels_are_not_returned(self):

        pass

    def valid_coins_are_counted(self):

        pass

    def valid_coins_are_not_returned(self):

        pass


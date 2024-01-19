from assertpy import assert_that

from src.maquinita import VendingMachine


class TestVendingMachine:

    def test_cositas(self):
        maquinita = VendingMachine()
        assert_that(maquinita.add(1, 2)).is_equal_to(3)
        pass


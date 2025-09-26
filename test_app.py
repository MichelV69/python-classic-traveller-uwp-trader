import pytest
from classicTravellerRules import *

RI_AG_UWP = "C-767795-9"
NAG_NIN_P_UWP = "B-222699-B"


class TestGetBrokerCommission:
    def test_brokerLvl1(self):
        assert getBrokerCommission(1) == 0.05

    def test_brokerLvl2(self):
        assert getBrokerCommission(2) == 0.10

    def test_brokerLvl3(self):
        assert getBrokerCommission(3) == 0.15

    def test_brokerLvl4(self):
        assert getBrokerCommission(4) == 0.20


class TestPlanetMethods:
    blueMarble = Planet("BlooSpec", RI_AG_UWP)
    brownRock = Planet("Crumplli", NAG_NIN_P_UWP)

    def test_HexToInt(self):
        assert self.blueMarble.hexToInt("A") == 10
        assert self.blueMarble.hexToInt("8") == 8
        assert self.blueMarble.hexToInt("F") == 15

    def test_extractStatAtmosphere(self):
        assert self.blueMarble.atmosphere() == 6

    def test_extractStatGovernment(self):
        assert self.blueMarble.government() == 9

    def test_isAgWorld(self):
        assert self.blueMarble.is_agricultural()
        assert self.brownRock.is_nonAgricultural()

    def test_isRichWorld(self):
        assert self.blueMarble.is_rich()
        assert self.brownRock.is_poor()

    def test_getTradeClasses(self):
        assert self.blueMarble.getTradeClasses().__contains__("[Ri]")
        assert self.blueMarble.getTradeClasses().__contains__("[Ag]")

        assert self.brownRock.getTradeClasses().__contains__("[NAg]")
        assert self.brownRock.getTradeClasses().__contains__("[NIn]")
        assert self.brownRock.getTradeClasses().__contains__("[P]")

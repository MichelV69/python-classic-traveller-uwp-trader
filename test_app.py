import pytest

from app import getBrokerCommission, Planet


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
    blueMarble = Planet("BlooSpec", "B-678567-C")

    def test_HexToInt(self):
        assert self.blueMarble.hexToInt("A") == 10
        assert self.blueMarble.hexToInt("8") == 8
        assert self.blueMarble.hexToInt("F") == 15

    def test_extractStatAtmosphere(self):
        assert self.blueMarble.atmosphere() == 7

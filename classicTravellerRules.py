import locale
from diceBag import *

# Set the locale to CA English
locale.setlocale(locale.LC_ALL, "en_CA.UTF-8")

# --- classes


class Planet:
    uwp_map = dict(
        starport=0, size=2, atmo=3, hydro=4, pop=5, gov=6, law=7, tech=9
    )

    def __init__(self, name, uwp):
        self.name = name
        self.uwp = uwp

    def hexToInt(self, hexStat):
        match hexStat.upper():
            case "A":
                return 10
            case "B":
                return 11
            case "C":
                return 12
            case "D":
                return 13
            case "E":
                return 14
            case "F":
                return 15
            case "E":
                return 16
            case _:
                return int(hexStat)

    def is_agricultural(self):
        if self.atmosphere() < 4 or self.atmosphere() > 9:
            return False
        if self.hydrographic() < 4 or self.hydrographic() > 8:
            return False
        if self.population() < 5 or self.population() > 7:
            return False
        return True

    def is_nonAgricultural(self):
        if self.atmosphere() > 3:
            return False
        if self.hydrographic() > 3:
            return False
        if self.population() < 6:
            return False
        return True

    def is_rich(self):
        if self.atmosphere() != 6 and self.atmosphere() != 8:
            return False
        if self.population() < 6 or self.population() > 8:
            return False
        if self.government() < 4 or self.government() > 9:
            return False
        return True

    def is_poor(self):
        if self.atmosphere() < 2 or self.atmosphere() > 5:
            return False
        if self.hydrographic() > 3:
            return False
        return True

    def is_industrial(self):
        if (
            self.atmosphere() > 2
            and self.atmosphere() != 4
            and self.atmosphere() != 7
            and self.atmosphere() != 9
        ):
            return False
        if self.population() < 9:
            return False
        return True

    def is_nonIndustrial(self):
        if self.population() > 6:
            return False
        return True

    def atmosphere(self):
        return self.hexToInt(self.uwp[self.uwp_map["atmo"]])

    def hydrographic(self):
        return self.hexToInt(self.uwp[self.uwp_map["hydro"]])

    def population(self):
        return self.hexToInt(self.uwp[self.uwp_map["pop"]])

    def government(self):
        return self.hexToInt(self.uwp[self.uwp_map["gov"]])

    def getTradeClasses(self):
        tradeClasses = ""
        if self.is_agricultural():
            tradeClasses += " [Ag]"

        if self.is_nonAgricultural():
            tradeClasses += " [NAg]"

        if self.is_industrial():
            tradeClasses += " [Ind]"

        if self.is_nonIndustrial():
            tradeClasses += " [NIn]"

        if self.is_poor():
            tradeClasses += " [P]"

        if self.is_rich():
            tradeClasses += " [Ri]"

        return tradeClasses


# --- functions


def getBrokerCommission(brokerLevel):
    match brokerLevel:
        case 1:
            return 0.05
        case 2:
            return 0.10
        case 3:
            return 0.15
        case 4:
            return 0.20


def textiles(src, dest, brokerLevel):
    kindOfGoods = "Textiles: "
    basePrice = 3000
    availableQuantity = d6(3) * 5

    valueRoll = d6(2)
    if src.is_agricultural():
        valueRoll -= 7
    if src.is_nonAgricultural():
        valueRoll -= 5
    if src.is_nonIndustrial():
        valueRoll -= 3

    indent = "\n    "
    purchaseModPercent = actualValue(valueRoll)
    localCost = basePrice * purchaseModPercent
    orderValue = int(availableQuantity * localCost)
    brokerCommission = round(
        float(getBrokerCommission(brokerLevel)) * int(orderValue), 0
    )

    resultText = "Cargo Available: " + str(availableQuantity) + " tonnes "
    resultText += (
        "with a common market value of Cr"
        + locale.format_string("%d", basePrice, grouping=True)
        + "/ton."
    )
    resultText += indent + "We can purchase them locally for Cr"
    resultText += (
        locale.format_string("%d", localCost, grouping=True)
        + " per ton, which is a valuation "
    )
    if purchaseModPercent < 1:
        resultText += "below"
    else:
        resultText += "at or above"
    resultText += (
        " common market value." + indent + "That will cost us a total of Cr"
    )
    resultText += locale.format_string("%d", orderValue, grouping=True) + "."
    if int(brokerLevel) > 0:
        resultText += (
            indent + "This is in part due to our Broker, who will charge us"
        )
        resultText += (
            " Cr"
            + locale.format_string("%d", brokerCommission, grouping=True)
            + " for this transaction."
        )

    valueRoll = d6(2)
    if dest.is_agricultural():
        valueRoll -= 7
    if dest.is_nonAgricultural():
        valueRoll += 1
    if dest.is_rich():
        valueRoll += 3

    saleModPercent = actualValue(valueRoll)
    destSale = int(basePrice * saleModPercent)
    saleValue = int(destSale * availableQuantity)

    resultText += indent + "We expect to be able to sell upon arrival to "
    resultText += (
        dest.name
        + " for Cr"
        + locale.format_string("%d", destSale, grouping=True)
        + "/ton, which would be"
    )
    resultText += (
        " a total value of Cr"
        + locale.format_string("%d", saleValue, grouping=True)
        + "."
    )
    resultText += indent + "That would net a *"
    profitLoss = "profit"
    if saleValue < orderValue:
        profitLoss = "loss"
    resultText += (
        profitLoss
        + "* of Cr"
        + locale.format_string(
            "%d", abs(saleValue - orderValue), grouping=True
        )
        + "."
    )

    return resultText

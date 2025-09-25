import random

print("\n Classic Traveller Speculative Trade Generator")
print("````````````````````````````````````````````` ")
print("\n based on the rules found on pp.104-105 of 'The Traveller Book'(1977) ")

# create object for data storage / query

class Planet:
  def __init__(self, name, uwp):
    self.name = name
    self.uwp = uwp


# get sourceworld UWP
src = Planet("sourceworld", "x-000000-0")
src.uwp = input("\n Please enter the Source Planet's UWP (x-123456-7): ")
print("got "+src.uwp)

# get destworld UWP
dest = Planet("destworld", "x-000000-0")
dest.uwp = input("\n Please enter the Destination Planet's UWP (x-123456-7): ")
print("got "+dest.uwp)

# get broker level

brokerLevel = input("\n Please enter the available Broker level (0 .. 4): ")
print("brokerLevel: "+brokerLevel)

# roll a pair of D6, do not add them together.
d6a = random.randint(1, 6)
d6b = random.randint(1, 6)

dicePair = d6a*10 + d6b
print("dicePair: " + str(dicePair))

cargo = ""

match dicePair:
    case 11:
        cargo = textiles(src, dest, brokerLevel)
    case _:
        cargo = textiles(src, dest, brokerLevel)

print cargo


def d6(rolls):
    result = 0
    for _ to rolls:
        result += random.randint(1, 6)
    return result


def actualValue(twoDsix):
    if twoDsix < 2:
        twoDsix = 2
    if twoDsix > 15:
        twoDsix = 15

    return match twoDsix:
        2: 0.4
        3: 0.5
        4: 0.7
        5: 0.8
        6: 0.9
        7: 1.0
        8: 1.1
        9: 1.2
        10: 1.3
        11: 1.5
        12: 1.7
        13: 2.0
        14: 3.0
        15: 4.0


def getBrokerCommission(brokerLevel):
    return match brokerLevel:
        1: 5
        2: 10
        3: 15
        4: 20

def textiles(src, dest, brokerLevel):
    resultText = "Textiles: "
    basePrice = 3000
    availableQuantity = d6(3)*5

    valueRoll = d6(2)
    if src.is_agricultural():
        valueRoll -= 7
    if src.is_nonAgricultural():
        valueRoll -= 5
    if src.is_nonIndustrial():
        valueRoll -= 3

    purchaseModPercent = actualValue(valueRoll)
    brokerCommission = getBrokerCommission(brokerLevel)

    return resultText

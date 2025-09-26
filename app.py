import random
from classicTravellerRules import *

# --- functions


def d6(rolls):
    result = 0
    done = 0
    while done < rolls:
        done += 1
        result += random.randint(1, 6)
    return result


def actualValue(twoDsix):
    if twoDsix < 2:
        twoDsix = 2
    if twoDsix > 15:
        twoDsix = 15

    match twoDsix:
        case 2:
            result = 0.4
        case 3:
            result = 0.5
        case 4:
            result = 0.7
        case 5:
            result = 0.8
        case 6:
            result = 0.9
        case 7:
            result = 1.0
        case 8:
            result = 1.1
        case 9:
            result = 1.2
        case 10:
            result = 1.3
        case 11:
            result = 1.5
        case 12:
            result = 1.7
        case 13:
            result = 2.0
        case 14:
            result = 3.0
        case 15:
            result = 4.0

    return result

# --- main work


def main():

    src = Planet("sourceworld", "x-000000-0")
    src.uwp = input("\n Please enter the Source Planet's UWP (x-123456-7): ")
    print("got " + src.uwp)

    dest = Planet("destworld", "x-000000-0")
    dest.uwp = input("\n Please enter the Destination Planet's UWP (x-123456-7): ")
    print("got " + dest.uwp)

    brokerLevel = input("\n Please enter the available Broker level (0 .. 4): ")
    print("brokerLevel: " + brokerLevel)

    # roll a pair of D6, do not add them together.
    d6a = random.randint(1, 6)
    d6b = random.randint(1, 6)

    dicePair = d6a * 10 + d6b
    print("dicePair: " + str(dicePair))

    cargo = ""

    match dicePair:
        case 11:
            cargo = textiles(src, dest, brokerLevel)
        case _:
            cargo = textiles(src, dest, brokerLevel)

    print(cargo)


if __name__ == "__main__":
    main()

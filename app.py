from classicTravellerRules import *
from diceBag import *


# --- main work


def main():
    # C-767795-9 (rich ag)
    # B-222699-B (NAg Ind)

    src = Planet("sourceworld", "C-767795-9")
    # src.uwp = input("\n Please enter the Source Planet's UWP (x-123456-7): ")

    dest = Planet("destworld", "B-222699-B")
    # dest.uwp = input("\n Please enter the Destination Planet's UWP (x-123456-7): ")

    brokerLevel = (
        1  # input("\n Please enter the available Broker level (0 .. 4): ")
    )

    # roll a pair of D6, do not add them together.[[
    d6a = random.randint(1, 6)
    d6b = random.randint(1, 6)
    # ]]

    # weird dice mod stuff from pp.104 [[
    if src.population() >= 9:
        d6a += 1
    if src.population() <= 5:
        d6a -= 1

    if d6a < 1:
        d6a == 1
    if d6a > 6:
        d6a == 1
    # ]]

    dicePair = d6a * 10 + d6b
    print("dicePair: " + str(dicePair))

    cargo = ""

    match dicePair:
        case 11:
            cargo = textiles(src, dest, brokerLevel)
        case _:
            cargo = textiles(src, dest, brokerLevel)

    print("Speculative Cargo Opportunities")
    print(
        "From: "
        + src.name
        + " ("
        + src.uwp
        + " "
        + src.getTradeClasses()
        + ")"
    )
    print(
        "To: "
        + dest.name
        + " ("
        + dest.uwp
        + " "
        + dest.getTradeClasses()
        + ") \n"
    )

    print(cargo)


if __name__ == "__main__":
    main()

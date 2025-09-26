import random

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

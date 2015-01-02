__author__ = 'Dark_Silencer_P'
__project__ = 'WindWeather'

import dNroll


"""
WindWeather

The whole point of this module is to serve as a random weather generator of sors
"""


def weather():
    # First will be a d12 roll to determine the weather type, followed by a declaration of the result, followed by what it means.
    """	1: Grand storm, ships take ongoing 1d6 damage, spawn 1d6 twisters that move in wind direction and deal 1d12 +6 damage, boarding -15, PER -10, 25% chance of DEX check to avoid being moved by storm; difficult terrain
		2-5: Partially cloudy
		6: Thunderstorm; 25% likely lightning strikes ship, deals 2d6 lightning damage to ship and those aboard, 33% chance of rainy
		7-9: Sunny
		10: Rainy, difficult terrain, -5 boarding, -5 PER, 10% chance of DEX checks vs slipping
		11: Hail, -5 PER, -5 boarding, 1d4 damage to all uncovered individuals
		12: Perfect day, sunny, zero clouds, +5 PER.
    """
    d12 = dNroll.rolld12()
    if d12 == 1:
        weather = "a grand storm (ships take ongoing 1d6 damage, spawn 1d6 twisters that move in wind direction and deal 1d12 +6 damage, boarding -15, PER -10, 25% chance of DEX check to avoid being moved by storm; difficult terrain)"
    elif d12 >= 2 and d12 <= 5:
        weather = "partially cloudy"
    elif d12 == 6:
        weather = "thunderstorm (25% likely lightning strikes ship, deals 2d6 lightning damage to ship and those aboard, 20% chance of rain)"
    elif d12 >= 7 and d12 <= 9:
        weather = "Sunny"
    elif d12 == 10:
        weather = "rainy (-5 boarding, -5 PER, 10% chance of DEX checks vs slipping)"
    elif d12 == 11:
        weather = "hail (-5 PER, -5 boarding, 1d4 damage to all uncovered individuals)"
    elif d12 == 12:
        weather = "a perfect day, sunny, zero clouds, (+5 PER)"
    else:
        weather = "d12 out of range, check the d12 weather if-else chain in WindWeather"
    return weather


def windheading():
    """	1: Wind blows from multiple directions, ships move as if upwind.
		2: N
		3: NE
		4: E
		5: SE
		6: S
		7: SW
		8: W
		9: NW
		0: Wind blows optimally from multiple directions, ships move as if downwind
    """
    d10 = dNroll.rolld10()
    if d10 == 1:
        windheading = "North"
    elif d10 == 2:
        windheading = "North-East"
    elif d10 == 3:
        windheading = "East"
    elif d10 == 4:
        windheading = "South-East"
    elif d10 == 5:
        windheading = "South"
    elif d10 == 6:
        windheading = "South-West"
    elif d10 == 7:
        windheading = "West"
    elif d10 == 8:
        windheading = "North-West"
    elif d10 == 9:
        windheading = "all over the place, ships move as if upwind."
    elif d10 == 0:
        windheading = "optimal from multiple directions, ships move as if downwind"
    else:
        windheading = ("d10 out of range, check the d10 windheading if-else chain in WindWeather")
    return windheading


def windspeed():
    """	00: Gale winds, sails take 1d12+15 damage, ships take ongoing 1d4 damage, Speed=12, 25% chance of DEX check vs being pushed, -5 boarding
		10: No wind, (Speed=0)
		20-30: a Weak Breeze, (Speed=2)
		40-50: a Strong Breeze, (Speed=4)
		60-70: a Good Winds, (Speed=6)
        80-90: a Excellent Winds, (Speed=8)
    """
    d100 = dNroll.rolld100()
    if d100 >= 1 and d100 <= 10:
        windspeed = "The wind is practically nonexistant, (Speed=0)"
        speed = 0
    elif d100 >= 11 and d100 <= 30:
        windspeed = "There is a Weak Breeze, (Speed=1)"
        speed = 1
    elif d100 >= 31 and d100 <= 50:
        windspeed = "There is a Strong Breeze, (Speed=2)"
        speed = 2
    elif d100 >= 51 and d100 <= 70:
        windspeed = "There is a Good Winds, (Speed=3)"
        speed = 3
    elif d100 >= 71 and d100 <= 90:
        windspeed = "There is an Excellent Winds, (Speed=4)"
        speed = 4
    elif d100 >= 91 and d100 <= 100:
        windspeed = "There are Gale-force winds, (sails take 1d12+15 damage, ships take ongoing 1d4 damage, Speed=12, 25% chance of DEX check vs being pushed, -5 boarding)"
        speed = 5
    else:
        windspeed = ("d100 out of range, check the d100 windspeed if-else chain in WindWeather")
        speed = 0
    return windspeed, speed


def windweather():
    w = weather()
    ws, speed = windspeed()
    wh = windheading()
    print("The weather is %s. %s and the heading is: %s" % (w, ws, wh))
    return w, ws, speed, wh
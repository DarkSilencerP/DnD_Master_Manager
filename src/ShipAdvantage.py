__author__ = 'Dark_Silencer_P'
__project__ = 'ShipAdvantage'

import dNroll

"""
Things to add to ShipAdvantage (in order of priority):
	- Increase the weight of the wind heading on advantage
	- Increase the weight of the captain's check on advantage
	- Decrease the weight of individual non-captain checks such that they are no longer exorbitantly overweighted
	- Add ship-based modifiers to ShipAdvantage such that Manuverability > Speed >> Size affect advantage
"""

"""	Advantage check: Ship Check + Weather Mod
	Ship Check: Captain Check + Shiphand Checks
	Captain: WIS +mod
		Normal: -10
		Admiral: -3, +2/rank
		Shiphand: -5, +1/rank
	Shiphands: STR +Mod -10
		Normal: -10
		Admiral: -5 +1/rank
		Shiphand:  -2, +2/rank
"""

"""
     - This module in its current state is highly dependent on PCLvl and PCDif to scale modifiers and checks
     - Unpack ship_input() as one tuple called ShipInput
"""


def lvldifscaler():
    y = 5
    PCDif = 0
    PCLvl = 1
    while PCDif <= 5:
        x = 30
        PCLvl = 1
        while PCLvl <= x:
            shiphand1rank = int(round((PCLvl / 3) - (PCDif / 2)))
            shiphand2rank = int(round((PCLvl / 3) + (PCDif / 2)))
            PCLvl += 1
            print(PCDif, "-", PCLvl, "-", shiphand1rank, "vs", shiphand2rank)
        PCDif += 1


def NPC_friendly_sea_rank(PCLvl, PCDif):
    # let's define the shiphand rank scale
    return int(round((PCLvl / 3) - (PCDif / 2)))


def NPC_unfriendly_sea_rank(PCLvl, PCDif):
    # let's define the shiphand rank scale
    return int(round((PCLvl / 3) + (PCDif / 2)))


def ship_input(PCLvl, PCDif):
    # asks for basic combat input info, or automates everything based on player info
    captain_1 = input('is Captain 1 a PC? Y or N:').lower()
    if captain_1 == 'y' or captain_1 == 'yes':
        captain_1roll = int(input('What is the roll?'))
        captain_1type = input('Is Ship 1 captain a captain or a shiphand?').lower()
    else:
        captain_1roll = dNroll.rolld20()
        captain_1type = 'captain'
    captain_1rank = NPC_friendly_sea_rank(PCLvl, PCDif)
    captain_2type = 'captain'
    captain_2rank = NPC_unfriendly_sea_rank(PCLvl, PCDif)
    captain_2roll = dNroll.rolld20()
    shiphand_1rank = NPC_friendly_sea_rank(PCLvl, PCDif)
    shiphand_2rank = NPC_unfriendly_sea_rank(PCLvl, PCDif)
    ship1heading = input('Ship #1\'s heading?')
    ship2heading = input('Ship #2\'s heading?')
    return captain_1, captain_1type, captain_1rank, captain_1roll, captain_2type, captain_2rank, captain_2roll, shiphand_1rank, shiphand_2rank, ship1heading, ship2heading


# unpack as a tuple, ShipInput


def NPC_STR(PCLvl, PCDif):
    return int(12 + int(PCLvl / 2) + PCDif)


# unpack as NPCSTR


def captain_checks(ShipInput, NPCSTR):
    captain_1, captain_1type, captain_1rank, captain_1roll, captain_2type, captain_2rank, captain_2roll, shiphand_1rank, shiphand_2rank, ship1heading, ship2heading = ShipInput
    # Captain 1 check
    if captain_1type == 'captain':
        captain_1mod = (captain_1rank * 2)
        captain_1mod -= 3
    elif captain_1type == 'shiphand':
        captain_1mod = (captain_1rank)
        captain_1mod -= 5
    else:
        captain_1mod = (-10)
    captain_1mod += NPCSTR
    captain_1check = captain_1roll + captain_1mod
    # I'm assuming max 2 ships here, so I'm just gonna run with that assumption
    captain_2roll = dNroll.rolld20()
    if captain_2type == 'captain':
        captain_2mod = (captain_2rank * 2)
        captain_2mod -= 3
    elif captain_2type == 'shiphand':
        captain_2mod = (captain_2rank)
        captain_2mod -= 5
    else:
        captain_2mod = (-10)
    captain_2mod += NPCSTR
    captain_2check = captain_2roll + captain_2mod
    return captain_1check, captain_2check


def shiphand_checks(ShipInput, NPCSTR):
    captain_1, captain_1type, captain_1rank, captain_1roll, captain_2type, captain_2rank, captain_2roll, shiphand_1rank, shiphand_2rank, ship1heading, ship2heading = ShipInput
    # Shiphand 1 check
    shiphand1roll = dNroll.rolld20() + NPCSTR
    shiphand1question = int(input('How many shiphands are there?'))
    shiphand1mod = (shiphand_1rank * 2) - 2
    shiphand1PCquestion = int(input('What was the combined shiphand check for the PCs?'))
    shiphand1check = shiphand1PCquestion + shiphand1question * (shiphand1roll + shiphand1mod)
    # shiphand 2 check
    shiphand2roll = dNroll.rolld20() + NPCSTR
    shiphand2question = int(input('How many shiphands are there on the second ship?'))
    shiphand2mod = (shiphand_2rank * 2) - 2
    shiphand2check = shiphand2question * (shiphand2roll + shiphand2mod)
    return shiphand1check, shiphand2check


def weathermod(speed, windheading, ShipInput):
    captain_1, captain_1type, captain_1rank, captain_1roll, captain_2type, captain_2rank, captain_2roll, shiphand_1rank, shiphand_2rank, ship1heading, ship2heading = ShipInput
    ship1weathermod = speed
    ship2weathermod = speed
    if windheading == ship1heading:
        ship1weathermod += 2
    elif ((ship1heading == 'N' and (windheading == 'NE' or windheading == 'NW')) or
              (ship1heading == 'S' and (windheading == 'SE' or windheading == 'SW')) or
              (ship1heading == 'E' and (windheading == 'NE' or windheading == 'SE')) or
              (ship1heading == 'W' and (windheading == 'NW' or windheading == 'SW')) or
              (ship1heading == 'NW' and (windheading == 'N' or windheading == 'W')) or
              (ship1heading == 'SW' and (windheading == 'S' or windheading == 'W')) or
              (ship1heading == 'NE' and (windheading == 'N' or windheading == 'E')) or
              (ship1heading == 'SE' and (windheading == 'S' or windheading == 'E'))):
        ship1weathermod += 1
    elif (((ship1heading == 'N' or ship1heading == 'S') and (windheading == 'E' or windheading == 'W')) or
              ((ship1heading == 'E' or ship1heading == 'W') and (windheading == 'N' or windheading == 'S')) or
              ((ship1heading == 'NW' or ship1heading == 'SE') and (windheading == 'NE' or windheading == 'SW')) or
              ((ship1heading == 'SW' or ship1heading == 'NE') and (windheading == 'SE' or windheading == 'NW'))):
        ship1weathermod += 0
    else:
        ship1weathermod -= 2
    if windheading == ship2heading:
        ship2weathermod += 2
    elif ((ship2heading == 'N' and (windheading == 'NE' or windheading == 'NW')) or
              (ship2heading == 'S' and (windheading == 'SE' or windheading == 'SW')) or
              (ship2heading == 'E' and (windheading == 'NE' or windheading == 'SE')) or
              (ship2heading == 'W' and (windheading == 'NW' or windheading == 'SW')) or
              (ship2heading == 'NW' and (windheading == 'N' or windheading == 'W')) or
              (ship2heading == 'SW' and (windheading == 'S' or windheading == 'W')) or
              (ship2heading == 'NE' and (windheading == 'N' or windheading == 'E')) or
              (ship2heading == 'SE' and (windheading == 'S' or windheading == 'E'))):
        ship2weathermod += 1
    elif (((ship2heading == 'N' or ship2heading == 'S') and (windheading == 'E' or windheading == 'W')) or
              ((ship2heading == 'E' or ship2heading == 'W') and (windheading == 'N' or windheading == 'S')) or
              ((ship2heading == 'NW' or ship2heading == 'SE') and (windheading == 'NE' or windheading == 'SW')) or
              ((ship2heading == 'SW' or ship2heading == 'NE') and (windheading == 'SE' or windheading == 'NW'))):
        ship2weathermod += 0
    else:
        ship2weathermod -= 2
    return ship1weathermod, ship2weathermod


def ship_advantage(captain_1check, captain_2check, shiphand1check, shiphand2check, ship1weathermod, ship2weathermod):
    ship1check = captain_1check + shiphand1check
    ship1advantage = ship1check + ship1weathermod
    print('Ship 1\'s advantage is:', ship1advantage)
    ship2check = captain_2check + shiphand2check
    ship2advantage = ship2check + ship2weathermod
    print('Ship 2\'s advantage is:', ship2advantage)
    if ship1advantage > ship2advantage:
        print('Ship 1 has the advantage!')
    elif ship1advantage < ship2advantage:
        print('Ship 2 has the advantage!')
    else:
        ship1advantage = dNroll.rolld20()
        ship2advantage = dNroll.rolld20()
        if ship1advantage > ship2advantage:
            print('Ship 1 has the advantage!')
        elif ship1advantage < ship2advantage:
            print('Ship 2 has the advantage!')
        else:
            print('Another tie! Manual roll!')
    return ship1advantage, ship2advantage


def allshipadv(PCLvl, PCDif, speed, windheading):
    ShipInput = ship_input(PCLvl, PCDif)
    NPCSTR = NPC_STR(PCLvl, PCDif)
    captain_1check, captain_2check = captain_checks(ShipInput, NPCSTR)
    shiphand1check, shiphand2check = shiphand_checks(ShipInput, NPCSTR)
    ship1weathermod, ship2weathermod = weathermod(speed, windheading, ShipInput)
    ship_advantage(captain_1check, captain_2check, shiphand1check, shiphand2check, ship1weathermod, ship2weathermod)
    return ShipInput, NPCSTR, captain_1check, captain_2check, shiphand1check, shiphand2check, ship1weathermod, ship2weathermod
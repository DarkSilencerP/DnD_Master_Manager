__author__ = 'Dark_Silencer_P'
__project__ = 'Main D&D 4e Program'

# LIST OF ALL IMPORTED MODULES
import dNroll
import WindWeather
import Initiative
import ShipAdvantage


"""
**************************************************** MAIN PROGRAM ******************************************************
Project: D&D DM Assistance Program: Main program
Start Date:
Script: Python

12/28:
This is the central program that coordinates the various modules to create the DMAid program. The goal is to develop a
program that will make certain things much easier for PC-assisted DMs. The project started innocently enough when I
tried to plan a ship battle in my D&D group, and noted that there were no 4e rules on ship combat per say. Looking
online, I found ideas for using the concept of "Ship Advantage" on forums as a way of doing the ship-equivalent of
initiative and turn order. The idea is that different sea conditions, and different skilled crews will be able to
outmaneuver the lesser ship; although the original idea called for just using captain and crew checks for this purpose,
and an early standalone form of the ShipAdvantage module did only do just that, I was captivated by the idea of
including weather in these calculations, and as a result, since I was writing the Python script anyways, why not do it?
And from there, I thought: "you know, initiative is always annoying..." So I made a script for initiative. And then I
realized I had a lot of separate scripts so I decided to combine them to make the first version of the "Ship Combat"
module included here. From there, it was only a small leap to make a standalone "Land Combat" module that was only for
initiative. Finally, since I had combat, why not try to make a module for non-combat assistance? And so we reach the
current state of the program, with a fully-functional combat assistance suite, and a stand-in for a future non-combat
expansion.
"""
"""
****************************************************** CHANGELOG *******************************************************
12/28:
    - Ship Combat (see log)
    - Main Program description created
    - Changelog created
    - To-do list created
    - Generous commenting added throughout

"""
"""
******************************************************** TO-DO *********************************************************
Short-term:
    - To all variables requiring numerical input: change them to not use int() immediately, and instead check first if
    input is numerical, and run int() if it is; otherwise, start a loop that will continuously ask for a value and
    refuse to let the user input any non-numerical input.
    - Learn databases and add database integration so that other ideas become easier to do.
    - Code and add a non-combat module.
Mid-Term:
    - Make a GUI for this whole thing.
Long-Term:
    - Make a variant for D20 and Pathfinder Rules
"""

run = True
while run:
    print('Welcome to Manny\'s Magical Master Manager!')
    PCNumb, PCLvl, PCDif = Initiative.PCInfo()
    command = input('What do you want to do? (SC) Ship Combat, (LC) Land Combat, (CS) City-Scape, (E) Exit:').lower()
    if command == '':
        while command == '':
            print("Didn't catch that, let's try this again.")
            command = input(
                'What do you want to do? (SC) Ship Combat, (LC) Land Combat, (CS) City-Scape, (E) Exit:').lower()
    if command == 'sc':
        """
        ************************************************ DESCRIPTION **************************************************
        This is the Ship Combat module. Currently, it calculates ship advantages, then allows a pause for DM to move
        ship units and perform ship attacks, then it asks if the ships are in PvP combat range. Once they are in range,
        every subsequent turn after ship actions are performed it rolls for initiative (only runs the first time the
        ships are in PvP range) and then lists the turn order and goes combatant by combatant.
        A full turn (turns after first instance) in Ship Combat consists of:
        1- Weather generated & odds of weather changing generated (Weather conditions change based on odds of changing)
        2- Ship Advantage calculated (If weather subsequently changes, ship advantage is recalculated)
        3- Check to see if ships are in PvP range, or if combat is finished
        4- Pause allowing DM to perform ship-actions
        5- If PvP range, roll for initiative (If in PvP range uses prior checks) (if out of PvP range, loops back to 1)
        6- Goes combatant-by-combatant, giving pauses to either perform actions and continue or end combat.
        7- If combat hasn't ended, loops back to 1 to begin new turn.
        """
        """
        ************************************************* CHANGELOG ***************************************************
        12/28:
            - Thoroughly commented code
            - Started changelog
            - Changed values of variables "i" and "o" to True and/or False rather than 1/0
            - Added various "print()" to code to make the print-outs look nicer
            - Changed the "if combat..." chains from one large "if-elif" series to several independent "if" loops to
              simplify the code a little by removing redundant parts; removed unnecessary "else: pass" statement.
            - Moved "print('End of turn') statement out to end of loop instead of end of individual if statements.
            - Moved "if combat[0] == 'f':" loop to right after the initial input to allow immediate termination if the
              DM decides to end combat, rather than continue pointlessly until the end of the loop.
            - Changed all "combat == X" statements to "combat[0] == X" to make the code less picky about input.
            - Added ability to end combat in middle of initiative order by importing "if fight..." code from LandCombat
        """
        print('Aye, matey!')
        turn = 1
        i = False  # "i" variable makes sure that initiative checks only occur the first time the ships are in combat
        # range, and never again throughout the looping of the program.
        o = False  # "o" variable directs the program to rerun ShipAdvantage if the wind speed or heading changes
        weather, windspeed, speed, windheading = WindWeather.windweather()
        # Generates the weather conditions and respective modifiers
        ShipInput, NPCSTR, captain_1check, captain_2check, shiphand1check, shiphand2check, \
        ship1weathermod, ship2weathermod = ShipAdvantage.allshipadv(PCLvl, PCDif, speed, windheading)
        # uses the weather modifiers and PC stats to calculated ship advantage
        odds = dNroll.rolld100()  # generates the odds of weather changing. In future versions, I should make this
        # dependent on weather conditions such that more chaotic weather increases change rate
        print('There is a', odds, '%', 'of a change in the wind speed or heading!')
        while command == 'sc':  # This is the beginning of the Turn
            print()
            print('*****', 'Turn:', turn, '*****')  # Declares the current turn
            print()
            combat = input('Are ships in PvP range? (Y/N/Finished)').lower()
            if combat == '':  # this way it doesn't crash if they send in blank code
                combat = 'n'
            if combat[0] == 'f':  # if combat's over it just ends the loop right here
                command = 'n'
                break
            print()
            if dNroll.rolld100() < odds:  # reruns windheading if fate demands it, sets "o" to True to order SA to rerun
                windheading = WindWeather.windheading()
                print('The wind\'s heading has changed! It is now', windheading)
                o = True  # upon changing to True it will direct the program to rerun ShipAdvantage stuff to account for
                #           the new changes to the weather.
            if dNroll.rolld100() < odds:  # reruns windspeed if fate demands it, sets "o" to True to order SA to rerun
                windspeed, speed = WindWeather.windspeed()
                print("The windspeed has changed!", windspeed)
                o = True  # upon changing to 1 it will direct the program to rerun ShipAdvantage stuff to account for the
                #        new changes to the weather.
            if o:  # reruns ShipAdvantage to adjust for the new weather conditions if they change
                ShipAdvantage.weathermod(speed, windheading, ShipInput)
                ShipAdvantage.ship_advantage(captain_1check, captain_2check, shiphand1check, shiphand2check,
                                             ship1weathermod, ship2weathermod)
                print()
            print('*****', "Begin Ship Combat", '*****')
            print()
            input('Press Enter to continue...')  # technically allows program to run given any button press but whatever
            print()
            if combat[0] == 'y' and i is False:  # only runs when its the first time PvP begins, rolls for initiative
                print('*****', "Begin Player Combat", '*****')
                print()
                PC = Initiative.initiative(PCNumb)  # acquires PC initiatives
                NPC = Initiative.npc_initiative()  # auto-rolls NPC initiatives given the initiative bonuses of each one
                InitOrder, initiative, InitList = Initiative.initorder(PC, NPC)  # creates the initiative order
                Initiative.initdisplay(InitOrder)  # displays the full initiative order in an neat fashion
                i = True  # by setting "i" to true I'm making sure that this loop never runs again
            if combat[0] == 'y' and i is True:
                Initiative.initdisplay(InitOrder)  # displays the full initiative order in an neat fashion
                print('*****', "Begin Player Combat", '*****')
                print()
                for n in InitList:  # loops through each player's turn and pauses for action before displaying the next
                    #                 player's turn; also allows end of combat during each pause
                    print(n, '\'s', 'turn')
                    fight = input('Press Enter to continue, F to end combat...').lower()  # pauses action until DM
                    #                                                                       responses
                    print()
                if fight == '':  # Stops it from crashing if they send it back blank
                    fight = 'y'
                if fight[0] == 'f':  # if the DM responds with anything starting with 'f' it ends the combat; implicit
                    #                  else condition that if they respond with anything else the loop continues
                    command = 'n'
                    break
            print('*****', "End of turn", '*****')
            print()
            turn += 1  # marks a new turn
            o = False  # in case it was set to true, this resets it to false so weather doesn't change unnecessarily
    elif command == 'lc':
        """
        ************************************************ DESCRIPTION **************************************************
        This is the Land Combat module. Its not very impressive, its simply the naked Initiative program without any
        real bells or whistles. Nonetheless, its a pretty vital part of the program since PvP is much, much more common
        than ship combat. First, it rolls for initiative, and then it loops through the
        """
        """
        ************************************************* CHANGELOG ***************************************************
        12/28:
            - Thoroughly commented code
            - Started changelog
            - Made the loop-break un-ignorable by the code by adding "fight"'s status as second requirement for the code
            to loop
            - Added the "if fight == ''" code to prevent crashing when users submit blank code.
            - Added print()'s for aesthetics.
            - Removed unnecessary "else: pass" lines
        """
        print('Alrighty then, roll for initiative!')
        PC = Initiative.initiative(PCNumb)  # acquires PC initiatives
        NPC = Initiative.npc_initiative()  # generates NPC initiatives from initiative bonus input
        InitOrder, initiative, InitList = Initiative.initorder(PC, NPC)  # calculates initiative order
        Initiative.initdisplay(InitOrder)  # displays initiative order in a neat fashion
        turn = 1  # the first turn is declared, of course
        fight = 'y'  # I'm basically making this loop-break bulletproof
        while command == 'lc' and fight == 'y':  # I had issues with this loop continuing no matter what I did, so
            # this takes care of that.
            print()
            print('***** Turn:', turn, '*****')  # declares the turn number
            print()
            for n in InitList:
                print(n, '\'s', 'turn')
                fight = input('Press Enter to continue, F to end combat...').lower()  # asks DM to either move to next
                # combatant or end combat
                print()
                if fight == '':  # added to prevent crashing from blank string inputs
                    fight = 'y'
                if fight[0] == 'f':  # ends the loop if combat ends.
                    command = 'n'
                    break
            print('*****', "End of turn", '*****')
            turn += 1
    elif command == 'cs':
        """
        12/28 -
        Hi there! I mean, its not like I don't have plans for this section. Rather, I have the issue that what I wanna
        do are beyond my skill for the moment. Gimme some time XD
        """
        print('YOU MUST CONSTRUCT ADDITIONAL PYLONS')
    elif command[0] == 'e':
        run = False
    else:
        print('Sorry, try again.')
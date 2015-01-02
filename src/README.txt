DnD_Master_Manager
==================

INTRO:

  Manny's Magical Master Manager is an aid to manage the small details of DMing for you, so you can focus on the real work. Currently available as a text-based interface, a GUI is planned eventually.

  The final aim is to develop a program that will make certain things much easier for PC-assisted DMs. The project started innocently enough when I tried to plan a ship battle in my D&D group, and noted that there were no 4e rules on ship combat per say. Looking online, I found ideas for using the concept of "Ship Advantage" on forums as a way of doing the ship-equivalent of initiative and turn order. The idea is that different sea conditions, and different skilled crews will be able to out-maneuver the lesser ship; although the original idea called for just using captain and crew checks for this purpose, and an early standalone form of the ShipAdvantage module did only do just that, I was captivated by the idea of
including weather in these calculations, and as a result, since I was writing the Python script anyways, why not do it? And from there, I thought: "you know, initiative is always annoying..." So I made a script for initiative. And then I realized I had a lot of separate scripts so I decided to combine them to make the first version of the "Ship Combat" module included here. From there, it was only a small leap to make a standalone "Land Combat" module that was only for initiative. Finally, since I had combat, why not try to make a module for non-combat assistance? And so we reach the current state of the program.

  The current program is structured as 3 main parts: Sea Combat (SC), which provided the initial inspiration for the program; Land Combat (LC); and CityScape (CS). Its worth noting that changelogs for each part are kept in comments inside the actual ".py" modules, as well as a detailed explanation of the module and functions.


SEA COMBAT MODULE:

  The SC module sources functions from various places: dice rolls come from "dNroll;" the wind heading, speed, and weather conditions all come from functions in "WindWeather;" the main functions that determine ship advantage are in "ShipAdvantage;" and for PvE combat, it uses the initiative functions found in "Initiative." Currently, it calculates ship advantages, then allows a pause for DM to move ship units and perform ship attacks, then it asks if the ships are in PvP combat range. Once they are in range, every subsequent turn after ship actions are performed it rolls for initiative (only runs the first time the ships are in PvP range) and then lists the turn order and goes combatant by combatant.
  A full turn (or turns after first instance) in Ship Combat consists of:
    1 - Weather generated & odds of weather changing generated (Weather conditions change based on odds of changing)
    2 - Ship Advantage calculated (If weather subsequently changes, ship advantage is recalculated)
    3 - Check to see if ships are in PvP range, or if combat is finished
    4 - Pause allowing DM to perform ship-actions
    5 - If PvP range, roll for initiative (If in PvP range uses prior checks) (if out of PvP range, loops back to 1)
    6 - Goes combatant-by-combatant, giving pauses to either perform actions and continue or end combat.
    7 - If combat hasn't ended, loops back to 1 to begin new turn.

    Combat can end at several points during SC. When it does, the loop containing the SC ends, and the program goes back to the beginning.

  Its worth noting that this module is essentially finished. I have a wish-list of things to modify about it, however.
  Things to add to ShipAdvantage (in order of priority):
	- Increase the weight of the wind heading on advantage;
	- Increase the weight of the captain's check on advantage;
	- Decrease the weight of individual non-captain checks such that they are no longer exorbitantly overweighted;
	- Add ship-based modifiers to ShipAdvantage such that Manuverability > Speed >> Size affect advantage;
	- Add more comments.


LAND COMBAT MODULE:

  The LD module uses only commands in "Initiative," since all it does is roll for and manage Initiative. It works by asking for the names and respective initiative checks of each player, followed by asking for the number, names, and initiative bonuses of the NPCs in combat - it adds these bonuses to a d20 roll it makes to speed things up. It then sorts all the players and NPCs by order of descending initiative, and calls each combatant one-by-one, waiting for the DM to either continue the list at the end of their turn, or end combat.

  Things to add to the LC:
  - Allow DM to create and pre-load an .ini file with the monster names and initiative bonuses, to make that even smoother.


CITYSCAPE MODULE:

  Currently still in the works, see the Future Additions section for ideas!


OTHER MODULES:

  dNroll:
    The first module made, its just your normal random number generator, set up to imitate polyhedral dice. Would be nice if     it could be called whenever in the program to just have a polyhedral role on command.
  WindWeather:
    It uses dNroll to create random weather conditions. Could use some work for making it a bit more DM friendly.
  MainCompilationProgram:
    What it sounds like, its the main program tying all the modules together into one interface.


FUTURE ADDITIONS:
  - Make the function and variable names fit in-line with common Python practices.
  - CityScape Module, complete with Village Generator, Merchant Inventory Generator, NPC Generator, Name Generator, and much        more!
  - Notepad, for jotting session notes.
  - A GUI version of the program, one that ideally will have the various modules as their own semi-independent windows so        that the DM can arrange them as he wishes.
  - Maybe make Spanish and French versions, who knows.
  - Other suggestions!

SUGGESTIONS:
  I'm very receptive to suggestions for additional modules to this program. As it stands, there are other things I have noted in the files' wishlists that indicate my own ideas, which I may have failed to note here. However, at the same time, I want this to be a useful and straight-forward tool, which means that at some point, I can't incorporate every single idea into the program, or else it would probably suffer from Swiss-Army-Knife Syndrome. Still, lemme know if you have an idea!
__author__ = 'Dark_Silencer_P'
__project__ = 'Initiative'

from operator import itemgetter  # itemgetter is a fast way of getting the item from a list or tuple, and here, serves
# the vital function of getting the Init out of the list of tuples, and is used to sort
# the list by initiative.
import dNroll

"""
    - PCInfo() defines three variables, PCNumb, PCLvl, and PCDif, for the sake of collecting info for the encounter.
    Always unpack with:
        PCNumb, PCLvl, PCDif = PCInfo()
    - initiative() has one argument, PCNumb. It creates a blank list, PC, and then uses a for loop with the range PCNumb
    to ask for the name and  initiative check of every PC character. It then outputs the list as PC
    Unpack with:
        PC = initiative(PCNumb)
    - npc_initiative() does the same as initiative(), except that it asks for the NPC number as well, and automatically
    makes the initiative check after asking for the initiative bonus.
    Unpack with:
        NPC = npc_initiative()
    - initorder() takes two arguments, PC and NPC, which are lists. It then takes the two lists, combines them, sorts
    them by initiative from largest to smallest using itemgetter() and reverse=True, and then for convenience it also
    unzips the list of tuples to get a list of names and a list of initiatives in order.
    Unpack with:
        InitOrder, initiative, InitList = initorder(PC, NPC)
    - tuple_init() just packages everything into a tuple again for convenience.
    Unpack with:
        tuple_init=tuple_init()
    - initdatavomit() does exactly what the name implies here, nuff said. XD
"""


def PCInfo():
    # First thing's first, let's find out how many PC characters there are
    PCNumb = int(input('How many PCs are in the party?'))
    # Next, what's the party level
    PCLvl = int(input('What is the party level?'))
    # Next, what's the difficulty of this encounter?
    PCDif = int(input('What is the difficulty of the party?'))
    # Now, we return a tuple that has 3 parts: PCNumb, PCLvl, and PCDif
    return PCNumb, PCLvl, PCDif


def initiative(PCNumb):
    # Because we already have the player number courtesy of PCInfo(), make a loop that prompts for PC name and init
    PC = []
    for k in range(PCNumb):  # creates a new entry into PC for every player in the battle
        Name = input('Player:')
        Init = int(input('Initiative:'))
        PC.append((Name, Init))
        k += 1
    return PC


def npc_initiative():
    NPC = []
    for j in range(int(input('How many NPCs are there?'))):  # to do the same as in initiative(), we need to ask for the
        #                                                      number of NPCs involved, so I made the question part of
        #                                                      the range to economize lines of code.
        Name = input('Enemy:')
        Init = dNroll.rolld20() + int(input("Initiative bonus:"))
        NPC.append((Name, Init))
        j += 1
    return NPC


def initorder(PC, NPC):  # this initorder uses itemgetter and reverse=true to sort the list
    InitOrder = sorted(PC + NPC, key=itemgetter(1), reverse=True)  # create unified list and sort by initiative
    # see itemgetter explanation at import section
    InitList, initiative = zip(*InitOrder)  # zip(*[list]) takes a list of lists and unzips it into its parts. Here, it
    #                                       takes InitOrder, and it breaks it down into its constituent tuple pairs. It
    #                                       then saves the first number of each tuple, Name, and stores the list of all
    #                                       the names into InitList, and then it takes the second value of all tuples,
    #                                       Init, and it saves it under initiative.
    return InitOrder, initiative, InitList


def tuplize_init(PCNumb, PCLvl, PCDif, PC, InitOrder, initiative, InitList):
    tuple_init = (PCNumb, PCLvl, PCDif, PC, InitOrder, initiative, InitList)
    return tuple_init


def initdatavomit(tuple_init):
    PCNumb, PCLvl, PCDif, PC, k, InitOrder, initiative, InitList = tuple_init
    print('Here are all the variables contained in the initiative module:')
    print("PCNumb:", PCNumb)
    print("PCLvl:", PCLvl)
    print("PCDif:", PCDif)
    print("PC:", PC)
    print("initiative:", initiative)
    print("InitOrder:", InitOrder)
    print("InitList:", InitList)


def initdisplay(InitOrder):
    print("The initiative order is:")
    for index, (a, b) in enumerate(InitOrder):
        print((index + 1), ":", b, "(" + a + ")")


"""
*** Test run code: ***
PCNumb, PCLvl, PCDif = PCInfo()
PC = initiative(PCNumb)
NPC = npc_initiative()
InitOrder, initiative, InitList = initorder(PC, NPC)
tupleinit = tuplize_init(PCNumb, PCLvl, PCDif, PC, InitOrder, initiative, InitList)
initdatavomit(tupleinit)
initdisplay(InitOrder)
"""
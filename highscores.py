#!/bin/python

import urllib2

url = "http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player=eras"
content = urllib2.urlopen(url)

content = content.read()
content = content.split("\n")
attack = content[1].split(",")
defence = content[2].split(",")
strength = content[3].split(",")
hitpoints = content[4].split(",")
ranged = content[5].split(",")
prayer = content[6].split(",")
magic = content[7].split(",")
cooking = content[8].split(",")
woodcutting = content[9].split(",")
fletching = content[10].split(",")
fishing = content[11].split(",")
firemaking = content[12].split(",")
crafting = content[13].split(",")
smithing = content[14].split(",")
mining = content[15].split(",")
herblore = content[16].split(",")
agility = content[17].split(",")
theiving = content[18].split(",")
slayer = content[19].split(",")
farming = content[20].split(",")
runecraft = content[21].split(",")
hunter = content[22].split(",")
construction = content[23].split(",")

alist = [attack, defence, strength, hitpoints, ranged, prayer, magic, cooking, woodcutting, fletching, fishing, firemaking, crafting, smithing, mining, herblore, agility, theiving, slayer, farming, runecraft, hunter, construction]

for line in alist:
    print(line[1])

# ****************************************************************
# Blender Game Engine Python Code - Kerker-Generator
# Script by MrLarodos: http://www.youtube.com/user/MrLarodos
#
# Released under the Creative Commons Attribution 3.0 Unported License:
# http://creativecommons.org/licenses/by/3.0/de/
# http://creativecommons.org/licenses/by/3.0/
#
# If you use this code or parts of it, you have to include this information header.
#
# DEUTSCH:
# Wenn Du dieses Script oder Teile davon benutzt, musst Du diesen Infoteil im Script lassen.
# ****************************************************************

import GameLogic
import random

fields = {}
cont = GameLogic.getCurrentController()
own = cont.owner

adder = cont.actuators['adder']

trigger = cont.sensors['trigger']

if trigger.positive:
# ****************************************************************
    #START in diesem Block können Änderungen durchgeführt werden
    fieldsize_x = 50    #Spielfeldbreite in Feldern X-Achse
    fieldsize_y = 50    #Spielfeldbreite in Feldern Y-Achse
    block_count = 500   #Anzahl Blöcke auf Spielfeld
    chance=10           #Zusätzliche Chance Richtung beizubehalten
    #ENDE in diesem Block können Änderungen durchgeführt werden
# ****************************************************************
    
    for x_wert in range(0, fieldsize_x+2):
        for y_wert in range(0, fieldsize_y+2):
            fields[x_wert,y_wert]=0
            #print("xwert:"+str(x_wert)+" - ywert:"+str(y_wert))
    
    fieldsmax=fieldsize_x*fieldsize_y
    
    if block_count>fieldsmax:block_count=fieldsmax
    
    startfield_x = 1
    startfield_y = 1
    
    fields[startfield_x,startfield_y]=1
    
    aktuellesfeld_x=startfield_x
    aktuellesfeld_y=startfield_y
    
    x=0
    y=1
    lastdirection=1
    
    wert=1
    
    while wert<block_count:
        
        zufalldone=0
        
        while zufalldone==0:
            zufall=random.randint(1, 4+chance)
            #print("Zufallszahl: "+str(zufall))
            
            if zufall==1 and lastdirection!=3:
                x=0
                y=1
                lastdirection=1
                newval=True
            elif zufall==2 and lastdirection!=4:
                x=1
                y=0
                lastdirection=2
                newval=True
            elif zufall==3 and lastdirection!=1:
                x=0
                y=-1
                lastdirection=3
                newval=True
            elif zufall==4 and lastdirection!=2:
                x=-1
                y=0
                lastdirection=4
                newval=True
            elif zufall>4:
                x=x
                y=y
                newval=True
            else:
                newval=False
            
            if (aktuellesfeld_x+x)<=(fieldsize_x) and (aktuellesfeld_x+x)>=1 and (aktuellesfeld_y+y)<=(fieldsize_y) and (aktuellesfeld_y+y)>=1 and newval==True:
                zufalldone=1
                blockset=1
                fields[aktuellesfeld_x,aktuellesfeld_y]=1
                aktuellesfeld_x+=x
                aktuellesfeld_y+=y
                
        wert+=blockset
    
    #START BLÖCKE SETZEN
    ursprung_x=own.worldPosition[0]
    ursprung_y=own.worldPosition[1]
    
    for x_wert in range(1, fieldsize_x+1):
        for y_wert in range(1, fieldsize_y+1):
            if fields[x_wert,y_wert]==1:
                
                own.worldPosition[0]=ursprung_x+(x_wert*2)
                own.worldPosition[1]=ursprung_y+(y_wert*2)
            
                #START BODEN & DECKE EINFÜGEN
                adder.object="floor"
                adder.instantAddObject()
                adder.object="ceiling"
                adder.instantAddObject()
                #ENDE BODEN & DECKE EINFÜGEN
                
                #START WÄNDE EINFÜGEN
                if fields[x_wert,y_wert+1]==0:
                    adder.object="wall_n"
                    adder.instantAddObject()
                if fields[x_wert,y_wert-1]==0:
                    adder.object="wall_s"
                    adder.instantAddObject()
                if fields[x_wert+1,y_wert]==0:
                    adder.object="wall_e"
                    adder.instantAddObject()
                if fields[x_wert-1,y_wert]==0:
                    adder.object="wall_w"
                    adder.instantAddObject()
                #ENDE WÄNDE EINFÜGEN
                
                #START GEMÄLDE EINFÜGEN
                piczufall=random.randint(1, 40)
                if piczufall==1:
                    if fields[x_wert,y_wert+1]==0:
                        adder.object="painting_larodos_n"
                        adder.instantAddObject()
                    elif fields[x_wert,y_wert-1]==0:
                        adder.object="painting_larodos_s"
                        adder.instantAddObject()
                    elif fields[x_wert+1,y_wert]==0:
                        adder.object="painting_larodos_e"
                        adder.instantAddObject()
                    elif fields[x_wert-1,y_wert]==0:
                        adder.object="painting_larodos_w"
                        adder.instantAddObject()
                #ENDE GEMÄLDE EINFÜGEN
                
                #START POLLER EINFÜGEN
                if fields[x_wert,y_wert+1]==1 and fields[x_wert+1,y_wert]==0 and fields[x_wert-1,y_wert]==0 and fields[x_wert+1,y_wert+1]==1 and fields[x_wert-1,y_wert+1]==1:
                    adder.object="poller_n"
                    adder.instantAddObject()
                if fields[x_wert,y_wert-1]==1 and fields[x_wert+1,y_wert]==0 and fields[x_wert-1,y_wert]==0 and fields[x_wert+1,y_wert-1]==1 or fields[x_wert,y_wert-1]==1 and fields[x_wert+1,y_wert]==0 and fields[x_wert-1,y_wert]==0 and fields[x_wert-1,y_wert-1]==1:
                    adder.object="poller_s"
                    adder.instantAddObject()
                if fields[x_wert+1,y_wert]==1 and fields[x_wert,y_wert+1]==0 and fields[x_wert,y_wert-1]==0 and fields[x_wert+1,y_wert+1]==1 and fields[x_wert+1,y_wert-1]==1:
                    adder.object="poller_e"
                    adder.instantAddObject()
                if fields[x_wert-1,y_wert]==1 and fields[x_wert,y_wert+1]==0 and fields[x_wert,y_wert-1]==0 and fields[x_wert-1,y_wert+1]==1 or fields[x_wert-1,y_wert]==1 and fields[x_wert,y_wert+1]==0 and fields[x_wert,y_wert-1]==0 and fields[x_wert-1,y_wert-1]==1:
                    adder.object="poller_w"
                    adder.instantAddObject()
                #ENDE POLLER EINFÜGEN
                
                if x_wert!=startfield_x and y_wert!=startfield_y:
                    #START FEINDE EINFÜGEN
                    enemyzufall=random.randint(1, 10)
                    if enemyzufall==1:
                        own.worldPosition[2]=own.worldPosition[2]+0.5
                        
                        enemyzufallchoice=random.randint(1, 4)
                        
                        if enemyzufallchoice==1:adder.object="player.000"
                        if enemyzufallchoice==2:adder.object="player.001"
                        if enemyzufallchoice==3:adder.object="player.002"
                        if enemyzufallchoice==4:adder.object="player.003"
                        
                        adder.instantAddObject()
                        own.worldPosition[2]=own.worldPosition[2]-0.5
                    #ENDE FEINDE EINFÜGEN
                    
                    #START DEKO EINFÜGEN
                    dekozufall=random.randint(1, 100)
                    if dekozufall==1:
                        adder.object="kiste.000"
                    if dekozufall==2:
                        adder.object="kiste.001"
                    if dekozufall==3:
                        adder.object="kiste.002"
                    if dekozufall==4:
                        adder.object="kiste.003"
                    if dekozufall<5:adder.instantAddObject()
                    #ENDE DEKO EINFÜGEN
    #ENDE BLÖCKE SETZEN
        
    own.worldPosition[0]=0
    own.worldPosition[1]=0
    print("Fertig!")

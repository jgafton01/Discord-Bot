import psycopg2

conn = psycopg2.connect(database="postgres",
                        host="localhost",
                        user="postgres",
                        password="adminadmin",
                        port="5432")

cursor = conn.cursor()

GAMESSQL = cursor.execute("SELECT * FROM games")

Result = cursor.fetchall() 

from asyncio.windows_events import NULL
import random

#2-D array of games and scores  
Games2 =[["Forza Horizion 5",5.25],["Ghost Watchers",5],["Overwatch 2",6],["Boo Men",5.5],["V Rising",4.25],["SCP Pandemic",4.25],
["Tom Clancy's Wild Land",4.5],["Ready Or Not",6],["Elden Ring",5.25],["Red Dead Redemption 2",5.25],["Skater XL",5.25],["Warhammer 40k Darktide",5],["Mordhau",5.25],["Golf it",4.5],["THUG PRO",5],["Crab Game",4.25],["Mount and Blade Bannerlord",5.5],["Apex Legends",4.75],["In Silence",4.5],["Cry Of Fear",3],["Sign of Silence",4.25],["Inside the Backrooms",5.25],["Labyrinthine",4],["Valheim",3.25],["Hunt showdown",4.75],["Warzone",5.75],["Tekken 7",5.25],["Multiverses",4.75],["Five M",5.75],["Back 4 Blood",5],["Gladio and Glory",5.5],["For Honour",5.5],["Skyrim Co-Op",5.75],["Prison Architect",6.5],["Fall Guys",5.25],["Gang Beasts",5.25],["Age Of Empires II",6.25],["Dead Frontier 2",1],["Dead By Deadlight",6.25],["Killing Floor 2",6.75],["Competitve Euro Truck Sim 2",3.5],["Rainbow Six Vegas 2",5.5],["Sea Of Thieves",6.25],["GTA Online",5],["Minecraft",6.5],["Monopoly",3.25],["Modded Skate 3",3.5],["Dead By Daylight",6.25]]
games3 =[]
#array only stores games that meet criteria - Change to GameswCriteria

for game in Result:
    if game[2] > 4 :
        games3.append(game)
    

#Games = list (("Forza Horizion 5","Ghost watchers","Overwatch 2","Boo Men","V Rising","SCP Pandemic","Tom Clancys Wild Land","Ready Or Not" ,"Elden Ring","Red Dead Redemption 2","Skater XL","Warhammer 40k Darktide","Mordhau","Golf it","THUG Pro","Crab Game","Mount and Blade Bannerlord","Apex Legends","In Silence","Cry of fear coop" ,"Sign of Silence" ,"Inside the Backrooms","Labyrinthine","Valheim","Hunt Showdown","Shatterline","Warzone","Tekken 7","Multiverses","Five M","Back 4 Blood","Drunken Wrestlers","Gladio and Glory","For Honor","Skyrim CoOp","Prison Architect","Fall Guys","Gang Beasts"))
#print("original list is : "+str(Games))

rand_idx = random.randrange(len(games3))
random_num = games3[rand_idx][1]

#games3.remove(0)
print("Random selected Number is : " + str(random_num))







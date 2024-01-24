import psycopg2

conn = psycopg2.connect(database="postgres",
                        host="localhost",
                        user="postgres",
                        password="adminadmin",
                        port="5432")

cursor = conn.cursor()

GAMESSQL = cursor.execute("SELECT * FROM games")

Result = cursor.fetchall() 

import random

games3 =[]

for games in Result:
    if games[2] > 3 :
        games3.append(games)
    
    rand_idx = random.randrange(len(games3))
random_num = games3[rand_idx][1]

print("Random selected Number is : " + str(random_num))

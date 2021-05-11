# Package importing

import time
import psycopg2
import os
import sys

# Basic function call API
def createGame(gameName, gameType, conn) -> int:
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO public."GAME_ENGINE"("GAMENAME", "GAMETYPE", "STARTEDON") VALUES (' '''+ gameName +''' ',' '''+ gameType +''' ', NOW());''')
    cursor.execute('''SELECT * FROM public."GAME_ENGINE"''')
    totalData = cursor.fetchall()
    return totalData

def addPlayer(playerName, conn):
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO public."PLAYERS"("PLAYERNAME", "STARTDATE") VALUES (' '''+ playerName +''' ', NOW());''')
    cursor.execute('''SELECT * FROM public."PLAYERS"''')
    totalData = cursor.fetchall()
    return totalData


def takeTimeAndClear(sec) -> bool:
    time.sleep(sec)
    osv = sys.platform
    if osv == 'win32':
        os.system('cls')
        return True
    else:
        os.system('clear')
        return True
    return False


def startCount(num):
    return str("⭐" * num)


# Getting connection
conn = psycopg2.connect(database='Personal', user='vivekvijayan', password='Uzumymw@9841', host='127.0.0.1')
conn.autocommit = True
if conn:
    print('\n\n ✅ Connection established - POSTGRESQL DB SERVER')
    
else:
    print('\n\n ❌ Connection Failed, please check the configuration file')
    exit()

takeTimeAndClear(2)

# Option Part



while True:
    takeTimeAndClear(0)
    # Getting Data from the postgresql
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM public."PLAYERS"''')
    total_players_information = cursor.fetchall()
    cursor.execute('''SELECT "GAMEID", "GAMENAME" FROM public."GAMESET" ORDER BY "GAMEID" DESC LIMIT 1 ''')
    activeGame = cursor.fetchall()

    cursor.execute('''SELECT "GAMEID", "PLAYERID", SUM("SCORE") FROM public."GAMEPLAY" GROUP BY "GAMEID", "PLAYERID", "SCORE" HAVING "GAMEID" = ''' + str(activeGame[0][0]) )
    gameplay = cursor.fetchall()

    print('''
        🔥 CARD GAME TRACKER 🔥 
        ------------------------

        *    Developer : Vivek Vijayan
        *    Version   : 1.0.0  


        SCORE BOARD
        -----------
        User ID    PlayerName    Star
        ----------------------------- ''')

    for x in range(0, int(len(total_players_information))):
        print('''         ''' + str(total_players_information[x][0]) + '''        ''' +  str(total_players_information[x][1]) + '''    ''' + startCount(total_players_information[x][2]))
    print('''

        ACTIVE GAME : ''' + str(activeGame[0][0]) + ''' 👉 ''' + str(activeGame[0][1]) + '''

        CURRENT SCORE
        -------------
    ''')
    for x in range(0, int(len(gameplay))):
        print('''\tUSER ID : ''' + str(gameplay[x][1]) + '''   SCORE :   ''' +  str(gameplay[x][2]) )

    cursor.execute('''SELECT e."PLAYERNAME", g."SCORE" FROM public."GAMEPLAY" g join public."PLAYERS" e on g."PLAYERID" = e."PLAYERID"  where"GAMEID" = ''' + str(activeGame[0][0]) + ''' order by "GAMEPLAYID" desc limit 3  ''' )
    gameplayTop3 = cursor.fetchall()


    print('\n\n\t LAST 3 GAMEPLAY \n\t-------------------------------')
    for x in gameplayTop3:
        print("\t🟢 Winner : " + str(x[0]) + "    SCORE : " + str(x[1]))

    if gameplayTop3[0][0] == gameplayTop3[1][0] and gameplayTop3[2][0] != gameplayTop3[0][0]:
        print("\n\n\t 🔥 ON A HATRICK 🔥")

    option_1 = int(input(': ')) 







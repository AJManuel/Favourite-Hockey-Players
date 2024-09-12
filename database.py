import sqlite3

createPlayerTable = 'CREATE TABLE IF NOT EXISTS favourite_players (id INTEGER PRIMARY KEY, name TEXT, team TEXT, number INTEGER);'

baseSet = 'INSERT INTO favourite_players (name,team,number) VALUES("John Tavares", "Toronto Maple Leafs", 91);'

insertPlayers = 'INSERT INTO favourite_players (name,team,number) VALUES(?,?,?);'

getAllPlayers = 'SELECT * FROM favourite_players;'

getPlayersFromName = 'SELECT * FROM favourite_players WHERE name = ?;'

# getBestPrepMethod = """
# SELECT * FROM beans
# WHERE name = ?
# ORDER BY rating DESC
# LIMIT 1;
# """

deleteAll = 'DROP TABLE data;'

def connect():
    return sqlite3.connect('data.db')

def createTables(connection):
    with connection:
        connection.execute(createPlayerTable)

def addDataSet(connection):
    with connection:
        connection.execute(baseSet)

def addPlayers(connection,name,team,number):
    with connection:
        connection.execute(insertPlayers,(name,team,number))

def getThePlayers(connection):
    with connection:
        return connection.execute(getAllPlayers).fetchall()
    
def getPlayersByName(connection, name):
    with connection:
        return connection.execute(getPlayersFromName, (name,)).fetchall()
    
# def getBestBeanPrep(connection,name):
#     with connection:
#         return connection.execute(getBestPrepMethod, (name,)).fetchone()
    
def deleteFunc(connection):
    with connection:
        connection.execute(deleteAll)
    
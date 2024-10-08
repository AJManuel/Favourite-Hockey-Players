import sqlite3

createPlayerTable = 'CREATE TABLE IF NOT EXISTS favourite_players (id INTEGER PRIMARY KEY, name TEXT, team TEXT, number INTEGER);'

baseSet = """INSERT INTO favourite_players (name,team,number) VALUES("John Tavares", "Toronto Maple Leafs", 91),
("Auston Matthews","Toronto Maple Leafs",34),
("Connor Mcdavid", "Edmonton Oilers",97),
("Adam Fox", "New York Rangers",23),
("Viktor Arvidsson", "Edmonton Oilers",33),
("Tobias Bjornfort", "Florida Panthers",2),
("Brendan Lemieux", "Carolina Hurricanes",22),
("Timo Meier", "New Jersey Devils",28),
("Brock Boeser", "Vancouer Canucks",6),
("Jani Hakanpaa", "Toronto Maple Leafs", 2);"""

insertPlayers = 'INSERT INTO favourite_players (name,team,number) VALUES(?,?,?);'

getAllPlayers = 'SELECT * FROM favourite_players;'

getPlayersFromName = 'SELECT * FROM favourite_players WHERE name = ?;'

deletePlayerFromTableByName = 'DELETE FROM favourite_players WHERE name = ?;'

# getBestPrepMethod = """
# SELECT * FROM beans
# WHERE name = ?
# ORDER BY rating DESC
# LIMIT 1;
# """

sortPlayersByName = 'SELECT * FROM favourite_players ORDER BY name ASC;'

sortPlayersByTeam = 'SELECT * FROM favourite_players ORDER BY team ASC;'

sortPlayersByNum = 'SELECT * FROM favourite_players ORDER BY number ASC;'

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
    
def getPlayersSortedName(connection):
    with connection:
        return connection.execute(sortPlayersByName).fetchall()

def getPlayersSortedTeam(connection):
    with connection:
        return connection.execute(sortPlayersByTeam).fetchall()
    
def getPlayersSortedNum(connection):
    with connection:
        return connection.execute(sortPlayersByNum).fetchall()
    
def getPlayersByName(connection, name):
    with connection:
        return connection.execute(getPlayersFromName, (name,)).fetchone()
    
def deletePlayerFromTableByNameFunc(connection, name):
    with connection:
        return connection.execute(deletePlayerFromTableByName, (name,)).fetchone()
    
   
# def getBestBeanPrep(connection,name):
#     with connection:
#         return connection.execute(getBestPrepMethod, (name,)).fetchone()
    
def deleteFunc(connection):
    with connection:
        connection.execute(deleteAll)
    

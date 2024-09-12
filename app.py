import database
import tkinter as tk
from tkinter import *


window = tk.Tk()
window.title('Placeholder')
window.geometry("700x700")

menuPrompt = """Favourite Hockey Players

Please choose one of these options:

1) Add a new player
2) See all player
3) Find a player by name
4) See which preparation method is best for a bean
5) Exit.

Your selection:"""

def menu():
    connection = database.connect()
    database.createTables(connection)
    database.addDataSet(connection)

    while (user_input := input(menuPrompt)) != "5":
        if user_input == "1":
            name = input("Enter Players name: ")
            team = input("Enter how you have prepared it: ")
            number = int(input("Enter player number: "))

            database.addPlayers(connection,name,team,number)
        elif user_input == "2":
            players = database.getThePlayers(connection)

            for player in players:
                print(f"{player[1]} ({player[2]}) - {player[3]}")

        elif user_input == "3":
            name = input("Enter player name to find: ")
            players = database.getPlayersByName(connection, name)

            for player in players:
                print(f"{player[1]} ({player[2]}) - {player[3]}")
        elif user_input == "4":
            pass
            # name = input("Enter player name to find: ")
            # bestMethod = database.getBestBeanPrep(connection,name)

            # print(f"The best prep method for {name} is {bestMethod[2]}")
        else:
            print('Invalid Input')

def endAll():
    connection = database.connect()
    database.deleteFunc(connection)


def addPage():
    connection = database.connect()


menu()
window.mainloop()
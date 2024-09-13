import database
import tkinter as tk
from tkinter import *
from tkinter import ttk
import notebook


window = tk.Tk()
window.title('Placeholder')
window.geometry("700x700")

notebook = ttk.Notebook(window)
tab1 = Frame(notebook)
tab2 = Frame(notebook)
tab3 = Frame(notebook)

notebook.add(tab1, text="Home")
notebook.add(tab2, text="Players")
notebook.add(tab3, text="Sort/Search")



menuPrompt = """Favourite Hockey Players

Please choose one of these options:

1) Add a new player
2) See all player
3) Find a player by name
4) See which preparation method is best for a bean
5) Exit.

Your selection:"""

connection = database.connect()

def menu():
    #connection = database.connect()
    global connection
    database.createTables(connection)
    database.addDataSet(connection)

    while (user_input := input(menuPrompt)) != "5":
        if user_input == "1":
            name = addPlayerNameEntryBox.get()
            team = addPlayerTeamEntryBox.get()
            number = addPlayerNumberEntryBox.get()
            #name = input("Enter Players name: ")
            #team = input("Enter how you have prepared it: ")
            #number = int(input("Enter player number: "))

            database.addPlayers(connection,name,team,number)
        elif user_input == "2":
            players = database.getThePlayers(connection)

            for player in players:
                print(f"{player[1]} ({player[2]}) - {player[3]}")

        elif user_input == "3":
            name = input("Enter player name to find: ")
            players = database.getPlayersByName(connection, name)
            #print(players)
            # for player in players:
            #     #print(player)
            print(f"{players[1]} ({players[2]}) - {players[3]}")
        elif user_input == "4":
            pass
            # name = input("Enter player name to find: ")
            # bestMethod = database.getBestBeanPrep(connection,name)

            # print(f"The best prep method for {name} is {bestMethod[2]}")
        else:
            print('Invalid Input')
    
def enterIntoData():
    name = addPlayerNameEntryBox.get()
    team = addPlayerTeamEntryBox.get()
    number = addPlayerNumberEntryBox.get()
    database.addPlayers(connection,name,team,number)

titleLabel = tk.Label(master=window, text='Favourite Hockey Players')
titleLabel.grid(column=2, row=0)

addPlayerNameEntryBox = tk.Entry(master=window, text='Add Your Favourite Players Name')
addPlayerNameEntryBox.grid(column=2,row=2)

addPlayerTeamEntryBox = tk.Entry(master=window, text='Add Your Favourite Players Team')
addPlayerTeamEntryBox.grid(column=4,row=2)

addPlayerNumberEntryBox = tk.Entry(master=window, text='Add Your Favourite Players Number')
addPlayerNumberEntryBox.grid(column=6,row=2)

addPlayerInsertButton = tk.Button(master=window, text='Add To Database', command=enterIntoData)
addPlayerInsertButton.grid(column=2,row=4)

def endAll():
    connection = database.connect()
    database.deleteFunc(connection)


def addPage():
    connection = database.connect()



menu()
notebook.pack()
window.mainloop()

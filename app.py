import database
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import notebook


window = tk.Tk()
window.title('Placeholder')
window.geometry("300x500")

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

def clearFrame():
    for widget in window.winfo_children():
        widget.destroy()

def menu():
    #connection = database.connect()
    global connection
    database.createTables(connection)
    #database.addDataSet(connection)

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

def addPlayerPage():
    clearFrame()
    entryNameText = tk.StringVar()
    addPlayerNameEntryBox = tk.Entry(master=window, textvariable=entryNameText, width=30)
    entryNameText.set("Enter A Players Name")
    addPlayerNameEntryBox.grid(column=2,row=2, pady=10, padx=60)

    entryTeamText = tk.StringVar()
    addPlayerTeamEntryBox = tk.Entry(master=window, textvariable=entryTeamText, width=30)
    entryTeamText.set("Enter The Players Team")
    addPlayerTeamEntryBox.grid(column=2,row=4, pady=10, padx=60)

    entryNumberText = tk.StringVar()
    addPlayerNumberEntryBox = tk.Entry(master=window, textvariable=entryNumberText, width=30)
    entryNumberText.set("Enter The Players Number")
    addPlayerNumberEntryBox.grid(column=2,row=6, pady=10, padx=60)


    def enterIntoData():
        name = addPlayerNameEntryBox.get()
        team = addPlayerTeamEntryBox.get()
        number = addPlayerNumberEntryBox.get()
        if name or team or number == "":
            print('error')
            pass
        database.addPlayers(connection,name,team,number)
        messagebox.showinfo("Success", "Player Added")

    addPlayerInsertButton = tk.Button(master=window, text='Add To Database', command=enterIntoData)
    addPlayerInsertButton.grid(column=2,row=8, pady=10, padx=75)

def addViewPage():
    clearFrame()
    playerNameLabel = tk.Label(master=window, text="Player")
    playerNameLabel.grid(column=2, row=2)

    playerTeamLabel = tk.Label(master=window, text="Team")
    playerTeamLabel.grid(column=3, row=2)

    playerNumberLabel = tk.Label(master=window, text="Number")
    playerNumberLabel.grid(column=4, row=2)

    players = database.getThePlayers(connection)
    for i,e in enumerate(players):
    
        playerNameGrid = tk.Label(master=window, text=e[1])
        playerNameGrid.grid(row=4 + i,column=2)

        playerTeamGrid = tk.Label(master=window, text=e[2])
        playerTeamGrid.grid(row=4 + i,column=3)

        playerNumberGrid = tk.Label(master=window, text=e[3])
        playerNumberGrid.grid(row=4 + i,column=4)
    
    pass

def addSearchPage():
    clearFrame()
    addPlayerSearchBox = tk.Entry(master=window, text='Test')
    addPlayerSearchBox.grid(column=2,row=2)

    def searchName():
        name = addPlayerSearchBox.get()
        players = database.getPlayersByName(connection, name)

        print(players[2])

        playerNameLabel = tk.Label(master=window, text="Player")
        playerNameLabel.grid(row=4,column=2)

        playerNameAns = tk.Label(master=window, text=players[1])
        playerNameAns.grid(row=5,column=2)

        playerTeamLabel = tk.Label(master=window, text="Team")
        playerTeamLabel.grid(row=4,column=3)

        playerTeamAns = tk.Label(master=window, text=players[2])
        playerTeamAns.grid(row=5,column=3)

        playerNumberLabel = tk.Label(master=window, text="Number")
        playerNumberLabel.grid(row=4,column=4)

        playerNumberAns = tk.Label(master=window, text=players[3])
        playerNumberAns.grid(row=5,column=4)

    def mytest():
        try: 
            searchName()
        except TypeError:
            print('Error')
            playerErrorLabel = tk.Label(master=window, text="Player Not In Database")
            playerErrorLabel.grid(row=4,column=2)

    searchBtn = tk.Button(master=window,text="search", command=mytest)
    searchBtn.grid(column=4,row=2)


def deletePlayerPage():
    clearFrame()
    deletePlayerSearchBox = tk.Entry(master=window, text='Test')
    deletePlayerSearchBox.grid(column=2,row=2)

    def deletePlayer():
        name = deletePlayerSearchBox.get()
        database.deletePlayerFromTableByNameFunc(connection,name)
        messagebox.showinfo("Success", "Player Deleted")

    deletePlayerSubmitButton = tk.Button(master=window, text='Test',command=deletePlayer)
    deletePlayerSubmitButton.grid(column=2,row=4)   

def addBaseSet():
    database.addDataSet(connection)
    messagebox.showinfo("Success", "Base Data Set Added")

def imFeelingLuckyFunc():
    tempNum = random.randint(0,3)
    print(tempNum)
    if tempNum == 0:
        addPlayerPage()
    elif tempNum == 1:
        addSearchPage()
    elif tempNum == 2:
        deletePlayerPage()
    elif tempNum == 3:
        addViewPage()


titleLabel = tk.Label(master=window, text='Favourite Hockey Players')
titleLabel.grid(column=2, row=0, padx=75)

addFrame = tk.Button(master=window, text='Add Player',command=addPlayerPage)
addFrame.grid(column=2,row=2, pady=10, padx=10)

searchFrame = tk.Button(master=window, text='Search For Player',command=addSearchPage)
searchFrame.grid(column=2,row=4, pady=10, padx=10)

deletePlayerFrame = tk.Button(master=window, text='Delete Player',command=deletePlayerPage)
deletePlayerFrame.grid(column=2,row=6, pady=10, padx=10)

viewPlayerFrame = tk.Button(master=window, text='View Players',command=addViewPage)
viewPlayerFrame.grid(column=2,row=8, pady=10, padx=10)

addBaseSetFrame = tk.Button(master=window, text='Import Base Data Set',command=addBaseSet)
addBaseSetFrame.grid(column=2,row=10, pady=10, padx=10)

imFeelingLuckyButton = tk.Button(master=window, text="I'm Feeling Lucky", command=imFeelingLuckyFunc)
imFeelingLuckyButton.grid(column=2,row=12,pady=10, padx=10)




def endAll():
    connection = database.connect()
    database.deleteFunc(connection)


def addPage():
    connection = database.connect()




menu()
notebook.pack()
window.mainloop()

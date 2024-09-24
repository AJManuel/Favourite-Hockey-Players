import database
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random


#Base Tkinter Setup

window = tk.Tk()
window.title('Favourite Hockey Players')
window.geometry("525x500")

menuPrompt = """
"""

fontColour = '#FF0000'



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
        pass

#Function for the players

def addPlayerPage():
    clearFrame()
    entryNameText = tk.StringVar()
    addPlayerNameEntryBox = tk.Entry(master=window, textvariable=entryNameText, width=25)
    entryNameText.set("Enter A Players Name")
    addPlayerNameEntryBox.grid(column=2,row=2, pady=10,padx=75)

    entryTeamText = tk.StringVar()
    addPlayerTeamEntryBox = tk.Entry(master=window, textvariable=entryTeamText, width=25)
    entryTeamText.set("Enter The Players Team")
    addPlayerTeamEntryBox.grid(column=2,row=4, pady=10,padx=75)

    entryNumberText = tk.StringVar()
    addPlayerNumberEntryBox = tk.Entry(master=window, textvariable=entryNumberText, width=25)
    entryNumberText.set("Enter The Players Number")
    addPlayerNumberEntryBox.grid(column=2,row=6, pady=10,padx=75)


    def enterIntoData():
        name = addPlayerNameEntryBox.get()
        team = addPlayerTeamEntryBox.get()
        number = addPlayerNumberEntryBox.get()
        if name or team or number == "":
            print('error')
            pass
        database.addPlayers(connection,name,team,number)
        messagebox.showinfo("Success", "Player Added")

    addPlayerInsertButton = tk.Button(master=window, text='Add To Database', command=enterIntoData, fg=fontColour)
    addPlayerInsertButton.grid(column=2,row=8, pady=10, padx=75)

    backButton = tk.Button(master=window,text="Back", command=backFunc, fg=fontColour)
    backButton.grid(column=2,row=10)

sortOptions = ['Name', 'Team', 'Number']
playerSortBox = ttk.Combobox(master=window,values=sortOptions)
#function for the view all players page

def addViewPage():
    clearFrame()
    global playerSortBox
    playerNameLabel = tk.Label(master=window, text="Player")
    playerNameLabel.grid(column=2, row=2)

    playerTeamLabel = tk.Label(master=window, text="Team")
    playerTeamLabel.grid(column=3, row=2)

    playerNumberLabel = tk.Label(master=window, text="Number")
    playerNumberLabel.grid(column=4, row=2)

    playerSortBox = ttk.Combobox(master=window,values=sortOptions)
    playerSortBox.grid(column=5,row=2)

    def playerAllSort():
        global playerSortBox
        currentOption = playerSortBox.get()
        if currentOption == 'Name':
            clearFrame()
            playerNameLabel = tk.Label(master=window, text="Player")
            playerNameLabel.grid(column=2, row=2)

            playerTeamLabel = tk.Label(master=window, text="Team")
            playerTeamLabel.grid(column=3, row=2)

            playerNumberLabel = tk.Label(master=window, text="Number")
            playerNumberLabel.grid(column=4, row=2)

            playerSortBox = ttk.Combobox(master=window,values=sortOptions)
            playerSortBox.grid(column=5,row=2)

            playerSortConfirm = tk.Button(master=window, text='Sort',fg=fontColour,command=playerAllSort)
            playerSortConfirm.grid(column=5,row=3)

            backButton = tk.Button(master=window,text="Back", command=backFunc, fg=fontColour)
            backButton.grid(column=3,row=totalPlayers+4)
            allPlayers = database.getPlayersSortedName(connection)
            print(allPlayers)
            for i,e in enumerate(allPlayers):
    
                playerNameGrid = tk.Label(master=window, text=e[1])
                playerNameGrid.grid(row=3 + i,column=2)

                playerTeamGrid = tk.Label(master=window, text=e[2])
                playerTeamGrid.grid(row=3 + i,column=3)

                playerNumberGrid = tk.Label(master=window, text=e[3])
                playerNumberGrid.grid(row=3 + i,column=4)
        elif currentOption == 'Team':
            clearFrame()
            playerNameLabel = tk.Label(master=window, text="Player")
            playerNameLabel.grid(column=2, row=2)

            playerTeamLabel = tk.Label(master=window, text="Team")
            playerTeamLabel.grid(column=3, row=2)

            playerNumberLabel = tk.Label(master=window, text="Number")
            playerNumberLabel.grid(column=4, row=2)

            playerSortBox = ttk.Combobox(master=window,values=sortOptions)
            playerSortBox.grid(column=5,row=2)

            playerSortConfirm = tk.Button(master=window, text='Sort',fg=fontColour,command=playerAllSort)
            playerSortConfirm.grid(column=5,row=3)

            backButton = tk.Button(master=window,text="Back", command=backFunc, fg=fontColour)
            backButton.grid(column=3,row=totalPlayers+4)
            allPlayers = database.getPlayersSortedTeam(connection)
            print(allPlayers)
            for i,e in enumerate(allPlayers):
    
                playerNameGrid = tk.Label(master=window, text=e[1])
                playerNameGrid.grid(row=3 + i,column=2)

                playerTeamGrid = tk.Label(master=window, text=e[2])
                playerTeamGrid.grid(row=3 + i,column=3)

                playerNumberGrid = tk.Label(master=window, text=e[3])
                playerNumberGrid.grid(row=3 + i,column=4)
        elif currentOption == 'Number':
            clearFrame()
            playerNameLabel = tk.Label(master=window, text="Player")
            playerNameLabel.grid(column=2, row=2)

            playerTeamLabel = tk.Label(master=window, text="Team")
            playerTeamLabel.grid(column=3, row=2)

            playerNumberLabel = tk.Label(master=window, text="Number")
            playerNumberLabel.grid(column=4, row=2)

            playerSortBox = ttk.Combobox(master=window,values=sortOptions)
            playerSortBox.grid(column=5,row=2)

            playerSortConfirm = tk.Button(master=window, text='Sort',fg=fontColour,command=playerAllSort)
            playerSortConfirm.grid(column=5,row=3)

            backButton = tk.Button(master=window,text="Back", command=backFunc, fg=fontColour)
            backButton.grid(column=3,row=totalPlayers+4)
            allPlayers = database.getPlayersSortedNum(connection)
            print(allPlayers)
            for i,e in enumerate(allPlayers):
    
                playerNameGrid = tk.Label(master=window, text=e[1])
                playerNameGrid.grid(row=3 + i,column=2)

                playerTeamGrid = tk.Label(master=window, text=e[2])
                playerTeamGrid.grid(row=3 + i,column=3)

                playerNumberGrid = tk.Label(master=window, text=e[3])
                playerNumberGrid.grid(row=3 + i,column=4)
        else:
            print('error')
            messagebox.showerror('Error', 'Please select a proper sorting method')

    playerSortConfirm = tk.Button(master=window, text='Sort',fg=fontColour,command=playerAllSort)
    playerSortConfirm.grid(column=5,row=3)

    players = database.getThePlayers(connection)
    for i,e in enumerate(players):
    
        playerNameGrid = tk.Label(master=window, text=e[1])
        playerNameGrid.grid(row=3 + i,column=2)

        playerTeamGrid = tk.Label(master=window, text=e[2])
        playerTeamGrid.grid(row=3 + i,column=3)

        playerNumberGrid = tk.Label(master=window, text=e[3])
        playerNumberGrid.grid(row=3 + i,column=4)
    totalPlayers = len(players)
    backButton = tk.Button(master=window,text="Back", command=backFunc, fg=fontColour)
    backButton.grid(column=3,row=totalPlayers+4)
    pass

#function for the search all players page

def addSearchPage():
    clearFrame()
    playerSearchLabel = tk.Label(master=window, text="Enter The Players Name")
    playerSearchLabel.grid(column=2,row=1)

    addPlayerSearchBox = tk.Entry(master=window, text='Search')
    addPlayerSearchBox.grid(column=2,row=2)

    def searchName():
        name = addPlayerSearchBox.get()
        players = database.getPlayersByName(connection, name)

        playerNameLabel = tk.Label(master=window, text="Player: ")
        playerNameLabel.grid(row=4,column=1)

        playerNameAns = tk.Label(master=window, text=players[1])
        playerNameAns.grid(row=4,column=2)

        playerTeamLabel = tk.Label(master=window, text="Team: ")
        playerTeamLabel.grid(row=5,column=1)

        playerTeamAns = tk.Label(master=window, text=players[2])
        playerTeamAns.grid(row=5,column=2)

        playerNumberLabel = tk.Label(master=window, text="Number: ")
        playerNumberLabel.grid(row=6,column=1)

        playerNumberAns = tk.Label(master=window, text=players[3])
        playerNumberAns.grid(row=6,column=2)

    def mytest():
        try: 
            searchName()
        except TypeError:
            print('Error')
            playerErrorLabel = tk.Label(master=window, text="Player Not In Database")
            playerErrorLabel.grid(row=4,column=2)

    searchBtn = tk.Button(master=window,text="Search", command=mytest, fg=fontColour)
    searchBtn.grid(column=2,row=7)

    backButton = tk.Button(master=window,text="Back", command=backFunc, fg=fontColour)
    backButton.grid(column=2,row=9)

#function for the delete player page

def deletePlayerPage():
    clearFrame()
    deletePlayerLabel = tk.Label(master=window, text="Enter The Players Full Name To Delete")
    deletePlayerLabel.grid(column=2,row=1,padx=75)

    deletePlayerSearchBox = tk.Entry(master=window, text='Test')
    deletePlayerSearchBox.grid(column=2,row=2,padx=75)

    def deletePlayer():
        name = deletePlayerSearchBox.get()
        database.deletePlayerFromTableByNameFunc(connection,name)
        messagebox.showinfo("Success", "Player Deleted")

    deletePlayerSubmitButton = tk.Button(master=window, text='DELETE',command=deletePlayer, fg="#FF0000")
    deletePlayerSubmitButton.grid(column=2,row=4,padx=75)   
    backButton = tk.Button(master=window,text="Back", command=backFunc, fg=fontColour)
    backButton.grid(column=2,row=6,padx=75)

#function to add a base set of players to the database

def addBaseSet():
    database.addDataSet(connection)
    messagebox.showinfo("Success", "Base Data Set Added")

#function for the im feeling lucky button

def imFeelingLuckyFunc():
    tempNum = random.randint(0,3)
    if tempNum == 0:
        addPlayerPage()
    elif tempNum == 1:
        addSearchPage()
    elif tempNum == 2:
        deletePlayerPage()
    elif tempNum == 3:
        addViewPage()

fontChoices = {
    "Red": "#FF0000",
    "Green": "#00FF00",
    "Blue": "#0000FF",
    "Steel Blue": "#231A24",
    "Pale Green": "#89AC76",
    "Slate Grey": "#434750",
    "Salmon": "#D95030"
}
fontChoicesKeys = []
fontChoicesValues = []
for each in fontChoices:
    fontChoicesKeys.append(each)
for each in fontChoices:
    fontChoicesValues.append(fontChoices[each])

def updateColour():
    currentColour = fontColourButton.get()
    for each in fontChoices:
        if currentColour == each:
            global fontColour
            fontColour = fontChoices[each]
        elif currentColour != each:
            print('Not This Colour')
    backFunc()



def backFunc():
    clearFrame()
    titleLabel = tk.Label(master=window, text='Favourite Hockey Players', font=('arial', 15))
    titleLabel.grid(column=2, row=0, padx=75)

    addFrame = tk.Button(master=window, text='Add Player',command=addPlayerPage, fg=fontColour)
    addFrame.grid(column=2,row=2, pady=10, padx=10)

    searchFrame = tk.Button(master=window, text='Search For Player',command=addSearchPage, fg=fontColour)
    searchFrame.grid(column=2,row=4, pady=10, padx=10)

    deletePlayerFrame = tk.Button(master=window, text='Delete Player',command=deletePlayerPage, fg=fontColour)
    deletePlayerFrame.grid(column=2,row=6, pady=10, padx=10)

    viewPlayerFrame = tk.Button(master=window, text='View Players',command=addViewPage, fg=fontColour)
    viewPlayerFrame.grid(column=2,row=8, pady=10, padx=10)

    addBaseSetFrame = tk.Button(master=window, text='Import Base Data Set',command=addBaseSet, fg=fontColour)
    addBaseSetFrame.grid(column=2,row=10, pady=10, padx=10)

    imFeelingLuckyButton = tk.Button(master=window, text="I'm Feeling Lucky", command=imFeelingLuckyFunc, fg=fontColour)
    imFeelingLuckyButton.grid(column=2,row=12,pady=10, padx=10)

    fontColourButton2 = ttk.Combobox(master=window,values=fontChoicesKeys)
    fontColourButton2.grid(column=2,row=14,padx=10,pady=10) 

    def repeatUpdateColour():
        currentColour = fontColourButton2.get()
        for each in fontChoices:
            if currentColour == each:
                global fontColour
                fontColour = fontChoices[each]
            elif currentColour != each:
                print('Not this colour')
        backFunc()

    updateColourButton = tk.Button(master=window,text="Update Font",command = repeatUpdateColour, fg=fontColour)
    updateColourButton.grid(column=2,row=16,pady=10,padx=10) 
#tkinter set up for the opening page



titleLabel = tk.Label(master=window, text='Favourite Hockey Players', font=('arial', 15))
titleLabel.grid(column=2, row=0, padx=75)

addFrame = tk.Button(master=window, text='Add Player',command=addPlayerPage, fg=fontColour)
addFrame.grid(column=2,row=2, pady=10, padx=10)

searchFrame = tk.Button(master=window, text='Search For Player',command=addSearchPage, fg=fontColour)
searchFrame.grid(column=2,row=4, pady=10, padx=10)

deletePlayerFrame = tk.Button(master=window, text='Delete Player',command=deletePlayerPage, fg=fontColour)
deletePlayerFrame.grid(column=2,row=6, pady=10, padx=10)

viewPlayerFrame = tk.Button(master=window, text='View Players',command=addViewPage, fg=fontColour)
viewPlayerFrame.grid(column=2,row=8, pady=10, padx=10)

addBaseSetFrame = tk.Button(master=window, text='Import Base Data Set',command=addBaseSet, fg=fontColour)
addBaseSetFrame.grid(column=2,row=10, pady=10, padx=10)

imFeelingLuckyButton = tk.Button(master=window, text="I'm Feeling Lucky", command=imFeelingLuckyFunc, fg=fontColour)
imFeelingLuckyButton.grid(column=2,row=12,pady=10, padx=10)


fontColourButton = ttk.Combobox(master=window,values=fontChoicesKeys)
fontColourButton.grid(column=2,row=14,padx=10,pady=10)


updateColourButton = tk.Button(master=window,text="Update Font",command=updateColour, fg=fontColour)
updateColourButton.grid(column=2,row=16,pady=10,padx=10)

#final set up parts

menu()
window.mainloop()

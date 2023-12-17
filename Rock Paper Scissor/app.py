# importing the necessary libraries:
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import random

# arrays to store the win history:
playerScore = []
computerScore = []

# rock button click command function:
def isRock():
    game("Rock", playerScore, computerScore)

# paper button click command function:
def isPaper():
    game("Paper", playerScore, computerScore)

# scissor button click command function:
def isScissor():
    game("Scissor", playerScore, computerScore)

# function to get computers move randomly from the list of moves:
def computerMove():
    moves = ["Rock", "Paper", "Scissor"]
    return random.choice(moves)

# function that determines the winner of the game:
def game(userMove, playerScore, computerScore):
    computersMove = computerMove()
    # user winning cases:
    if(userMove == "Rock"):
        if(computersMove == "Scissor"):
            playerScore.append(1)
            showWinner("player", userMove, computersMove, playerScore, computerScore)
    if(userMove == "Paper"):
        if(computersMove == "Rock"):
            playerScore.append(1)
            showWinner("player", userMove, computersMove, playerScore, computerScore)
    if(userMove == "Scissor"):
        if(computersMove == "Paper"):
            playerScore.append(1)
            showWinner("player", userMove, computersMove, playerScore, computerScore)
    
    # computer winning cases:
    if(computersMove == "Rock"):
        if(userMove == "Scissor"):
            computerScore.append(1)
            showWinner("computer", userMove, computersMove, playerScore, computerScore)
    if(computersMove == "Paper"):
        if(userMove == "Rock"):
            computerScore.append(1)
            showWinner("computer", userMove, computersMove, playerScore, computerScore)
    if(computersMove == "Scissor"):
        if(userMove == "Paper"):
            computerScore.append(1)
            showWinner("computer", userMove, computersMove, playerScore, computerScore)

# function to show the game result in a second tkinter window:
def showWinner(winner, playerMove, computerMove, playerScore, computerScore):
    usersMove = playerMove
    computersMove = computerMove
    
    # tkinter window declarations and setting up the window
    secondaryWindow = tk.Tk()
    secondaryWindow.title("Winner")
    secondaryWindow.resizable(0,0)
    secondaryWindow.geometry("600x300+300+160")
    secondaryWindow.configure(background="#00B4D8")
    
    # defining the description text of the game based on the winner:
    if winner == "player":
        winnerText = "Player Wins"
        descText = (usersMove + " beats " + computersMove)
    else:
        winnerText = "Computer Wins"
        descText = (computersMove + " beats " + usersMove)

    frame2 = Frame(secondaryWindow, background="#00B4D8")
    frame2.pack()
    frame3 = Frame(secondaryWindow, background="#00B4D8")
    frame3.pack()
    frame4 = Frame(secondaryWindow, background="#00B4D8")
    frame4.pack()
    
    # to show players points:
    label2_1 = Label(
        frame2,
        text = "Player: " + str(len(playerScore)),
        font=("Normal", 24),
        foreground="#9e2a2b",
        background="#00B4D8"
    )
    
    # to show computers points:
    label2_2 = Label(
        frame2,
        text = "Computer: " + str(len(computerScore)),
        font = ("Normal", 24),
        foreground="#9e2a2b",
        background="#00B4D8"
    )
    
    # to display the winner of the game:
    label3 = Label(
        frame3,
        text = winnerText,
        font = ("Courier New", 30),
        foreground="#ffc300",
        background = "#00B4D8",
        width=20,
        height=2,
        borderwidth=2,
        relief="ridge"
    )
    
    # to display the description of the moves played in the game:
    label4 = Label(
        frame4,
        text = descText,
        font = ("Normal", 24, "underline"),
        background = "#00B4D8"
    )
    
    # button to continue the game:
    replayButton = Button(
        secondaryWindow,
        text="Replay Game",
        background = "#06D6A0",
        activebackground = "#f28482",
        command=secondaryWindow.withdraw
    )
    
    label2_1.grid(row=0, column=0, padx=20, pady=10)
    label2_2.grid(row=0, column=1, padx=20, pady=10)
    label3.pack(pady=10)
    label4.pack(pady=10)
    replayButton.pack()
    secondaryWindow.mainloop()

# mainwindow Tkiniter declarations:
mainWindow = tk.Tk()
mainWindow.resizable(0,0)
mainWindow.geometry("800x450+200+50")
mainWindow.configure(background = "#118AB2")
mainWindow.title("Rock Paper Scissor Game")



headerFrame = tk.Frame(mainWindow, background="#EF476F")
headerFrame.pack(fill="both")
frame1 = tk.Frame(mainWindow, background="#118AB2")
frame1.pack()
frame2 = tk.Frame(mainWindow, background="#118AB2")
frame2.pack(pady=5)
buttonFrame = tk.Frame(mainWindow, background="#118AB2")
buttonFrame.pack()
exitFrame = tk.Frame(mainWindow, background="#118AB2")
exitFrame.pack()

# fetching the images from the media folder:
rock = Image.open("./media/rock.png")
rockResize = rock.resize((200,200))
rockImage = ImageTk.PhotoImage(rockResize)
paper = Image.open("./media/paper-plane.png")
paperResize = paper.resize((200,200))
paperImage = ImageTk.PhotoImage(paperResize)
scissor = Image.open("./media/scissor.png")
scissorResize = scissor.resize((200,200))
scissorImage = ImageTk.PhotoImage(scissorResize)

# the header label
headerLabel = Label(
    headerFrame,
    text = "Rock Paper Scissor",
    font = ("Georgia Bold", "36"),
    background="#EF476F",
)

# instruction label:
label1 = Label(
    frame1,
    text = ("Choose Your Move"),
    font=("Courier New", "18", "underline"),
    background= "#118AB2"
)

# rock button:
rockButton = Button(
    buttonFrame,
    text="Rock",
    image=rockImage,
    bg="#118AB2",
    command=isRock
)

# paper button:
paperButton = Button(
    buttonFrame,
    text="Paper",
    image=paperImage,
    bg="#118AB2",
    command=isPaper
)

# scissor button:
scissorButton = Button(
    buttonFrame,
    text="Scissor",
    image=scissorImage,
    bg = "#118AB2",
    command=isScissor
)

# exit button:
exitButton = Button(
    exitFrame,
    text="Force Exit",
    background = "#06D6A0",
    activebackground = "#f28482",
    command=mainWindow.quit
)

# rock label:
rockLabel = Label(
    frame2,
    text="Rock",
    font=("Impact light", "20"),
    width=10,
    background="#118AB2"
)

# paper label
paperLabel = Label(
    frame2,
    text="Paper",
    font=("Impact light", "20"),
    width=10,
    background="#118AB2"
)

# scissor label:
scissorLabel = Label(
    frame2,
    text="Scissor",
    font=("Impact light", "20"),
    width=10,
    background="#118AB2"
)


rockLabel.configure(padx=25)
paperLabel.configure(padx=20)
scissorLabel.configure(padx=20)

headerLabel.pack()
label1.pack(pady=10)
exitButton.pack(pady=20)
rockLabel.grid(row=0, column=0, padx=20)
paperLabel.grid(row=0, column=1, padx=20)
scissorLabel.grid(row=0, column=2, padx=20)
rockButton.grid(row=1, column=0, padx=20)
paperButton.grid(row=1, column=1, padx=20)
scissorButton.grid(row=1, column=2, padx=20)

# initiating the mainWindow:
mainWindow.mainloop()
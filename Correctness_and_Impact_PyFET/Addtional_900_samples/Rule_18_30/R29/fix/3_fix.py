
unoDeck = buildDeck()
unoDeck = shuffleDeck(unoDeck)
unoDeck = shuffleDeck(unoDeck)
discards = []

players_name = []
players = []
colours = ["Red", "Green", "Yellow", "Blue"]
numPlayers = int(input("How many players?"))
while numPlayers < 2 or numPlayers > 4:
    numPlayers = int(
        input("Invalid. Please enter a number between 2-4.\nHow many players?"))
for player in range(numPlayers):
    players_name.append(input("Enter player {} name: ".format(player+1)))
    players.append(drawCards(5))


playerTurn = 0
playDirection = 1
playing = True
discards.append(unoDeck.pop(0))
splitCard = discards[0].split(" ", 1)
currentColour = splitCard[0]
if currentColour != "Wild":
    cardVal = splitCard[1]
else:
    cardVal = "Any"

while playing:
    showHand(playerTurn, players[playerTurn])
    print("Card on top of discard pile: {}".format(discards[-1]))
    if canPlay(currentColour, cardVal, players[playerTurn]):
        cardChosen = int(input("Which card do you want to play?"))
        while not canPlay(currentColour, cardVal, [players[playerTurn][cardChosen-1]]):
            cardChosen = int(
                input("Not a valid card. Which card do you want to play?"))
        print("You played {}".format(players[playerTurn][cardChosen-1]))
        discards.append(players[playerTurn].pop(cardChosen-1))

        # cheak if player won
        if len(players[playerTurn]) == 0:
            playing = False
            # winner = "Player {}".format(playerTurn+1)
            winner = players_name[playerTurn]
        else:
            # cheak for special cards
            splitCard = discards[-1].split(" ", 1)
            currentColour = splitCard[0]
            if len(splitCard) == 1:
                cardVal = "Any"
            else:
                cardVal = splitCard[1]
            if currentColour == "Wild":
                for x in range(len(colours)):
                    print("{}) {}".format(x+1, colours[x]))
                newColour = int(
                    input("What colour would you like to choose? "))
                while newColour < 1 or newColour > 4:
                    newColour = int(
                        input("Invalid option. What colour would you like to choose"))
                currentColour = colours[newColour-1]
            if cardVal == "Reverse":
                playDirection = playDirection * -1
            elif cardVal == "Skip":
                playerTurn += playDirection
                if playerTurn >= numPlayers:
                    playerTurn = 0
                elif playerTurn < 0:
                    playerTurn = numPlayers-1
            elif cardVal == "Draw Two":
                playerDraw = playerTurn+playDirection
                if playerDraw == numPlayers:
                    playerDraw = 0
                elif playerDraw < 0:
                    playerDraw = numPlayers-1
                players[playerDraw].extend(drawCards(2))
            elif cardVal == "Draw Four":
                playerDraw = playerTurn+playDirection
                if playerDraw == numPlayers:
                    playerDraw = 0
                elif playerDraw < 0:
                    playerDraw = numPlayers-1
                players[playerDraw].extend(drawCards(4))
            print("")
    else:
        print("You can't play. You have to draw a card.")
        players[playerTurn].extend(drawCards(1))

    playerTurn += playDirection
    if playerTurn >= numPlayers:
        playerTurn = 0
    elif playerTurn < 0:
        playerTurn = numPlayers-1

print("Game Over")
print("{} is the Winner!".format(winner))

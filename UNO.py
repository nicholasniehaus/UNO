import random
from datetime import date
import time

start = time.time()
uno_cards_color = ["Red_", "Blue_", "Green_", "Yellow_"]
uno_cards_number = ['1', '2', '3', '4', '5']
turn = 1
topcard = ""
handsize1 = 7
handsize2 = 7

winner = 0


# this function is used to process each turn.
def player_turn(player1_hand, topcard, turn):

    turn = turn * -1
    uno_card = unocardfunc(uno_cards_color, uno_cards_number)
    #this part makes sure the card they play is valid.
    invalid = True

    while invalid:
        player1_play = input("Play a card or type 'Draw':")
        player1_play = player1_play.strip().title()
        player1_play_lower = player1_play.strip().lower()
        player1_hand_lower = []

        for card in player1_hand:
            player1_hand_lower.append(card.lower())

        for card in player1_hand_lower:
            if (card == player1_play_lower):
                invalid = False
                break
        if player1_play_lower == 'draw':
            invalid = False
        if invalid:
            print(
                "Invalid card, enter a card in your hand or enter in 'Draw'.")

    if player1_play == "Draw":
        player1_hand.append(uno_card)
        return topcard, player1_hand, turn

    testcard = player1_play.split("_")
    testplay = topcard.split("_")

    if len(testplay) < 2:
        topcard = player1_play
        testplay = topcard.split("_")
    #this part makes sure that either the color, or the number of the card matches.
    if testcard[0].lower() == testplay[0].lower(
    ) or testcard[1] == testplay[1]:
        topcard = player1_play
        player1_hand.remove(player1_play)
    else:
        player1_hand.append(uno_card)
        return topcard, player1_hand, turn

    return topcard, player1_hand, turn


#this function counts each player's hand.
def card_count(player1_hand):
    handsize1 = len(player1_hand)
    return handsize1


#this function prints out the victory certificate!
def wincertificate(winner, gamelength):

    today = date.today()
    import os

    filename = "UNOwinner.txt"
    print(filename)

    finalfilename = os.path.join(os.path.expanduser('~'), 'Downloads',
                                 filename)

    printout = open(finalfilename, "w+")

    if winner == 1:
        printout.write("Player 1 Won Uno! on {}".format(today))
    if winner == 2:
        printout.write("Player 2 Won Uno! on {}".format(today))
    printout.write("\n\nThe game took {: .2f} seconds".format(gamelength))
    printout.close()

    return


#this function sets up the inital conditons for the game.
def gamesetup(uno_cards_color, uno_cards_number, player1_hand, player2_hand,
              unocardfunc):

    while len(player1_hand) < 7:
        uno_card = random.choice(uno_cards_color) + random.choice(
            uno_cards_number)
        player1_hand.append(uno_card)

    while len(player2_hand) < 7:
        uno_card = random.choice(uno_cards_color) + random.choice(
            uno_cards_number)
        player2_hand.append(uno_card)
    handsize1 = card_count(player1_hand)
    handsize2 = card_count(player2_hand)

    return player1_hand, player2_hand


#this function creates the cards from teh color and number lists.
def unocardfunc(uno_cards_color, uno_cards_number):
    uno_card = random.choice(uno_cards_color) + random.choice(uno_cards_number)
    #print(uno_card)
    return uno_card


if __name__ == "__main__":

    uno_cards_color = ["Red_", "Blue_", "Green_", "Yellow_"]
    uno_cards_number = ['1', '2', '3', '4', '5']
    turn = 1
    topcard = ""
    winner = 0

    player1_hand = []
    player2_hand = []

    gamesetup(uno_cards_color, uno_cards_number, player1_hand, player2_hand,
              unocardfunc)

    print("Player 1's turn now:")
    #this while loop makes sure that noone has won yet.
    while handsize1 > 0 and handsize2 > 0:
        if turn == 1:
            print("This is Player 1's hand: {}".format(player1_hand))
            print("This is the top card: {}".format(topcard))
            topcard, player1_hand, turn = player_turn(player1_hand, topcard,
                                                      turn)
            handsize1 = card_count(player1_hand)
            if handsize1 == 0:
                winner = 1
                print("Player 1 wins!")
                end = time.time()
                gamelength = end - start
                wincertificate(winner, gamelength)
                quit()
            if len(player1_hand) == 1:
                print("Player 1 UNO!")

            else:
                print("\n\n\n\nPlayer 2's turn")
        if turn == -1:
            print("\nThis is Player 2's hand: {}".format(player2_hand))
            print("This is the top card: {}".format(topcard))
            topcard, player2_hand, turn = player_turn(player2_hand, topcard,
                                                      turn)
            handsize2 = card_count(player2_hand)
            if handsize2 == 0:
                winner = 2
                print("Player 2 wins!")
                end = time.time()
                gamelength = end - start
                wincertificate(winner, gamelength)
                quit()
            if len(player1_hand) == 1:
                print("Player 2 UNO!")

            else:
                print("\n\n\n\nPlayer 1's turn")

def main():
    difficulty=input("Difficult or casual?")
    if not(difficulty=='Difficult' or difficulty=='Casual'):
        print('Enter a valid difficulty level')
        return

    players=input("Multiplayer or Single-player? ")
    if not(players=='Multiplayer' or difficulty=='Single-player'):
        print('Enter a valid player number')
        return

    if difficulty == "Difficult" and players == "Multiplayer":
        recommend("Poker")
    elif difficulty == "Difficult" and players == "Single-player":
        recommend("Klondike")
    elif difficulty=='Casual' and players == "Multiplayer":
        recommend("Hearts")
    else:
        recommend('Clock')



def recommend(game):
    print("we recommend",game)


main()
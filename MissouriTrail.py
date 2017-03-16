#part of the Missouri Trail game
#by Erik B & David I (davidizzy)
#this game is dependent on the custom modules: characters, movements, and outcomes
#Welcome to the Missour Trail game

import characters, string

def playGame(name, charType, gameLength="200"):
    if charType == "1":
        player = characters.doctor(name)
    else:
        player = characters.hunter(name)
    dist = int(gameLength)
    gamePlay = True
    turn = 1
    while gamePlay == True:
        print("\n" + player.getName() + " is at mile " + str(player.distanceTraveled) + " of " + str(dist) +"mi")
        if turn != 1 and player.isAlive == True and player.distanceTraveled < dist:
            continuePlay = input("\n Press Enter/Return key to continue play. ") # CHANGED so the message is clearer
        elif not player.isAlive:
            break
        if player.getDistance() >= dist:
            print("\nCongrats!\n" + player.getName() +" reached the Arch! Enjoy some toasted raviolis!\n")
            gamePlay = False
        elif player.getDistance() < dist:
            print("\n" + player.moveForward() +"\n")
        turn += 1
    return "\nGame over\n"


def main():
    print("Welcome to Missouri Trail Game! Let's get started...")
    name = input("Type your name: ")
    charType = input("Play as Doctor [1] or as Hunter [2]: ")
    while charType != "1" and charType != "2":
        charType = input("Type the 1 to play as a doctor or type 2 to play as a hunter: ")
    gameLength = input("How many miles do you want to travel? (50-1000):")
    while gameLength.isnumeric() == False or int(gameLength) > 1000 or int(gameLength) < 50:
        gameLength = input("How many miles do you want to travel? (50-1000):")
    print(playGame(name, charType, gameLength))

if __name__ == '__main__':
    main()

# Jeff Haak
# A CLI implementation of the Morse Code game
from morseGame import MorseGame


class MorseCLI:

    def __init__(self, playerName):
        self._morseGame = MorseGame(playerName)

    def play(self):
        print "Here are the games I know.  Pick one by entering the number next to the game you want to play!  " \
              "If you are done, just type the letter N or -."

        games = self._morseGame.getGames()
        for i in range(len(games)):
            print str(i) + ". " + games[i]

        choice = raw_input()
        while True:
            if choice.lower() == 'n' or choice == '-.':
                exit(0)
            elif choice.isdigit() and int(choice) >= 0 and int(choice) < len(games):
                choice = int(choice)
                break
            else:
                choice = raw_input("I need an integer that is in the list.  I can be very persistent.\n")



def main():
    name = raw_input("Hi! My name is Sam.  What is your name?\n")

    morseCli = MorseCLI(name)

    play = raw_input("Let's play some games! (y/n): ").lower()

    if play == 'y':
        morseCli.play()
    else:
        print "Aww man, I was so excited.  Come back soon!"
        exit(0)


if __name__ == "__main__":
    main()
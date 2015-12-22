# Jeff Haak
# A CLI implementation of the Morse Code game
import os
from morseGame import MorseGame


class MorseCLI:

    def __init__(self, playerName):
        self._morseGame = MorseGame(playerName)

    def printGames(self, games):
        print "Here are the games I know.  Pick one by entering the number next to the game you want to play!  " \
              "If you are done, just type the letter N or -."

        for i in range(len(games)):
            print str(i) + ". " + games[i]

    def play(self):
        games = self._morseGame.getGames()
        self.printGames(games)

        choice = raw_input()
        while True:
            if self.exitCondition(choice):
                exit(0)
            elif choice.isdigit() and int(choice) >= 0 and int(choice) < len(games):
                choice = int(choice)
                self.playGame(games[choice])
            else:
                choice = raw_input("I need an integer that is in the list.  I can be very persistent.\n")

            self.clearScreen()
            print "Want to play again?"
            self.printGames(games)
            choice = raw_input()

    def exitCondition(self, choice):
        if choice.lower() == 'n' or choice == '-.':
            return True
        return False

    def playGame(self, gameChoice):
        self.clearScreen()

        if gameChoice == "Encoder":
            self.encoder()
        elif gameChoice == "Decoder":
            self.decoder()
        elif gameChoice == "Learn the Letter":
            self.learnLetter()
        elif gameChoice == "Test Letters":
            self.testLetter()
        elif gameChoice == "Test Morse":
            self.testMorse()
        elif gameChoice == "Test Knowledge":
            self.testKnowledge()

    def encoder(self):
        self.clearScreen()
        aString = raw_input("I am really good at Morse Code!  What would you like me to translate?\n")
        mString = self._morseGame.encode(aString)
        print "Hmm, let me think about that a second... hmm... Carry the 1... annnnddddddd, here you go"
        print mString
        print "\n"

    def decoder(self):
        self.clearScreen()
        mString = raw_input("I am really good at Morse Code!  What would you like me to translate?\n")
        aString = self._morseGame.decode(mString)
        print "Oh, that is a good one!  Here you go:"
        print aString
        print "\n"

    def learnLetter(self):
        self.clearScreen()
        print "When you are done, type N or -."

        while True:
            print "Do you know this one?"

            letter = self._morseGame.getRandomLetter()

            print letter[0] + " = " + letter[1]

            choice = raw_input()
            if self.exitCondition(choice):
                break

            self.clearScreen()

    def testLetter(self):
        print "I'll give you the letter, you give me the morse code!  You get 100pts if you get it on the first try" \
              "Then 50 for the second, 25 for the 3rd, and after that you lose 50 pts!  Good luck!  When you are done, type Done"

        while True:
            print "Ha!  Here is a hard one!"
            entry = self._morseGame.getRandomLetter()

            count = 0
            gotIt = False
            quitGame = False
            while count < 3:
                print "Score: " + str(self._morseGame.getScore())
                print entry[0]
                response = raw_input()

                if response.strip().lower() == "done":
                    quitGame = True
                    break
                elif response.strip() == entry[1] and count == 0:
                    print "Nice job!  First try!"
                    self._morseGame.increaseScore(100)
                    gotIt = True
                    self.clearScreen()
                    break
                elif response.strip() == entry[1]:
                    print "There we go!"

                    if count == 1:
                        self._morseGame.increaseScore(50)
                    elif count == 2:
                        self._morseGame.increaseScore(25)

                    gotIt = True
                    self.clearScreen()
                    break
                else:
                    count += 1
                    if count < 3:
                        print "Try Again"

            if quitGame:
                break

            if not gotIt:
                print "The answer was: " + entry[1]
                print "You'll get it next time!"
                self._morseGame.decreaseScore(50)


    def testMorse(self):
        print "I'll give you the morse code, you give me the letter!  You get 100pts if you get it on the first try" \
              "Then 50 for the second, 25 for the 3rd, and after that you lose 50 pts!  Good luck!  When you are done, type Done"

        while True:
            print "Ha!  Here is a hard one!"
            entry = self._morseGame.getRandomMorse()

            count = 0
            gotIt = False
            quitGame = False
            while count < 3:
                print "Score: " + str(self._morseGame.getScore())
                print entry[0]
                response = raw_input().upper()
                if response.strip().lower() == "done":
                    quitGame = True
                    break
                elif response.strip() == entry[1] and count == 0:
                    print "Nice job!  First try!"
                    self._morseGame.increaseScore(100)
                    gotIt = True
                    self.clearScreen()
                    break
                elif response.strip() == entry[1]:
                    print "There we go!"

                    if count == 1:
                        self._morseGame.increaseScore(50)
                    elif count == 2:
                        self._morseGame.increaseScore(25)
                    gotIt = True
                    self.clearScreen()
                    break
                else:
                    count += 1
                    if count < 3:
                        print "Try Again"

            if quitGame:
                break

            if not gotIt:
                print "The answer was: " + entry[1]
                print "You'll get it next time!"
                self._morseGame.decreaseScore(50)


    def testKnowledge(self):
        print "I'll give you something, you give me the translation!  You get 100pts if you get it on the first try" \
              "Then 50 for the second, 25 for the 3rd, and after that you lose 50 pts!  Good luck!  When you are done, type Done"

        while True:
            print "Ha!  Here is a hard one!"
            choices = []
            entry = self._morseGame.getRandomPair()

            count = 0
            gotIt = False
            quitGame = False
            while count < 3:
                print "Score: " + str(self._morseGame.getScore())
                print entry[0]
                response = raw_input().upper()
                if response.strip().lower() == "done":
                    quitGame = True
                    self.clearScreen()
                    break
                elif response.strip() == entry[1] and count == 0:
                    print "Nice job!  First try!"
                    self._morseGame.increaseScore(100)
                    gotIt = True
                    self.clearScreen()
                    break
                elif response.strip() == entry[1]:
                    print "There we go!"

                    if count == 1:
                        self._morseGame.increaseScore(50)
                    elif count == 2:
                        self._morseGame.increaseScore(25)
                    gotIt = True
                    self.clearScreen()
                    break
                else:
                    count += 1
                    if count < 3:
                        print "Try Again"

            if quitGame:
                break

            if not gotIt:
                print "The answer was: " + entry[1]
                print "You'll get it next time!"
                self._morseGame.decreaseScore(50)

    def clearScreen(self):
        absolutely_unused_variable = os.system('cls' if os.name=='nt' else 'clear')

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
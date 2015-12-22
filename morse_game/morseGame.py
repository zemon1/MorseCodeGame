# Jeff Haak
# This game is intended to help people learn Morse Code, and test their learning. It also doubles as an encoder/decoder.
from morseCode import MorseCode


class MorseGame:

    def __init__(self, playerName):
        self._morseCoder = MorseCode()
        self._player = playerName

        self._games = ["Encoder",            # Encode normal strings into Morse Code
                      "Decoder",            # Decode Morse Code into normal strings
                      "Learn the Letter",   # Letters are presented as "Letter : 'Morse Code'"
                      "Test Letters",       # Presented with a letter, enter the morse code
                      "Test Morse",         # Presented with morse code, enter the letter
                      "Test Knowledge"]     # Presented with letters or morse code, translate it.

        self._score = 0

    def getPlayer(self):
        return self._player

    def getGames(self):
        return self._games

    def encode(self, alphaString):
        return self._morseCoder.translateString(alphaString)

    def decode(self, morseString):
        return self._morseCoder.translateMorseString(morseString)

    def getRandomLetter(self):
        res = self._morseCoder.getRandomLetter()

        if res[0] == " ":
            res = self._morseCoder.getRandomLetter()

        return res

    def getScore(self):
        return self._score

    def increaseScore(self, amt):
        self._score = self._score + amt

    def decreaseScore(self, amt):
        self._score = self._score - amt
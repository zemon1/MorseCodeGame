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

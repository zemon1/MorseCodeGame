# Jeff Haak
# This contains Morse Code translations for Python
import random


class MorseCode:

    _l2m = {'E':    '.',
            'T':    '-',
            'I':    '..',
            'A':    '.-',
            'N':    '-.',
            'S':    '...',
            'M':    '--',
            'U':    '..-',
            'R':    '.-.',
            'D':    '-..',
            'H':    '....',
            'W':    '.--',
            'K':    '-.-',
            'G':    '--.',
            'O':    '---',
            'V':    '...-',
            'F':    '..-.',
            'L':    '.-..',
            'B':    '-...',
            'P':    '.--.',
            'X':    '-..-',
            'Z':    '--..',
            'C':    '-.-.',
            'J':    '.---',
            'Y':    '-.--',
            'Q':    '--.-',
            '0':    '-----',
            '1':    '.----',
            '2':    '..---',
            '3':    '...--',
            '4':    '....-',
            '5':    '.....',
            '6':    '-....',
            '7':    '--...',
            '8':    '---..',
            '9':    '----.',
            '.':    '.-.-.-',
            ',':    '--..--',
            '?':    '..--..',
            '!':    '..--.',
            ':':    '---...',
            '"':    '.-..-.',
            '\'':   '.----.',
            '=':    '-...-',
            ' ':    '   '}

    _m2l = {'.':        'E',
            '-':        'T',
            '..':       'I',
            '.-':       'A',
            '-.':       'N',
            '...':      'S',
            '--':       'M',
            '..-':      'U',
            '.-.':      'R',
            '-..':      'D',
            '....':     'H',
            '.--':      'W',
            '-.-':      'K',
            '--.':      'G',
            '---':      'O',
            '...-':     'V',
            '..-.':     'F',
            '.-..':     'L',
            '-...':     'B',
            '.--.':     'P',
            '-..-':     'X',
            '--..':     'Z',
            '-.-.':     'C',
            '.---':     'J',
            '-.--':     'Y',
            '--.-':     'Q',
            '-----':    '0',
            '.----':    '1',
            '..---':    '2',
            '...--':    '3',
            '....-':    '4',
            '.....':    '5',
            '-....':    '6',
            '--...':    '7',
            '---..':    '8',
            '----.':    '9',
            '.-.-.-':   '.',
            '--..--':   ',',
            '..--..':   '?',
            '..--.':    '!',
            '---...':   ':',
            '.-..-.':   '"',
            '.----.':   '\'',
            '-...-':    '=',
            '   ':      ' ',
            ' ':        ''}

    def getLetter(self, morse):
        """
        Upon being given a morse string such as '.-' this function should return the letter associated with that morse
            string
        :param morse: A string such as '.-'
        :return: A string containing a single character, such as 'A'
        """
        if morse in self._m2l:
            return self._m2l[morse]
        else:
            return -1

    def getMorse(self, letter):
        """
        Upon being given a letter such as 'A' this function should return the morse code associated with that letter
        :param letter: A string containing a single character, such as 'A'
        :return: A string containing the morse string that corresponding to the letter supplied, such as '.-'
        """
        if letter in self._l2m:
            return self._l2m[letter]
        else:
            return -1

    def getLetters(self, morseList):
        """
        Retrieve a list of letters based on an input list of morse strings. ex: in - ['.-', '-.', '.'],
            out - ['A', 'N' ,'E']
        :param morseList: A list of morse code strings
        :return: A list of characters corresponding to the list that came in.
        """
        letters = []

        for morse in morseList:
            letter = self.getLetter(morse)

            if letter != -1:
                letters.append(letter)
            else:
                letters.append('')

        return letters

    def getMorses(self, letters):
        """
        Retrieve a list of morse code strings based on an input list of letters. ex: in - ['A', 'N' ,'E'],
            out - ['.-', '-.', '.']
        :param letters: A list of characters
        :return: A list of morse strings corresponding to the letters that came in.
        """
        morse = []

        for let in letters:
            response = self.getMorse(let)

            if response != -1:
                morse.append(response)
            else:
                morse.append('')

        return morse

    def translateMorseString(self, morseString):
        """
        Turn a string of morse code into normal letters
        :param morseString: a string of morse code
        :return: An alpha numeric string corresponding to the morse code string passed in
        """
        letters = ''

        cleaned = morseString.replace(self._l2m[' '], "/")
        words = [word.split() for word in cleaned.split("/")]

        for word in words:
            for letter in word:
                letter = self.getLetter(letter)

                if letter != -1:
                    letters += letter

            letters += " "

        return letters.strip()

    def translateString(self, alphaString):
        """
        Turn an alpha numeric string into morse code
        :param alphaString: A string of letters and numbers that you would like translated to morse code
        :return:
        """
        morseString = ""

        for char in alphaString.upper():
            morse = self.getMorse(char)

            if morse != -1:
                if char != " ":
                    morseString += morse + " "
                else:
                    morseString = morseString[:-1] + morse

        return morseString.strip()

    def getRandomMorse(self):
        """
        Return a random Morse character
        :return: A string of morse code
        """
        return random.choice(self._m2l.keys())

    def getRandomLetter(self):
        """
        Return a random character
        :return: A string with a single character in it
        """
        return random.choice(self._l2m.keys())

def main():
    morse = MorseCode()

    hm = ".... . .-.. .-.. ---   .... --- .--   .- .-. .   -.-- --- ..-"
    hs = "Hello how are you $"

    print hs
    print morse.translateMorseString(hm)
    print "------------"
    print hm
    print morse.translateString(hs)

if __name__ == "__main__":
    main()

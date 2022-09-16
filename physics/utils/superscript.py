class SuperScript(object):

    def __init__(self):
        superscript_map = {
            "0": "0", "1": "1", "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9": "9",
            "a": "a", "b": "b", "c": "c", "d": "d", "e": "e", "f": "f", "g": "g", "h": "h", "i": "ɪ", "j": "j",
            "k": "k", "l": "l", "m": "m", "n": "n", "o": "o", "p": "p", "q": "٩", "r": "r", "s": "s", "t": "t",
            "u": "u", "v": "v", "w": "w", "x": "x", "y": "y", "z": "z", "A": "A", "B": "B", "C": "c", "D": "D",
            "E": "E", "F": "f", "G": "G", "H": "H", "I": "I", "J": "J", "K": "K", "L": "L", "M": "M", "N": "N",
            "O": "O", "P": "P", "Q": "Q", "R": "R", "S": "s", "T": "T", "U": "U", "V": "V", "W": "W", "X": "x",
            "Y": "y", "Z": "z", "+": "+", "-": "−", "=": "=", "(": "(", ")": ")"}

        self.trans = str.maketrans(
            ''.join(superscript_map.keys()),
            ''.join(superscript_map.values()))

    def translate_sup(self):
        return self.trans

# if  __name__ == '__main__':
#     sups = SuperScript()
#     print("Hello "+"This is a superscript test.".translate(sups.translate_sup()))

class SubScript(object):

    def __init__(self):
        subscript_map = {
            "0": "0", "1": "1", "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9": "9",
            "a": "a", "b": "♭", "c": "꜀", "d": "ᑯ", "e": "e", "f": "բ", "g": "9", "h": "ₕ", "i": "i", "j": "j",
            "k": "ₖ", "l": "ₗ", "m": "ₘ", "n": "ₙ", "o": "o", "p": "ₚ", "q": "૧", "r": "r", "s": "ₛ", "t": "ₜ",
            "u": "u", "v": "v", "w": "w", "x": "x", "y": "γ", "z": "2", "A": "a", "B": "8", "C": "C", "D": "D",
            "E": "e", "F": "բ", "G": "G", "H": "ₕ", "I": "i", "J": "j", "K": "ₖ", "L": "ₗ", "M": "ₘ", "N": "ₙ",
            "O": "o", "P": "ₚ", "Q": "Q", "R": "r", "S": "ₛ", "T": "ₜ", "U": "u", "V": "v", "W": "w", "X": "x",
            "Y": "γ", "Z": "Z", "+": "+", "-": "−", "=": "=", "(": "(", ")": ")"}
        self.trans = str.maketrans(
            ''.join(subscript_map.keys()),
            ''.join(subscript_map.values()))

    def translate_sub(self):
        return self.trans

# if  __name__ == '__main__':
#     subs = SubScript()
#     print("Hello "+"This is a subscript test.".translate(subs.translate_sub()))

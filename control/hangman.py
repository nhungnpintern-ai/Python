import string

class ComputerGuesser:
    def __init__(self):
        self.guess_order = ['e', 'a'] + [
            c for c in string.ascii_lowercase if c not in ['e', 'a']
        ]
        self.guessed_letters = set()

    def guess(self):
        for letter in self.guess_order:
            if letter not in self.guessed_letters:
                self.guessed_letters.add(letter)
                return letter
        return None


class HangmanGame:
    def __init__(self, guesser):
        self.guesser = guesser
        self.secret_word = "apple"   # ví dụ đơn giản
        self.max_attempts = 6
        self.attempts = 0
        self.correct_letters = set()

    def play(self):
        while self.attempts < self.max_attempts:
            letter = self.guesser.guess()

            if letter in self.secret_word:
                self.correct_letters.add(letter)
                if all(c in self.correct_letters for c in self.secret_word):
                    return True
            else:
                self.attempts += 1

        return False
    
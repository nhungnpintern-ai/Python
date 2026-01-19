from hangman import HangmanGame, ComputerGuesser

def simulate(n_games):
    wins = 0

    for _ in range(n_games):
        game = HangmanGame(ComputerGuesser())
        if game.play():
            wins += 1

    print(f'Win rate: {wins}/{n_games}')

if __name__ == "__main__":
    simulate(10)

import random

class Score:
    """Class to manage overall scores."""
    def __init__(self):
        self.scores = {
            "guess_number": 0,
            "rps": 0,
            "trivia": 0
        }

    def add_score(self, category, points):
        if category in self.scores:
            self.scores[category] += points

    def display_scores(self):
        print("\n--- Overall Score ---")
        for category, score in self.scores.items():
            print(f"{category.replace('_', ' ').title()}: {score}")
        print("---------------------\n")

class GuessNumberGame:
    """Class for the Guess Number Game."""
    def play(self, score):
        print("Welcome to the Guess Number Game!")
        secret = random.randint(1, 20)
        guess_count = 0

        while True:
            try:
                guess = int(input("Guess the number (1-20): "))
                if guess < 1 or guess > 20:
                    print("Please enter a number between 1 and 20.")
                    continue
                guess_count += 1
                if guess == secret:
                    print("Correct! You win!")
                    earned = max(0, 20 - guess_count)
                    print(f"You earned {earned} points.")
                    score.add_score("guess_number", earned)
                    break
                elif guess < secret:
                    print("Too low.")
                else:
                    print("Too high.")
            except ValueError:
                print("Invalid input. Enter a number.")

class RockPaperScissorsGame:
    """Class for Rock Paper Scissors Game."""
    def play(self, score):
        print("Welcome to Rock Paper Scissors!")
        choices = ["rock", "paper", "scissors"]
        rounds = self.get_int("How many rounds do you want to play? ", 1)

        wins = 0
        for _ in range(rounds):
            user = input("Enter rock, paper, or scissors: ").strip().lower()
            if user not in choices:
                print("Invalid choice.")
                continue
            computer = random.choice(choices)
            print(f"Computer chose: {computer}")

            if user == computer:
                print("It's a tie!")
            elif (user == "rock" and computer == "scissors") or \
                 (user == "scissors" and computer == "paper") or \
                 (user == "paper" and computer == "rock"):
                print("You win!")
                wins += 1
            else:
                print("You lose.")

        print(f"Total wins: {wins}")
        score.add_score("rps", wins)

    def get_int(self, prompt, min_value):
        while True:
            try:
                value = int(input(prompt))
                if value < min_value:
                    print(f"Please enter a number >= {min_value}")
                else:
                    return value
            except ValueError:
                print("Invalid input. Please enter a number.")

class TriviaPursuitGame:
    """Class for Trivia Pursuit Game."""
    def __init__(self):
        self.questions = {
            "Science": [
                ("What gas do plants breathe in?", ["A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide"], "C")
            ],
            "History": [
                ("Who discovered America?", ["A. Columbus", "B. Einstein", "C. Newton"], "A")
            ]
        }

    def play(self, score):
        print("Welcome to Trivia Pursuit!")
        total_correct = 0

        for category, qlist in self.questions.items():
            print(f"\nCategory: {category}")
            for question, options, answer in qlist:
                print(question)
                for opt in options:
                    print(opt)
                user_answer = input("Enter your answer (A/B/C): ").strip().upper()
                if user_answer == answer:
                    print("Correct!")
                    total_correct += 1
                else:
                    print(f"Wrong. The correct answer was {answer}.")

        print(f"Total correct answers: {total_correct}")
        score.add_score("trivia", total_correct)

class PokemonBinderManager:
    """Class to manage Pokemon card binder."""
    def __init__(self):
        self.binder = []

    def manage(self):
        print("Welcome to Pokemon Card Binder Manager!")
        while True:
            print("\nMain Menu:")
            print("7. Add Pokemon card")
            print("8. Reset binder")
            print("9. View current placements")
            print("10. Exit")
            choice = self.get_int("Enter your choice: ", 7, 10)

            if choice == 7:
                name = input("Enter Pokemon name: ").strip()
                hp = self.get_int("Enter Pokemon HP: ", 1)
                self.binder.append({"name": name, "hp": hp})
                print(f"{name} with {hp} HP added to binder.")
            elif choice == 8:
                self.binder.clear()
                print("Binder has been reset.")
            elif choice == 9:
                if not self.binder:
                    print("Binder is empty.")
                else:
                    for i, card in enumerate(self.binder, 1):
                        print(f"{i}. {card['name']} - HP: {card['hp']}")
            elif choice == 10:
                break

    def get_int(self, prompt, min_val, max_val=None):
        while True:
            try:
                val = int(input(prompt))
                if val < min_val or (max_val is not None and val > max_val):
                    print("Input out of range.")
                else:
                    return val
            except ValueError:
                print("Invalid input. Please enter a number.")

class GameManager:
    """Main game manager to run the program."""
    def __init__(self):
        self.score = Score()
        self.guess_game = GuessNumberGame()
        self.rps_game = RockPaperScissorsGame()
        self.trivia_game = TriviaPursuitGame()
        self.pokemon_binder = PokemonBinderManager()

    def run(self):
        while True:
            print("\nSelect a function (1-6):")
            print("1. Guess Number game")
            print("2. Rock paper scissors game")
            print("3. Trivia Pursuit Game")
            print("4. Pokemon Card Binder Manager")
            print("5. Check Current Overall score")
            print("6. Exit program")

            choice = self.get_int("Enter your choice: ", 1, 6)

            if choice == 1:
                self.guess_game.play(self.score)
            elif choice == 2:
                self.rps_game.play(self.score)
            elif choice == 3:
                self.trivia_game.play(self.score)
            elif choice == 4:
                self.pokemon_binder.manage()
            elif choice == 5:
                self.score.display_scores()
            elif choice == 6:
                print("Exiting the program. Goodbye!")
                break

    def get_int(self, prompt, min_val, max_val):
        while True:
            try:
                val = int(input(prompt))
                if min_val <= val <= max_val:
                    return val
                else:
                    print(f"Enter a number between {min_val} and {max_val}.")
            except ValueError:
                print("Invalid input. Enter a valid number.")

# Run the program
if __name__ == "__main__":
    game = GameManager()
    game.run()

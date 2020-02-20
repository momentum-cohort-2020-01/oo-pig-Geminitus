from random import randint
dice_sides = 6


class Game:
    def __init__(self, name, winning_score=100):
        self.dice = Dice(dice_sides)
        self.player = Player(name)
        self.dealer = Dealer()

    def __str__(self):
        return f'{self.player}'

    def play(self):
        choice = input("Press 'Enter' to roll or 'h' then Enter to end turn: ")
        if choice == '':
            self.dice.roll()
            print(self.dice.value)
            if self.dice.value == 1:
                self.player.score_turn = 0
                print("Pig rolled, better luck next time.")
                self.dealer.dealer_turn()
                if self.dealer.score_total >= 100:
                    return
                self.play()
            else:
                self.player.score_turn += self.dice.value
                if self.dealer.score_total >= 100:
                    return
                if (self.player.score_total + self.player.score_turn) >= 100:
                    print(self.player.score_total, self.player.score_turn)
                    return print(f"Congratulations {self.player.name}, you have won this game of Pig!")
                print(
                    f"Your score for this turn so far is: {self.player.score_turn}.")
                self.play()
        if choice == 'h' or choice == 'H':
            self.player.score_total += self.player.score_turn
            print(f"Your total score is now: {self.player.score_total}.")
            self.dealer.dealer_turn()
            if self.dealer.score_total >= 100:
                return
            self.play()


class Dice:
    def __init__(self, sides):
        self.sides = sides
        self.value = 1

    def __str__(self):
        return f'{self.value}'

    def roll(self):
        self.value = randint(1, self.sides)


class Player:
    def __init__(self, name, score_turn=0, score_total=0):
        self.score_total = score_total
        self.score_turn = score_turn
        self.name = name

    def __str__(self):
        return f'Player: {self.name} Score for the turn: {self.score_turn} Total Score: {self.score_total}'


class Dealer:
    def __init__(self, score_turn=0, score_total=0):
        self.score_turn = score_turn
        self.score_total = score_total
        self.dice = Dice(dice_sides)

    def dealer_turn(self):
        self.dice.roll()
        if self.dice.value > 1:
            self.score_turn += self.dice.value
            if self.score_total + self.score_turn >= 100:
                self.score_total += self.score_turn
                return print("Sorry, the Dealer has won this round. Better luck next time!")
        if self.score_turn >= 20:
            self.score_total += self.score_turn
            return print(f"Dealer's score is now {self.score_total}.")
        self.dealer_turn()
        if self.dice.value == 1:
            self.score_turn = 0
            return print("Dealer has pigged this turn.")


new_game = Game("Austin")
new_game.play()

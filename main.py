from random import randint

houses = ("clubs", "spades", "hearts", "diamonds")
values = (2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A")


class Card:
    def __init__(self, cardHouse, cardValue):
        self.house = cardHouse
        self.value = cardValue


class Deck:
    def __init__(self):
        self.cards_list = []
        for house in houses:
            for value in values:
                self.cards_list.append(Card(house, value))
        self.print_deck()

    def print_deck(self):
        print(len(self.cards_list))
        for card in self.cards_list:
            print(f"Card = {card.house} : {card.value}")

    def shuffle_deck(self):
        shuffledDeck = []
        while len(self.cards_list) > 0:
            randomCard = randint(0, len(self.cards_list) - 1)
            shuffledDeck.append(self.cards_list.pop(randomCard))
        self.cards_list = shuffledDeck.copy()

    def deal_card(self):
        if len(self.cards_list) > 0:
            return self.cards_list.pop()
        else:
            print("Deck has no cards left")


class Player:
    def __init__(self):
        self.hand = []

    def add_card_to_hand(self, dealtCard):
        if isinstance(dealtCard.value, int):
            if self.current_score() + dealtCard.value <= 21:
                self.hand.append(dealtCard)
            else:
                print(f"Card {dealtCard.house}:{dealtCard.value} makes {self.current_score()} more than 21")
        else:
            if dealtCard.value in ("J", "Q", "K"):
                if self.current_score() + 10 <= 21:
                    self.hand.append(dealtCard)
                else:
                    print(f"Card {dealtCard.house}:{dealtCard.value} makes {self.current_score()} more than 21")
            else:
                if self.current_score() + 11 <= 21:
                    self.hand.append(Card(dealtCard.house, 11))
                elif self.current_score() + 1 <= 21:
                    self.hand.append(Card(dealtCard.house, 1))
                else:
                    print(f"Card {dealtCard.house}:{dealtCard.value} makes {self.current_score()} more than 21")

    def current_score(self) -> int:
        if len(self.hand) != 0:
            score = 0
            for card in self.hand:
                if card.value in ("J", "Q", "K"):
                    score += 10
                else:
                    score += card.value
            return score
        else:
            print("Player has an empty hand")
            return 0

    def print_hand(self):
        print(f"Count of cards in hand: {len(self.hand)}")
        print(f"Score from hand: {self.current_score()}")
        for card in self.hand:
            print(f"Hand Card: {card.value}")


TestDeck = Deck()
TestDeck.shuffle_deck()
TestDeck.shuffle_deck()

player1 = Player()

for i in range(0, 3):
    player1.add_card_to_hand(TestDeck.deal_card())

player1.print_hand()

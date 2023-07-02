# This is a program that reproduces the basic starting process of card games.
# This program will create a deck, shuffle the deck, and deal cards based on user input
import random

suits = ["Hearts", "Spades", "Diamonds", "Clubs"]
ranks = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", 
            "Eight", "Nine", "Ten", "Jack", "Queen", "King"]

def create_shuffled_deck():
    deck_of_cards = []

    for suit in suits:
        for rank in ranks:
            card = "%s of %s" % (rank, suit)
            deck_of_cards.append(card)

    random.shuffle(deck_of_cards)

    return deck_of_cards

deck = create_shuffled_deck()

def deal_hand():
    hand = []

    for card in range(5):
        card = deck[len(deck) - 1]
        hand.append(card)
        deck.pop(len(deck) - 1)

    return hand

def sort_hand_ranks(hand):
    hand_ranks = []

    for card in hand:
        for rank in ranks:
            if rank in card:
                hand_rank = int((ranks.index(rank))) + 1
                hand_ranks.append(hand_rank)

    hand_ranks.sort()

    return hand_ranks


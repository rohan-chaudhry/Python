# File: Poker.py

# Description: This file will attempt to simulate a regular poker game typically referred to as 5-Card Draw by randomly generating five hands and evaluating them.

# Student Name: Daniel Snyder

# Student UT EID: djs3928

# Partner Name: Rohan Chaudhry

# Partner UT EID: rc43755 

# Course Name: CS 313E

# Unique Number: 51335

# Date Created: 02/05/18

# Date Last Modified: 02/10/18

##################

import random

class Card (object):
    RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)
    SUITS = ('C', 'D', 'H', 'S')

    def __init__ (self, rank = 12, suit = 'S'):
        if (rank in Card.RANKS):
            self.rank = rank
        else:
            self.rank = 12
        if (suit in Card.SUITS):
            self.suit = suit
        else:
            self.suit = 'S'

    def __str__ (self):
        if (self.rank == 14):
            rank = 'A'
        elif (self.rank == 13):
            rank = 'K'
        elif (self.rank == 12):
            rank = 'Q'
        elif (self.rank == 11):
            rank = 'J'
        else:
            rank = str (self.rank)
        return rank + self.suit

    def __eq__ (self, other):
        return (self.rank == other.rank)

    def __ne__ (self, other):
        return (self.rank != other.rank)

    def __lt__ (self, other):
        return (self.rank < other.rank)

    def __le__ (self, other):
        return (self.rank <= other.rank)

    def __gt__ (self, other):
        return (self.rank > other.rank)

    def __ge__ (self, other):
        return (self.rank >= other.rank)

class Deck (object):
    def __init__ (self):
        self.deck = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                card = Card (rank, suit)
                self.deck.append (card)

    def shuffle (self):
        random.shuffle (self.deck)

    def deal (self):
        if (len(self.deck) == 0):
            return None
        else:
            return self.deck.pop(0)

class Poker (object):
    def __init__ (self, num_players):
        self.deck = Deck()
        self.deck.shuffle()
        self.players = []
        numcards_in_hand = 5
        self.points_hand = []

        for i in range (num_players):
            hand = []
            for j in range (numcards_in_hand):
                hand.append (self.deck.deal())
            self.players.append (hand)
            
    def play (self):
        # sort the hands of each player and print
        for i in range (len(self.players)):
            sortedHand = sorted (self.players[i], reverse = True)
            self.players[i] = sortedHand
            hand = ''
            for card in sortedHand:
                hand = hand + str (card) + ' '
            print ('Player ' + str (i + 1) + ": " + hand)
        print(" ")

        #determine each type of hand and print
        points_hand = [] # create list to store points for each hand

        # determine winner and print
        for i in range(len(self.players)):
            curHand = self.players[i]
            points_earned = self.is_royal(curHand, i+1)
            points_hand.append(points_earned)

        #print(points_hand)
        maxpoint = max(self.points_hand)
        maxindex = self.points_hand.index(maxpoint)

        print ('\nPlayer %d wins.'% (maxindex+1))
        '''
        pair_hands = []
        for i in range (len(self.players)):
            for j in range (len(self.players) - i):
                if hand[i] == 'One Pair':
                    if hand[i] == ha
        '''

    def point(self, hand):
        sortedHand = sorted(hand, reverse = True)
        c_sum = 0
        ranklist = []
        for card in sortedHand:
            ranklist.append(card.rank)
        c_sum = (ranklist[0]*13**4)+(ranklist[1]*13**3)+(ranklist[2]*13**2)+(ranklist[3]*13)+ranklist[4]
        return c_sum

    # determine if a hand is a royal flush
    def is_royal (self, hand, x):
        h = 10
        points_earned = h*13**5+self.point(hand)
        same_suit = True
        for i in range (len(hand) - 1):
            same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

        if (not same_suit):
            same_suit = False

        rank_order = True
        for i in range (len(hand)):
            rank_order = rank_order and (hand[i].rank == 14 - i)

        if (same_suit and rank_order):
            print ("Player", str(x) + ": Royal Flush")
            self.points_hand.append(points_earned)
            return int(points_earned)
        else:
            self.is_straight_flush(hand, x)

    def is_straight_flush (self, hand, x):
        straight_flush_flag = True
        h = 9
        suit_tracker = hand[0].suit
        rank_tracker = hand[0].rank
        points_earned = h*13**5+self.point(hand)
        
        for card in hand:
            if card.suit != suit_tracker or card.rank != rank_tracker:
                straight_flush_flag = False
                break
            else:
                rank_tracker -= 1
        if straight_flush_flag:
            print ("Player", str(x) + ": Straight Flush")
            self.points_hand.append(points_earned)
            return int(points_earned)
        else:
            self.is_four_kind(hand, x)

    def is_four_kind (self, hand, x):
        four_kind_flag = True
        h = 8
        rank_tracker = hand[1].rank
        match_counter = 0
        points_earned = h*13**5+self.point(hand)
        
        for card in hand:
            if card.rank == rank_tracker:
                match_counter +=1
        if match_counter >= 4:
            four_kind_flag = True
            print("Player", str(x) + ": Four of a Kind")
            self.points_hand.append(points_earned)
            return int(points_earned)
        else:
            self.is_full_house(hand, x)

    def is_full_house (self, hand, x):
        full_house_flag = True
        h = 7
        points_earned = h*13**5+self.point(hand)
        full_house_list = []

        for card in hand:
            full_house_list.append(card.rank)
        rank1 = hand[0].rank
        rank2 = hand[-1].rank
        count_rank1 = full_house_list.count(rank1)
        count_rank2 = full_house_list.count(rank2)
        if (count_rank1 == 2 and count_rank2 == 3) or (count_rank1 == 3 and count_rank2 == 2):
            full_house_flag = True
            print ("Player", str(x) + ": Full House")
            self.points_hand.append(points_earned)
            return int(points_earned)
        else:
            full_house_flag = False
            self.is_flush(hand, x)
            
    def is_flush (self, hand, x):
        flush_flag = True
        h = 6
        points_earned = h*13**5+self.point(hand)
        suit_tracker = hand[0].suit

        for card in hand:
            if (card.suit != suit_tracker):
                flush_flag = False
                break
        if (flush_flag):
            print ("Player", str(x) + ": Flush")
            self.points_hand.append(points_earned)
            return int(points_earned)
        else:
            self.is_straight(hand, x)

    def is_straight (self, hand, x):
        straight_flag = True
        h = 5
        points_earned = h*13**5+self.point(hand)
        rank_tracker = hand[0].rank

        for card in hand:
            if card.rank != rank_tracker:
                straight_flag = False
                break
            else:
                rank_tracker -= 1
        if (straight_flag):
            print("Player", str(x) + ": Straight")
            self.points_hand.append(points_earned)
            return int(points_earned)
        else:
            self.is_three_kind(hand, x)

    def is_three_kind (self, hand, x):
        three_kind_flag = True
        h = 4
        points_earned = h*13**5+self.point(hand)
        rank_tracker = hand[2].rank
        three_kind_list = []

        for card in hand:
            three_kind_list.append(card.rank)
        if three_kind_list.count(rank_tracker) == 3:
            three_kind_flag = True
            print ("Player", str(x) + ": Three of a Kind")
            self.points_hand.append(points_earned)
            return int(points_earned)
        else:
            three_kind_flag = False
            self.is_two_pair(hand, x)

    def is_two_pair (self, hand, x):
        two_pair_flag = True
        h = 3
        points_earned = h*13**5+self.point(hand)
        rank1 = hand[1].rank
        rank2 = hand[3].rank
        two_pair_list = []
        for card in hand:
            two_pair_list.append(card.rank)
        if two_pair_list.count(rank1) == 2 and two_pair_list.count(rank2) == 2:
            two_pair_flag = True
            print ("Player", str(x) + ": Two Pair")
            self.points_hand.append(points_earned)
            return int(points_earned)
        else:
            two_pair_flag = False
            self.is_one_pair(hand, x)
                   
    # determine if a hand is one pair
    def is_one_pair (self, hand, x):
        h = 2
        points_earned = h*13**5+self.point(hand)
        for i in range (len(hand) - 1):
            if (hand[i].rank == hand[i + 1].rank):
                print ("Player", str(x) + ": One Pair")
                self.points_hand.append(points_earned)
                print(points_earned) # delete
                return int(points_earned)
        self.is_high_card(hand, x)

    def is_high_card (self, hand, x):
        h = 1
        points_earned = h*13**5+self.point(hand)
        high_card_list = []
        for card in hand:
            high_card_list.append(card.rank)
        print ("Player", str(x) + ": High Card")
        self.points_hand.append(points_earned)
        print(points_earned)
        return int(points_earned)

def main():
    # prompt user to enter the number of players
    num_players = int (input ('Enter number of players: '))
    while ((num_players < 2) or (num_players > 6)):
        num_players = int (input ('Enter number of players: '))

    # create the Poker object
    game = Poker (num_players)

    # play the game of poker
    print(" ")
    game.play()

    #print(" ")
    #for i in range(num_players):
        #current_hand = game.players[i]
        #print ("Hand " + str(i+1) + ": ", end = "")
        #game.is_royal(current_hand)

    #highest_score = max(game.points_hand)
    #highest_score_index = game.points_hand.index(highest_score)
    #print ('\nHand %d wins'% (highest_score_index + 1))

main()
    





















            

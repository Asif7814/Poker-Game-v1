import card_games_toolbox_v1

suits = card_games_toolbox_v1.suits
ranks = card_games_toolbox_v1.ranks

players = []
player_hands_list = []
player_hand_ranks_list = []
player_hand_tiers_list = []
player_hand_types_list = []

num_of_players = 2

print("v1")
print("---------------------------------")

for i in range(num_of_players):
    player_hand = card_games_toolbox_v1.deal_hand()
    player_hands_list.append(player_hand)
    
    player_hand_ranks = card_games_toolbox_v1.sort_hand_ranks(player_hand)
    player_hand_ranks_list.append(player_hand_ranks)

    player = i + 1
    players.append(player)

def is_flush(player_hand):
    # determine the suit of the first card
    for suit in suits:
        if suit in player_hand[0]:
            first_card_suit = suit

    # count to see if it is a flush
    count = 0

    for card in player_hand:
        if first_card_suit in card:
            count += 1 

    if count == 5:
        return True    
    
    return False  

def is_straight(player_hand_ranks):
    count = 0
    
    # for the iteration between the second card and the end of the hand 
    for i in range(1, len(player_hand_ranks)):
        # if the rank of the first card is one less than the rank of the second card, then increase count by 1
        if player_hand_ranks[i] - 1 == player_hand_ranks[i - 1]:
            count += 1

    # if the count reaches 4, it means all the ranks in the hand are ascending by 1, so it is a Straight
    if count == 4:
        return True
    
    return False

def is_royal_flush(player_hand_ranks):
    count = 0

    for i in range(2, len(player_hand_ranks)):
        if player_hand_ranks[i] - 1 == player_hand_ranks[i - 1]:
            count += 1

    if count == 3 and (1 in player_hand_ranks) and (13 in player_hand_ranks):
        return True 
    
    return False

def is_four_of_a_kind(player_hand_ranks):
    if player_hand_ranks.count(player_hand_ranks[0]) == 4 or player_hand_ranks.count(player_hand_ranks[4]) == 4:
        return True 
    
    return False

def is_matching_sets(player_hand_ranks): 
    count_one = 1
    count_two = 1

    for i in range(1, len(player_hand_ranks) - 2): # counts matching sets from start to middle
        if player_hand_ranks[i] == player_hand_ranks[i - 1]:
            count_one += 1

    for i in range(2, len(player_hand_ranks) - 1): # counts matching sets from middle to end
        if player_hand_ranks[i] == player_hand_ranks[i + 1]:
            count_two += 1

    is_full_house = (count_one == 3 and count_two == 2) or count_one == 2 and count_two == 3
    is_two_pair = count_one == 2 and count_two == 2
    is_three_of_a_kind = (player_hand_ranks[1] == player_hand_ranks[3]) or (count_one == 3 or count_two == 3)
    is_pair = count_one == 2 or count_two == 2

    if is_full_house:
        return "FH"
    elif is_three_of_a_kind:
        return "TK"
    elif is_two_pair:
        return "TP"
    elif is_pair:
        return "P"
    else:
        return ""
            
def det_player_hand_tier(hand, hand_ranks):
    hand_tier = 0

    matching_sets_result = is_matching_sets(hand_ranks)

    is_full_house = matching_sets_result == "FH"
    is_two_pair = matching_sets_result == "TP"
    is_three_of_a_kind = matching_sets_result == "TK"
    is_pair = matching_sets_result == "P"

    if is_flush(hand):
        if is_royal_flush(hand_ranks):
            hand_tier = 10 
        elif is_straight(hand_ranks):
            hand_tier = 9
        else:
            hand_tier = 6
    elif is_straight(hand_ranks):
        hand_tier = 5
    elif is_four_of_a_kind(hand_ranks):
        hand_tier = 8
    elif is_full_house:
        hand_tier = 7
    elif is_three_of_a_kind:
        hand_tier = 4
    elif is_two_pair:
        hand_tier = 3
    elif is_pair:
        hand_tier = 2
    else:
        hand_tier = 1

    return hand_tier

def det_player_hand_type(player_hand_tier):
    hand_type = ""

    if player_hand_tier == 10:
        hand_type = "Royal Flush"
    elif player_hand_tier == 9:
        hand_type = "Straight Flush"
    elif player_hand_tier == 8:
        hand_type = "Four of a Kind"
    elif player_hand_tier == 7:
        hand_type = "Full House"
    elif player_hand_tier == 6:
        hand_type = "Flush"
    elif player_hand_tier == 5:
        hand_type = "Straight"
    elif player_hand_tier == 4:
        hand_type = "Three of a Kind"
    elif player_hand_tier == 3:
        hand_type = "Two Pair"
    elif player_hand_tier == 2:
        hand_type = "Pair"
    else:
        hand_type = "High Card"

    return hand_type

for i in range(len(player_hand_ranks_list)):
    # creates a 2d list comprising of the player and their particular hand tier; first item shows tier, second shows player
    player_hand_tier = det_player_hand_tier(player_hands_list[i], player_hand_ranks_list[i])
    player_hand_tiers_list.append(player_hand_tier)

    # determines the hand types for each player; for purpose of displaying on screen
    player_hand_type = det_player_hand_type(player_hand_tiers_list[i])
    player_hand_types_list.append(player_hand_type)
    
def print_player_hands():
    for i in range(len(player_hands_list)):
        print("Player " + str(i + 1) + ": ")
        print(player_hands_list[i])
        print(player_hand_ranks_list[i])
        print("Hand: %s [%s]" %(str(player_hand_types_list[i]), str(player_hand_tiers_list[i])))
        print()    

def det_poker_game_results():
    for i in range(1, len(player_hand_tiers_list)):
         better_hand = players[i-1]
         if player_hand_tiers_list[i] >= player_hand_tiers_list[i - 1]:
            # if two hand_tiers are the same, order the players based on the high card; from greatest to least
            if player_hand_tiers_list[i] == player_hand_tiers_list[i - 1]:
                high_card = players[i - 1]
                if player_hand_ranks_list[i] > player_hand_ranks_list[i-1]:
                    players[i - 1] = players[i]
                    players[i] = high_card 
            # else it must be greater; order the players by hand_tiers from greatest to least
            else:        
                players[i - 1] = players[i]
                players[i] = better_hand

    # prints the game results
    print("Poker Game Leaderboard: ")
    print("---------------------------------")
    for player in players:
        print("#%s - Player %s" % (players.index(player) + 1, player))


print_player_hands()
print("---------------------------------")
det_poker_game_results()
print()
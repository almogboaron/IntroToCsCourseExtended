def poker_hand(hand):
    # ["High Card", "One Pair", "Two Pairs", "Three of a Kind", "Straight", "Flush", "Full House", "Four of a Kind", "Straight Flush", "Royal Flush"]
    cards = str.split(hand)
    straight_check = 0
    flush_check = 0
    for letter in "HDCS":
        counter = 0
        for card in cards:
            if letter in card:
                counter += 1
        if counter == 5:
            flush_check = 1
            break
        if counter in range(1, 5):
            break
    seg = "23456789TJQKA"
    myhand = []
    straight_counter = 0
    straight_check = 0
    for letter in seg:
        counter = 0
        for card in cards:
            if letter in card:
                counter += 1
        if counter == 0:
            straight_counter = 0
        elif counter == 1:
            straight_counter += 1
            if straight_counter == 5:
                straight_check = 1
        elif counter == 2:
            myhand.append(2)
        elif counter == 3:
            if sum(myhand) == 2:
                return
            myhand.append(3)
        elif counter == 4:
            return "Four of a Kind"
    if flush_check:
        if straight_counter == 5:
            return "Royal Flush"
        if straight_check:
            return "Straight Flush"
        return "Flush"
    if straight_check:
        return "Straight"
    if sum(myhand) == 2:
        return "One Pair"
    if sum(myhand) == 3:
        return "Three of a Kind"
    if sum(myhand) == 4:
        return "Two Pairs"
    if sum(myhand) == 5:
        return "Full House"
    return "High Card"


if poker_hand("5H 5C 6S 7S KD") != 'One Pair' or \
    poker_hand("5D 8C 9S JS AC") != 'High Card' or \
    poker_hand("3D 6D 7D TD QD") != 'Flush' or \
    poker_hand("3C 3D 3S 9S 9D") != 'Full House' or \
    poker_hand("AC TC JC KC QC") != 'Royal Flush' or \
    poker_hand("AC TC JC KC QD") != 'Straight':
    print("error in poker_hand")







import array
import random
deck = array.array('f',[1,2,3,4,5,6,7,8,9,10])
blackjack = array.array('f', [21])

def dealer_deal():
    hand_dealer = array.array('f',[])
    deal = random.choice (deck)
    hand_dealer.append(deal)
    print(f"This is the dealer's hand {list(hand_dealer)}, and one hidden card.")
    hand_dealer.append(deal)

    return hand_dealer

def player_deal():
    hand_player = array.array('f',[])
    deal = random.choice (deck)
    hand_player.append(deal)
    deal = random.choice (deck)
    hand_player.append(deal)

    return hand_player
    

def sum_hit(hand_player):
    hit = 'y'
    
    while sum(hand_player) < 21 and hit == 'y':
        print(f"This is the player's hand {list(hand_player)}")
        hit = input("Would you like to hit? y/n: ")
        if hit == 'y':
            deal = random.choice(deck)
            hand_player.append(deal)
            print(f"{deal}")
        elif hit == 'n':
            print(f"Final hand: {list(hand_player)} Total: {sum(hand_player)}")
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
    
    if sum(hand_player) > 21:
        print(f"cringe! You lost. {sum(hand_player)}")
    elif sum(hand_player) == 21:
        print(f"21! {sum(hand_player)}")

    return hand_player
 
def dealer_logic(deal_hand):
    hand = sum(list(deal_hand))
    while hand < 17:
        deal = random.choice(deck)
        deal_hand.append(deal)
        hand = sum(list(deal_hand))
    return hand

def main():
    deal_hand = dealer_deal()
    hand_player = player_deal()
    d_hand = dealer_logic(deal_hand)
    print(d_hand)
    play_hand = sum_hit(hand_player)

    if d_hand < 21 and d_hand > sum(play_hand):
        print(f"Dealer hand greater," , sum(deal_hand))
    elif sum(deal_hand) > 21:
            print(f"Dealer bust." , sum(deal_hand))
    elif play_hand > deal_hand:
            print(f"Player hand closer to Blackjack! Player win." , sum(play_hand))
    else:
            print("Dealer win. Cringe.")

main()
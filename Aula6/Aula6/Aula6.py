import random


deck_player=["1","2","3","4","5","6","7","8","9","10","J","Q","K","A"]
deck_npc=["1","2","3","4","5","6","7","8","9","10","J","Q","K","A"]

def shuffle(): #shuffles both decks
    random.shuffle(deck_player)
    random.shuffle(deck_npc)


def show(): #prints both decks' contents
    print("Player Deck:",deck_player)
    print("NPC Deck", deck_npc)
    
def fish(deck): #returns the top 2 cards of the inputted deck
    top1=deck[-1]
    top2=deck[-2]
    hand=[top1,top2]
    return hand
   

def value(card): #returns the point value of the inputted card
    if card =="J":
        return 11
    elif card =="Q":
        return 12
    elif card=="K":
        return 13
    elif card=="A":
        return 14
    else:
        return int(card)



def compare(hand_player,hand_npc): #returns 1,-1 or 0 when the player's 2 cards are worth more, less or the same as the npc's
    
    pnt_player=value(hand_player[0])+value(hand_player[1])
    pnt_npc=value(hand_npc[0])+value(hand_npc[1])

    if pnt_player>pnt_npc:
        return 1
    elif pnt_player<pnt_npc:
        return -1
    else:
        return 0


inp="debug"
while inp!="n":
    shuffle()
    hand_player=fish(deck_player)
    print("Your hand:",hand_player)
    print("1)Discard both cards")
    print("2)Discard 1 card")
    print("3)Keep current hand")
    inp=input("Select option: (1/2/3):")
    if inp=="1":
        hand_player=(deck_player[-3],deck_player[-4])
    elif inp=="2":
        inp=input("Discard first or second card? (1/2):")
        if inp=="1":
            hand_player=[deck_player[-3],hand_player[1]]
        elif inp=="2":
            hand_player=[hand_player[0],deck_player[-3]]
    

    hand_npc=fish(deck_npc)
    print("Your hand:",hand_player)
    print("Opponent's hand:",hand_npc)
    res=compare(hand_player,hand_npc)
    
    if res==1:
        print("Winner!")
    elif res==-1:
        print("You lose")
    else:
        print("Draw")

    inp=input("Play again? (y/n):")










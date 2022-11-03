import random


deck_player=["1","2","3","4","5","6","7","8","9","10","J","Q","K","A"]
deck_npc=["1","2","3","4","5","6","7","8","9","10","J","Q","K","A"]

def shuffle():
    random.shuffle(deck_player)
    random.shuffle(deck_npc)


def show():
    print("Player Deck:",deck_player)
    print("NPC Deck", deck_npc)
    
def fish(deck):
    top1=deck[-1]
    top2=deck[-2]
    return top1, top2
   

def value(card):
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



def compare():
    top_player=fish(deck_player)
    top_npc=fish(deck_npc)
    
    pnt_player=value(top_player[0])+value(top_player[1])
    pnt_npc=value(top_npc[0])+value(top_npc[1])

    if pnt_player>pnt_npc:
        return 1
    elif pnt_player<pnt_npc:
        return -1
    else:
        return 0




shuffle()
show()
print(fish(deck_player))
print(fish(deck_npc))
print(compare())





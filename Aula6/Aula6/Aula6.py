import random


deck_player=["1","2","3","4","5","6","7","8","9","10","J","Q","K","A"]
deck_npc=["1","2","3","4","5","6","7","8","9","10","J","Q","K","A"]

def shuffle():
    global deck_player, deck_npc
    random.shuffle(deck_player)
    random.shuffle(deck_npc)


def show():
    print("Player Deck:",deck_player)
    print("NPC Deck", deck_npc)
    
def fish():
    #global deck_player
    top1=deck_player[-1]
    top2=deck_player[-2]
    return top1, top2
    



shuffle()
show()
print(fish())
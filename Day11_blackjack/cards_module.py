import random

# cards를 만든다. 카드 개수만큼 만들어서 하나가 뽑히면 이를 제거할 예정
# 구현의 편의를 위해 Ace는 11로 설정 calculate_score 함수에서 확인할 수 있음
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]

def pop_random_card():
    """
    cards에서 무작위로 하나를 뽑아 return하고 해당 값을 cards에서 삭제하는 함수
    게임이 cards가 빌 때까지 진행될 수 없으니 len(cards)가 0이 되는 경우는 고려하지 않아도 됨
    """
    idx = random.randint(0, len(cards) - 1)
    return cards.pop(idx)

def calculate_score(player_cards):
    """
    카드의 총합을 반환하는 함수
    """
    #ace는 1 또는 11이 되므로 카드가 2개가 있을 때는 1을 11로 선택
    if sum(player_cards) == 21 and len(player_cards) == 2:
        return (21)
    # ace 카드가 있을 때의 선택
    elif 11 in player_cards and sum(player_cards) > 21:
            player_cards.remove(11)
            player_cards.append(1)
        
    return (sum(player_cards))

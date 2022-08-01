import random
from art import logo
from replit import clear
  

def deal_card():
  cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
  return random.choice(cards)
  
def calculate_score(hand):
  if sum(hand) > 21 and len(hand) == 2:
    return 0

  if 11 in hand and sum(hand) > 21:
    hand.remove(11)
    hand.append(1)
  return sum(hand)
  
def compare_scores(user_score, dealer_score):
  if user_score > 21 and dealer_score > 21:
    return "You went over. You lose 😤"


  if user_score == dealer_score:
    return "Draw 🙃"
  elif dealer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif dealer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > dealer_score:
    return "You win 😃"
  else:
    return "You lose 😤"
  

def blackjack():
  print(logo)
  user_hand = []
  dealer_hand = []
  is_game_over = False
  
  for _ in range(2):
    user_hand.append(deal_card())
    dealer_hand.append(deal_card())

  while not is_game_over:
    user_score = calculate_score(user_hand)
    dealer_score = calculate_score(dealer_hand)
    print(f"Your cards: {user_hand}. Your score: {user_score}")
    print(f"Dealer's first card: {dealer_hand[0]}")

    if user_score == 0 or dealer_score == 0 or user_score > 21:
      is_game_over = True
    else: 
      user_should_deal = input("Would you like another card or stand? 'Y' or 'N'").lower()
      if user_should_deal == 'y':
        user_hand.append(deal_card())
      else:
        is_game_over = True
  while dealer_score != 0 and dealer_score <17:
    dealer_hand.append(deal_card())
    dealer_score = calculate_score(dealer_hand)
  print(f"   Your final hand: {user_hand}, final score: {user_hand}")
  print(f"   Dealer's final hand: {dealer_hand}, final score: {dealer_score}")
  print(compare_scores(user_score, dealer_score))
    


    

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
  clear()
  blackjack()
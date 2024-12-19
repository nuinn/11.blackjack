import random
import os

logo = r"""
.------.            _     _            _    _            _
|A_  _ |.          | |   | |          | |  (_)          | |
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |
      `------'                           |__/
"""

def deal_card(deck):
  index = random.randint(0, len(deck) - 1)
  card = deck.pop(index)
  return card

def starting_deal(game):
  game["player"].append(deal_card(game["deck"]))
  game["dealer"].append(deal_card(game["deck"]))
  game["player"].append(deal_card(game["deck"]))
  game["dealer"].append(deal_card(game["deck"]))

def get_score(cards):
  score = 0
  for card in cards:
    if isinstance(card, int):
      score += card
    elif card == 'A':
      score += 11
    else:
      score += 10
  index = 0
  while score > 21 and index < len(cards):
    if cards[index] == 'A':
      score -= 10
    index +=1
  return score

def error_handler(input_string):
  while True:
    response = input(input_string)
    if response.lower() == 'y' or response.lower() == 'n':
      break
  return response.lower()

def print_gamestate(game):
  print(f"Your cards: {game["player"]}, current score: {get_score(game["player"])}")
  print(f"Dealer's first card: {game["dealer"][0]}")

def get_winner(player_score, dealer_score):
  if dealer_score > 21:
    return "Opponent went over. You win 😁"
  if player_score > dealer_score:
    if player_score == 21:
      return "Win with a Blackjack 😎"
    return "You win 😃"
  if dealer_score > player_score:
    if dealer_score == 21:
      return "Lose, opponent has a Blackjack 😱"
    return "You lose. 😤"
  else:
    return "It's a draw 🙃"

possible_cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

while True:
  live_game = error_handler("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
  if live_game == 'n':
    break
  os.system('cls' if os.name == 'nt' else 'clear')
  print(logo)
  game = {
    "deck": possible_cards * 4,
    "player": [],
    "dealer": [],
  }
  starting_deal(game)
  print_gamestate(game)

  bust = False
  while not bust:
    hit_me = error_handler("Type 'y' to get another card, type 'n' to pass: ")
    if hit_me == 'n':
      break
    game["player"].append(deal_card(game["deck"]))
    print_gamestate(game)
    if get_score(game["player"]) > 21:
      bust = True

  if bust:
    print('You went over. You lose 😭')

  else:
    while get_score(game["dealer"]) < 17:
      game["dealer"].append(deal_card(game["deck"]))

    player_score = get_score(game["player"])
    dealer_score = get_score(game["dealer"])

    print(f"Your final hand: {game["player"]}, final score: {player_score}")
    print(f"Dealer's final hand: {game["dealer"]}, final score: {dealer_score}")
    print(get_winner(player_score, dealer_score))


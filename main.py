from art import logo, vs
from game_data import data
import random
import os

def random_name():
  random_dic = random.choice(data)
  return random_dic

def format_data(account):
  account_name = account['name']
  account_description = account['description']
  account_country = account['country']
  return f"{account_name}, a {account_description}, from {account_country}"

def check(ans, countA, countB):
  if countA > countB:
    if ans == 'A':
      return True
    else:
      return False
  elif countA < countB:
    if ans == 'B':
      return True
    else:
      return False

print(logo)
count = 0
stop_compare = False
compare_list = random_name()
against_list = random_name()

while not stop_compare:  
  compare_list = against_list
  against_list = random_name()
  while compare_list == against_list:
    against_list = random_name()
  print(f"Compare A: {format_data(compare_list)}")
  print(vs)
  print(f"Against B: {format_data(against_list)}")
  ans = input("Who has more followers? Type 'A' or 'B': ").upper()
  compare_count = compare_list['follower_count']
  against_count = against_list['follower_count']
  os.system("clear")
  print(logo)
  if check(ans, compare_count, against_count):
    count += 1
    print(f"You are right! Current score: {count}")
  else:
    stop_compare = True
    os.system("clear")
    print(f"Sorry, that's wrong. Final score: {count}")
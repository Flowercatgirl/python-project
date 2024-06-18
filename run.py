import os
import random
import gspread
from character import Hero, Enemy
from weapon import short_bow, iron_sword, fists
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
CREDS = Credentials.from_service_account_file('creds.json')

SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

sales = SHEET.worksheet('sales')

data = sales.get_all_values()

print(data)

# Create a lists of weapons
weapons = [iron_sword, fists, short_bow]

# Create 2 players and assign a random weapon to each

hero = Hero(name = 'Hero', health = 100, weapon = random.choice(weapons))
enemy = Enemy(name = 'Enemy', health = 100, weapon = random.choice(weapons))

while hero.health != 0 and enemy.health != 0:
    # In this game loop I am calling the attack methods of both the hero and the enemy

    os.system('clear')
    hero.attack(enemy)
    enemy.attack(hero)

    hero.health_bar.draw()
    enemy.health_bar.draw()

    input()

if hero.health == 0 and enemy.health == 0:
    print("Let's call it a draw.")
elif hero.health == 0:
    print(f'{enemy.name} is a Winner!!!')
elif enemy.health == 0:
    print(f'{hero.name} is a Winner!!!')
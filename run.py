import gspread
from character import Hero, Enemy
from weapon import short_bow
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

# Create 2 players

hero = Hero(name = 'Hero', health = 100)
enemy = Enemy(name = 'Enemy', health = 100, weapon = short_bow)

while True:
    # In this game loop I am calling the attack methods of both the hero and the enemy
    hero.attack(enemy)
    enemy.attack(hero)

    print(f'Health of {hero.name}: {hero.health}')
    print(f'Health of {enemy.name}: {enemy.health}')

    input()


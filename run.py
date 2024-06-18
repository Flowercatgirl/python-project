from os import system, name
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
SHEET = GSPREAD_CLIENT.open('game_results')


# Define a terminal clear function
def clear():

    # for Windows
    if name == 'nt':
        _ = system('cls')

    # for Mac and Linux
    else:
        _ = system('clear')


# Create a lists of weapons
weapons = [iron_sword, fists, short_bow]

# Create 2 players and assign a random weapon to each

hero = Hero(name='Hero', health=100, weapon=random.choice(weapons))
enemy = Enemy(name='Enemy', health=100, weapon=random.choice(weapons))

while hero.health != 0 and enemy.health != 0:
    # Calling the attack methods of both the hero and the enemy

    clear()
    hero.attack(enemy)
    enemy.attack(hero)

    hero.health_bar.draw()
    enemy.health_bar.draw()

    input()


def get_battle_data():
    '''
    Get battle results data
    '''
    data = []
    if hero.health == 0 and enemy.health == 0:
        data = [0, 0, 1]
        print("Let's call it a draw.\n")
    elif hero.health == 0:
        data = [0, 1, 0]
        print(f'{enemy.name} is a Winner!!!\n')
    elif enemy.health == 0:
        data = [1, 0, 0]
        print(f'{hero.name} is a Winner!!!\n')

    return data


# Create a function to update a game worksheet
def update_game_worksheet(data):
    '''
    Update history worksheet, add new row with battle result
    '''

    print('Updating the results...\n')
    history_worksheet = SHEET.worksheet('history')
    history_worksheet.append_row(data)
    print('Results successfully updated.\n')


battle_data = get_battle_data()
update_game_worksheet(battle_data)

# Check how many history rows are full in the worksheet
worksheet = SHEET.get_worksheet(0)
rows = worksheet.get_all_values()
filled_rows = len(rows)

# if there are more than 50 - delete the first data row at the start
if filled_rows > 50:
    worksheet.delete_rows(2)

# Count how many times hero and enemy won and draw happenned

# Define the Character column index you want to check
column_index = 1
cell_value = worksheet.acell('A1').value

while column_index < 3:

    # Get all values in the specified column
    column_values = worksheet.col_values(column_index)

    # Function to check if a value is an integer
    def is_integer(value):
        try:
            return int(value)
        except ValueError:
            return None

    # Sum the integer values (how many victories) in the column
    integer_sum = sum(is_integer(value)
                      for value in column_values
                      if is_integer(value) is not None)

    print(f"{cell_value} has won {integer_sum} times so far")

    cell_value = worksheet.acell('B1').value
    column_index += 1

print(f"{worksheet.acell('C1').value} has happened {integer_sum} times so far\n")

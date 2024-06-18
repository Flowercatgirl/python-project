# Epic Battle - A Command Line Interface Quiz Game

![Epic Battle](images/game.jpg)

## Portfolio 3 Python project
Epic Battle is a 2 Characters Command Line Interface game where Hero and Enemy fight to win.

The live link can be found [here](https://epic-battle-2452b7f71b56.herokuapp.com/)

[Google Sheet game_results](https://docs.google.com/spreadsheets/d/1sdG2CdFVH0bLmYMzo-3HmMyNibCLyjya37lIib3h-SU/edit?usp=sharing)

## How to play

At the start of the game Hero and Enemy get randomly assigned weapons: it can be Iron Sword, Short Bow or Fists.

Iron Sword is the most powerful one, it does the most damage, then goes Short Bow and the weakest weapon are bare Fists.

By pressing enter both parties get hit until eventually the weakest gets defeated.

The game is over and the Winner is declared. 

The result gets recorded to Google Sheet, information about previos games gets retrieved and displayed on the screen.

## Features

### Random weapon generation
* Hero and Enemy get randomly assigned weapons: it can be Iron Sword, Short Bow or Fists.

### Graphical health bar
* Text-based graphics to show health status for both fighters.

### Maintains Scores
* The result gets recorded to Google Sheet, information about previos games gets retrieved and displayed on the screen.

## Future Features

* Allow the user to choose from more weapons

* Allow the user to choose between different styles of Health bars

* Allow the user to choose from multiple different Enemies

## Data Model

This is an object oriented application.

It has 3 main classes: Character, Weapon and Health Bar, that are stored in 3 separate .py files.

Character class has 2 subclasses: Hero and Enemy.

This game uses Google Sheets API to store the results.

## Testing

I have tested this project with pycodestyle 2.12.0

## Deployment

This project was developed through Gitpod, using Code Institue's mock terminal for Heroku and their way of linking to Google Sheet API.

## Credits

* Code Instiute 'Love Sandwiches' project

* [The Heroku Checklist](https://code-institute-students.github.io/heroku-update-checklist/)

* [Learn Python Classes With a Text-Based Battle - OOP Tutorial](https://www.youtube.com/watch?v=cM_ocyOrs_k)

* [How to clear screen in python](https://www.geeksforgeeks.org/clear-screen-python/)
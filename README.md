# Wellness Bingo
![](https://github.com/ryan-lam/WellnessBingo/blob/main/static/wellness-bingo.png)

## Inspiration
We were inspired by the gamification of simple day-to-day activities and tasks, and decided to apply that gamification concept to health and wellness

## What it does
Wellness Bingo is basically a bingo game where the player has to complete tasks (that are written on the board) to get the corresponding tile on the bingo board. To win the game, a person will need to get 2 rows filled up. It is a website and can be view on a mobile device (since is intended for mobile devices and multiple players). It is intended for outdoor use, where players can walk/run/race to different places to complete tasks

## How we built it
We built a database of potential tasks that are to be done by the user. The board that the player gets will always be different because the tiles on the board is generated randomly. Using Flask and Python, we built a backend to do all the necessary calculations and return that info to the frontend. When the user interacts with the program, important info will be sent to the backend and written in an array (that represents the bingo board)

## Challenges we ran into
- Getting the tiles of the board to change colors
- Creating the "Not done" button which undos a task (reverting it back to the original tile)
- Getting the board to not reset itself after every user input

## Accomplishments that we're proud of
- Problem solving and "thinking out of the box" when we ran into problems (ie. using images for tiles instead of text)
- Getting something of this difficulty done (we did not expect to finish)

## What we learned
- How to read/write info between the front and backend using Flask
- Working with 3D arrays in python

## What's next for Wellness Bingo
- Have custom tasks that users can add
- Add an animation for when the tasks are completed and tiles change color

## Demo Video
[Wellness Bingo - Demo Video](https://youtu.be/RXuirUNSwhM)

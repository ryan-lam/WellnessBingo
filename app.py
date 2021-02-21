from flask import Flask, redirect, url_for, render_template, request
import random
import sys

app = Flask(__name__)

matrix = [[['do 10 jumping jacks', False, 'red.png'], ['find a dog', False, 'red.png'], ['find a watch', False, 'red.png'], ['find an old coin', False, 'red.png'], ['budget your money', False, 'red.png']], 
          [['draw a stickman', False, 'red.png'], ['listen to music', False, 'red.png'], ['watch a streamer', False, 'red.png'], ['search for a Leonardo DiCaprio movie', False, 'red.png'], ['play a game of chess', False, 'red.png']], 
          [['learn a new skill', False, 'red.png'], ['experiment with different spices', False, 'red.png'], ['drink a cup of water', False, 'red.png'], ['write down your dreams', False, 'red.png'], ['eat a piece of chocolate', False, 'red.png']], 
          [['read about igloos', False, 'red.png'], ['watch an NBA game', False, 'red.png'], ['message a friend', False, 'red.png'], ['get some sun light', False, 'red.png'], ['jump up and down 5 times', False, 'red.png']], 
          [['complete a jigsaw puzzle', False, 'red.png'], ['play a brain teaser', False, 'red.png'], ['write down gift ideas', False, 'red.png'], ['learn about wellness', False, 'red.png'], ['wash your hands', False, 'red.png']], 
          [['run up and down some stairs', False, 'red.png'], ['find medicine or supplements', False, 'red.png'], ['watch a documentary', False, 'red.png'], ['find cooking oil', False, 'red.png'], ['make salt water', False, 'red.png']], 
          [['get a bottle of red.png bull', False, 'red.png'], ['search up bitcoin', False, 'red.png'], ['take a shower', False, 'red.png'], ['write something on a calendar', False, 'red.png'], ['get a stuffed animal', False, 'red.png']], 
          [['touch a figurine', False, 'red.png'], ['fill a bottle up with water', False, 'red.png'], ['play a note on a piano', False, 'red.png'], ['draw a digital art', False, 'red.png'], ['fold a paper air plane', False, 'red.png']], 
          [['find an electricity outlet', False, 'red.png'], ['write a sentence', False, 'red.png'], ['look at the clouds', False, 'red.png'], ['find a dead tree branch', False, 'red.png'], ['touch soap', False, 'red.png']]]

original = [['qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png'], 
          ['qmark.png', 'qmark.png', 'qmark.png', "qmark.png", "qmark.png"], 
          ['qmark.png', "qmark.png", 'qmark.png', "qmark.png", "qmark.png"], 
          ['qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png'], 
          ['qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png']]

answer = [['red.png', 'red.png', 'red.png', 'red.png', 'red.png'], 
           ['red.png', 'red.png', 'red.png', "red.png", "red.png"], 
           ['red.png', "red.png", 'red.png', "red.png", "red.png"], 
           ['red.png', 'red.png', 'red.png', 'red.png', 'red.png'], 
           ['red.png', 'red.png', 'red.png', 'red.png', 'red.png']]

colours = [['qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png'], 
          ['qmark.png', 'qmark.png', 'qmark.png', "qmark.png", "qmark.png"], 
          ['qmark.png', "qmark.png", 'qmark.png', "qmark.png", "qmark.png"], 
          ['qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png'], 
          ['qmark.png', 'qmark.png', 'qmark.png', 'qmark.png', 'qmark.png']]

def func(i, j, status):
  global matrix
  matrix[i][j][1] = status

  if matrix[i][j][1] == True:
    colours[i][j] = "red.png"
    return matrix[i][j]
  else:
    colours[i][j] = "qmark.png"
    return [matrix[i][j][0], matrix[i][j][1], None]

def writeAnswer():
  for i in range(0, 5):
    for j in range(0,5):
      colours[i][j] = "red.png"

def resetAnswer():
  for i in range(0, 5):
    for j in range(0,5):
      colours[i][j] = "qmark.png"

# @app.route('/', methods=['POST', 'GET'])
# def index():
    
#     if request.method == 'POST':
#         try:
#             pos = request.form["content"]
#             x = pos.split(" ")[0]
#             y = pos.split(" ")[1]
#             print(pos)
#             print(x)
#         except:
#             print("ERROR")
        
#         return render_template('index.html')
#     return render_template('index.html')


@app.route('/', methods=['POST', 'GET'])
def check():
    result = ["HEYY", False, "qmark.png"]
    if request.method == "POST":
        
        try:
          pos = request.form["content"].split(" ")
          print(pos)
          x = int(pos[0])
          y = int(pos[1])
          state = pos[2]
          if(state == "True"):
            result = func(x,y,True)
          elif(state == "False"):
            result = func(x,y,False)
          elif(state == "Complete"):
            writeAnswer()
          else:
            resetAnswer()
          print(result[2])
        except:
          print("ERROR")
        
        return render_template("index.html", colour00 = colours[0][0], colour01 = colours[0][1], colour02 = colours[0][2], colour03 = colours[0][3], colour04 = colours[0][4],
        colour10 = colours[1][0], colour11 = colours[1][1], colour12 = colours[1][2], colour13 = colours[1][3], colour14 = colours[1][4],
        colour20 = colours[2][0], colour21 = colours[2][1], colour22 = colours[2][2], colour23 = colours[2][3], colour24 = colours[2][4],
        colour30 = colours[3][0], colour31 = colours[3][1], colour32 = colours[3][2], colour33 = colours[3][3], colour34 = colours[3][4], 
        colour40 = colours[4][0], colour41 = colours[4][1], colour42 = colours[4][2], colour43 = colours[4][3], colour44 = colours[4][4], description = result[0])

    return render_template("index.html", colour00 = colours[0][0], colour01 = colours[0][1], colour02 = colours[0][2], colour03 = colours[0][3], colour04 = colours[0][4],
        colour10 = colours[1][0], colour11 = colours[1][1], colour12 = colours[1][2], colour13 = colours[1][3], colour14 = colours[1][4],
        colour20 = colours[2][0], colour21 = colours[2][1], colour22 = colours[2][2], colour23 = colours[2][3], colour24 = colours[2][4],
        colour30 = colours[3][0], colour31 = colours[3][1], colour32 = colours[3][2], colour33 = colours[3][3], colour34 = colours[3][4], 
        colour40 = colours[4][0], colour41 = colours[4][1], colour42 = colours[4][2], colour43 = colours[4][3], colour44 = colours[4][4], description = result[0])


if __name__ == "__main__":
    app.run(debug=True, port=8080)

#pip3 install virtualenv
#virtualenv env
#source env/bin/activate
#pip3 install flask 
# TO kill as port -> sudo lsof -iTCP:8080 -sTCP:LISTEN


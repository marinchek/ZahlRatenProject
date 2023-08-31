from flask import Flask, render_template, request, redirect, url_for, session
from random import randint, random
from database_requests import *
import random
 
#---------------------------------------------------------------------Definieren von Variablen zur Ausgabe von Phrasen---------------------------------------------------------------------
#Phrasen, die ausgegeben werden, wenn der Spieler zu niedrig geraten hat
low_phrases = [
    "Oh no, it's too low!",
    "That's lower than a snake's belly!",
    "Is that a limbo attempt? It's too low!",
    "Down in the valleys of numbers, that's where you are!",
    "Did you dig a hole for your guess? It's too low!",
    "Calling all spelunkers, your guess is too deep!",
    "Houston, we have a low guess!",
    "Is that your golf score? Because it's too low!",
    "Comon man, it's looow!",
    "Is your guess on vacation? It's too low!",
    "You're diving for treasure, but you need to go higher!",
    "Your guess is so low, it's doing the limbo!",
    "Is your guess practicing for limbo championships? Too low!",
    "Low guess alert! Someone get the low-guess alarm!",
    "The elevator of guesses isn't going up far enough! Your number is too low!",
    "Bring out the step stool, your guess needs a boost! Your number is too low!",
    "Low like a limbo master! Too low for the game.",
    "Your guess is so low, even ants are taller!",
    "When you're guessing low, you're aiming for the center of the Earth!",
    "Is that a worm's-eye view? Because your guess is low!",
    "Did you bring your hiking boots? Your guess is down in the valley!",
    "It's a low-guess party and your guess is the life of it!",
    "Your guess is in the basement of numbers. Try the upper floors!",
    "Is your guess doing the limbo dance? It's too low!",
    "You're aiming for gold, but your guess is in the bronze category! Your number is too low!",
    "Low like a submarine! But too low for this game.",
    "Your guess is so low, it's borrowing sugar from the Earth's core!",
    "Low altitude warning! Your guess needs more altitude!",
    "We've hit rock bottom! Well, your guess has, at least. Your number is too low!",
    "Your guess is sunbathing at the lowest point!",
    "Lowest of the low! Let's aim higher!",
    "Underground treasure? Maybe, but your guess is too low!",
    "Low guess spotted! Let's try for something higher.",
    "Your guess is in the bottom bunk of numbers.",
    "Your guess is so low, it's practically in the basement!",
    "Are you mining for diamonds? Your guess is too low!",
    "Your guess is playing hide and seek in the number basement!",
    "Calling all deep-sea divers! Your guess is too deep!",
    "Low like a limbo champion! But too low for the game.",
    "Your guess is exploring the depths of numberdom!",
    "Down, down, down your guess goes! Too low for the game.",
    "Low guess alert! Time to shoot for the stars instead!"
]

#Phrasen, die ausgegeben werden, wenn der Spieler richtig geraten hat
correct_phrases = [
    "You nailed it! Well done!",
    "Jackpot! That's the correct number!",
    "You're a mind reader! It's the right number!",
    "You're on fire! Your guess is spot on!",
    "Ding ding ding! Correct guess!",
    "Who's the number whisperer? You are!",
    "You've got it! That's the correct number!",
    "Bravo! Your guess is right on the money!"
]
#Phrasen, die ausgegeben werden, wenn der Spieler zu hoch geraten hat
high_phrases = [
    "You're aiming for the stars, but Your number is too high!",
    "Hitting the ceiling! It's too high.",
    "Is your guess skydiving? It's too high!",
    "You're in the upper stratosphere of numbers!",
    "Is your guess in an elevator? It's going too high!",
    "That's so high, it's touching the clouds!",
    "Higher than a giraffe's neck! Try something lower!",
    "Maybe your guess is on a rocket to space. Too high!",
    "Your guess is doing a skydiving stunt! Too high!",
    "Did you climb a mountain for that guess? It's too high!",
    "Did you send your guess to the moon? It's too high!",
    "The weather's fine up there, but its to high for your guess!",
    "High like a skyscraper! But too high for this game.",
    "You're reaching for the heavens with that guess!",
    "Your guess is at cruising altitude, but to high for this game!",
    "Did your guess go bungee jumping? It's too high!",
    "Your guess is hanging out with the birds. Too high!",
    "Is your guess in the cloud? It's too high!",
    "Flying high like a superhero! But too high for the game.",
    "That's one giant leap for a guess! But too high.",
    "High as a rocket ship! But too high for the game.",
    "Your guess is on a roller coaster to the moon. Try lower!",
    "Your guess is at the peak of Everest! But too high for the game.",
    "That guess is so high, it's waving to the International Space Station!",
    "Are you aiming for Mars? Your guess is too high!",
    "Your guess is doing a skydive from the top of the Eiffel Tower! Too high!",
    "High like a professional basketball player! But too high for the game.",
    "Your guess is in the upper deck of numbers. Bring it down!",
    "Up, up, and away! Your guess is flying too high.",
    "Is your guess at the top of Mount Everest? It's too high!",
    "Did your guess join a hot air balloon race? It's too high!",
    "Your guess is so high, it's seeing shooting stars!",
    "Is your guess taking an elevator to the moon? It's too high!",
    "High like a satellite! Try something lower!",
    "Your guess is so high, it's touching the edge of space!",
    "Sky's the limit, but not for your guess! Your number is too high!",
    "Is your guess doing a parachute jump from a plane? It's too high!",
    "Your guess is having a picnic on a mountaintop. Too high!",
    "That guess is on the rocket ship express! But too high for this game.",
    "Is your guess visiting the International Space Station? It's too high!",
    "Your guess is skydiving without a parachute! Too high!",
    "That's a stratospheric guess! But still too high.",
    "Your guess is at the top of the tallest building! But too high for this game.",
    "High as a hot air balloon! But not high enough for the game.",
    "Your guess is in the cockpit of a rocket ship. Too high!",
    "Up, up, and away! Your guess is soaring too high.",
    "Is your guess floating in the atmosphere? It's too high!",
]


#---------------------------------------------------------------------Ende Variablen-Definition---------------------------------------------------------------------


#---------------------------------------------Start der App per Flask---------------------------------------------
app = Flask(__name__, template_folder='templateFiles', static_folder='staticFiles')
app.secret_key = '300102'
@app.route('/')


#---------------------------------------------Start Definition der Routen---------------------------------------------
def index():
    return render_template('login.html')

@app.route('/welcomeScreen', methods=['GET', 'POST'])
def welcomeScreen():
    username = request.form.get('username', 0)
    password = request.form.get('password', 0)
    #if (CheckIfUserExists(username, password)):
    #    session['username'] = username
    #    print(session['username'])
    print(username)
    return render_template('welcomeScreen.html')

@app.route('/game', methods=['GET', 'POST'])
def game():
    fromUntilMessage = ""
    number_guess = ""
    response = ''
    number = ''
    counterMessage = ''

    if 'level' in request.args:
        level = request.args['level']
        if level == 'easy':
            min_range, max_range = 1, 100
        elif level == 'dev':
            min_range, max_range = 1, 1

        if 'counter' not in session:
            session['counter'] = 0

        if 'randomNumber' not in session: #or  number_guess == 0:
            session['randomNumber'] = randint(min_range, max_range)
            print(session['randomNumber'])
    
    if request.method == 'POST':
        user_guess = request.form.get('user_guess', 0)
        if user_guess == "0" or user_guess == "" or user_guess == None:
            number_guess = "You have not entered any number!"
        elif int(user_guess) > max_range or int(user_guess) < min_range:
            number_guess = "Your number is not in range!"
        elif int(user_guess) == session['randomNumber']:
            number_guess = random.choice(correct_phrases)
            number = session['randomNumber']
            session.pop('counter', None)
            session.pop('randomNumber', None)
            response = 'correct'
        elif int(user_guess) < session['randomNumber'] and int(user_guess) > min_range:
            number_guess = random.choice(low_phrases)
            session['counter'] += 1
        elif int(user_guess) > session['randomNumber'] and int(user_guess) < max_range:
            number_guess = random.choice(high_phrases)
            session['counter'] += 1

    fromUntilMessage = "Guess a number between " + str(min_range) + " and " + str(max_range) + "!"
    counterMessage = "Tries: " + str(session['counter'])

    return render_template('game.html', numberGuess=number_guess, fromUntilMessage=fromUntilMessage, counterMessage=counterMessage, response=response, number=number)


@app.route('/register', methods=['POST'])
def register():
    return render_template('register.html')  # Or redirect to another page

@app.route('/registerUserToDatabase', methods=['POST'])
def registerUserToDatabase():

    return render_template('game.html', numberGuess = 0)


if __name__ == '__main__':
    app.run(debug=True)
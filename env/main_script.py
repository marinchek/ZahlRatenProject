from flask import Flask, render_template, request, redirect, url_for, session
from random import randint, random
import random
 


low_phrases = [
    "Oh no, it's too low!",
    "That's lower than a snake's belly!",
    "Is that a limbo attempt? It's too low!",
    "Down in the valleys of numbers, that's where you are!",
    "Did you dig a hole for your guess? It's too low!",
    "Napoleon Dynamite would say, 'Lucky!'",
    "Calling all spelunkers, your guess is too deep!",
    "The floor is lava, but your guess is too low!",
    "Houston, we have a low guess!",
    "Is that your golf score? Because it's too low!",
    "Comon man, it's looow!",
    "To infinity and beyond... well, not quite with that guess!",
    "Is your guess on vacation? It's too low!",
    "You're diving for treasure, but you need to go deeper!",
    "Your guess is so low, it's doing the limbo!",
    "Is your guess practicing for limbo championships? Too low!",
    "Low guess alert! Someone get the low-guess alarm!",
    "The elevator of guesses isn't going down far enough!",
    "Bring out the step stool, your guess needs a boost!",
    "Low like a limbo master! But not low enough for the game.",
    "Your guess is so low, even ants are taller!",
    "When you're guessing low, you're aiming for the center of the Earth!",
    "Is that a worm's-eye view? Because your guess is low!",
    "Did you bring your hiking boots? Your guess is down in the valley!",
    "It's a low-guess party and your guess is the life of it!",
    "Your guess is in the basement of numbers. Try the upper floors!",
    "Is your guess doing the limbo dance? It's too low!",
    "You're aiming for gold, but your guess is in the bronze category!",
    "Low like a submarine! But not low enough for this game.",
    "Your guess is so low, it's borrowing sugar from the Earth's core!",
    "Low altitude warning! Your guess needs more altitude!",
    "We've hit rock bottom! Well, your guess has, at least.",
    "Your guess is sunbathing at the lowest point!",
    "Lowest of the low! Let's aim higher!",
    "Underground treasure? Maybe, but your guess is too low!",
    "Low guess spotted! Let's try for something higher.",
    "Your guess is in the bottom bunk of numbers.",
    "Your guess is so low, it's practically in the basement!",
    "Are you mining for diamonds? Your guess is too low!",
    "Your guess is playing hide and seek in the number basement!",
    "Calling all deep-sea divers! Your guess is too deep!",
    "Low like a limbo champion! But not low enough for the game.",
    "Your guess is exploring the depths of numberdom!",
    "Down, down, down your guess goes! Too low for the game.",
    "Low guess alert! Time to shoot for the stars instead!"
]
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
high_phrases = [
    "Whoa there, too high!",
    "You're aiming for the stars, but not quite that high!",
    "Hitting the ceiling! It's too high.",
    "Is your guess skydiving? It's too high!",
    "You're in the upper stratosphere of numbers!",
    "Is your guess in an elevator? It's going too high!",
    "High as a kite! But not high enough for the game.",
    "That's so high, it's touching the clouds!",
    "Higher than a giraffe's neck! But still not right.",
    "Maybe your guess is on a rocket to space. Too high!",
    "The sky's the limit, but not that high!",
    "Your guess is doing a skydiving stunt! Too high!",
    "Did you climb a mountain for that guess? It's too high!",
    "Did you send your guess to the moon? It's too high!",
    "Your guess is so high, it's getting a nosebleed!",
    "The weather's fine up there, but not for your guess!",
    "High like a skyscraper! But not high enough for this game.",
    "You're reaching for the heavens with that guess!",
    "Your guess is at cruising altitude, but not for this game!",
    "Did your guess go bungee jumping? It's too high!",
    "High five for trying! But your guess is too high.",
    "Your guess is hanging out with the birds. Too high!",
    "Is your guess in the cloud? It's too high!",
    "Flying high like a superhero! But not high enough.",
    "Your guess is so high, it's sending postcards!",
    "Is your guess skydiving without a parachute? Too high!",
    "That's one giant leap for a guess! But still too high.",
    "High as a rocket ship! But not high enough for the game.",
    "Your guess is on a roller coaster to the moon. Too high!",
    "Your guess is at the peak of Everest! But not for the game.",
    "That guess is so high, it's waving to the International Space Station!",
    "Are you aiming for Mars? Your guess is too high!",
    "Your guess is doing a skydive from the top of the Eiffel Tower! Too high!",
    "High like a professional basketball player! But not high enough for the game.",
    "Your guess is in the upper deck of numbers. Bring it down!",
    "Up, up, and away! Your guess is flying too high.",
    "Is your guess at the top of Mount Everest? It's too high!",
    "Did your guess join a hot air balloon race? It's too high!",
    "Your guess is so high, it's seeing shooting stars!",
    "Is your guess taking an elevator to the moon? It's too high!",
    "High like a satellite! But not high enough for the game.",
    "Your guess is so high, it's touching the edge of space!",
    "Sky's the limit, but not for your guess!",
    "Is your guess doing a parachute jump from a plane? It's too high!",
    "Your guess is having a picnic on a mountaintop. Too high!",
    "That guess is on the rocket ship express! But too high for this game.",
    "Is your guess visiting the International Space Station? It's too high!",
    "Your guess is skydiving without a parachute! Too high!",
    "That's a stratospheric guess! But still too high.",
    "Your guess is at the top of the tallest building! But not for this game.",
    "High as a hot air balloon! But not high enough for the game.",
    "Your guess is in the cockpit of a rocket ship. Too high!",
    "Up, up, and away! Your guess is soaring too high.",
    "Is your guess floating in the atmosphere? It's too high!",
]

app = Flask(__name__, template_folder='templateFiles', static_folder='staticFiles')
app.secret_key = '300102'
@app.route('/')
def index():
    return render_template('login.html')

@app.route('/welcomeScreen', methods=['POST'])
def welcomeScreen():
    return render_template('welcomeScreen.html')

@app.route('/game', methods=['GET', 'POST'])
def game():
    fromUntilMessage = ""
    number_guess = ""

    if 'level' in request.args:
        level = request.args['level']
        if level == 'easy':
            min_range, max_range = 1, 50
        elif level == 'medium':
            min_range, max_range = 1, 500
        elif level == 'hard':
            min_range, max_range = 1, 1000
        else:
            # Default to medium level if level is not recognized
            min_range, max_range = 1, 500
        
        fromUntilMessage = "Guess a number between " + str(min_range) + " and " + str(max_range) + "!"    

        if 'randomNumber' not in session or  number_guess == 0:
            session['randomNumber'] = randint(min_range, max_range)
            print(session['randomNumber'])
    
    if request.method == 'POST':
        user_guess = int(request.form.get('user_guess', 0))
        if user_guess == 0 or user_guess == "0" or user_guess == "" or user_guess == None:
            number_guess = "You have not entered any number!"
        elif user_guess == session['randomNumber']:
            number_guess = random.choice(correct_phrases)
            session.pop('randomNumber', None)
        elif user_guess < session['randomNumber']:
            number_guess = random.choice(low_phrases)
        elif user_guess > session['randomNumber']:
            number_guess = random.choice(high_phrases)
    
    return render_template('game.html', numberGuess=number_guess, fromUntilMessage=fromUntilMessage)


@app.route('/register', methods=['POST'])
def register():

    return render_template('register.html')  # Or redirect to another page

@app.route('/registerUserToDatabase', methods=['POST'])
def registerUserToDatabase():

    return render_template('game.html', numberGuess = 0)


if __name__ == '__main__':
    app.run(debug=True)
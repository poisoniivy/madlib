"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]

PEOPLE = [
    "Abe Lincoln", "Lady Gaga", "Prince", "Steve Jobs", "Homer",
]

COLORS = [
    "green", "purple", "orange", "yellow",
]

THINGS = [
    "iPhone", "pants", "snowboard", "cup"
]

PLACES = [
    "London", "Paris", "Mars", "San Francisco",
]

FOODS = [
    "Pizza", "Hot Dogs", "Jello",
]

@app.route('/')
def start_here():
    """Display homepage."""

    return """
    Hi! This is the home page.
    <a href="/hello">Click here!</a>
    """


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)


@app.route('/game')
def show_madlib_form():
    """Madlibs game."""
    response = request.args.get("decision")

    if response == "no":
        return render_template("goodbye.html")
    else:
        return render_template("game.html", adjectives=AWESOMENESS, 
            people=PEOPLE, colors=COLORS, nouns=THINGS,
            places=PLACES, foods=FOODS)

@app.route('/madlib')
def show_madlib():
    name = request.args.get("name")
    color = request.args.get("color")
    noun = request.args.get("noun")
    adjective = request.args.get("adjective")
    place = request.args.get("place")
    # pizza = request.args.get("Pizza")
    # hotdog = request.args.get("Hot Dogs")
    # jello = request.args.get("Jello")
    food_list = request.args.getlist("food")
    # print pizza, hotdog, jello
    print food_list


    return render_template("madlib.html", person=name, color=color, noun=noun,
        adjective=adjective, place=place, foods=food_list)

if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)

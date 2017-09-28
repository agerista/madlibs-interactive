"""A madlib game that compliments its users."""

from random import choice
from flask import (Flask, render_template, request, session)
from madlibs_scripts import (get_input_fields, madlibs_scripts)

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)
app.secret_key = "super323SEC109RET87pa22ss5wor33dKe1y"


AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    print "hello!"

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    print "hello!"

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)


@app.route('/game', methods=['GET'])
def play_madlibs():
    """Madlibs Game"""

    text = madlibs_scripts()
    game = get_input_fields(text)

    session['play'] = game
    session['core'] = text

    return render_template("game.html", game=game)


@app.route('/results', methods=['POST'])
def madlibs_results():
    """Funny results ensue"""

    game = session['play']
    text = session['core']

    title = text[0]
    script = text[1].strip().split()
    fields = {}
    i = 0

    for key, value in game.iteritems():
        fields[key] = key
        fields[key] = []

        for item in range(0, value):
            num = str(item + 1)
            field = request.form.get(key + "-" + num)
            fields[key].append(field)

    print fields

    for word in script:

        if fields.get(word, 0) != 0:
            temp = fields[word][0]
            script[i] = temp.encode("utf-8")

            try:
                fields[word] = fields[word][1:]

            except KeyError:
                "No key found"

        # any word with a coma or a period will not get replaced unless we remove the last character
        # TODO: still having an isue with punctuation here
        elif fields.get(word[:-1], 0) != 0:
            temp = fields[word[:-1]][0] + word[-1]
            script[i] = temp.encode("utf-8")

            try:
                fields[word] = fields[word[:-1]][1:]

            except KeyError:
                "No key found"

        i += 1

    script = " ".join(script)

    return render_template("results.html", game=game, script=script, title=title)

###############################################################################################
if __name__ == "__main__":

    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = False
    # make sure templates, etc. are not cached in debug mode
    app.jinja_env.auto_reload = app.debug

    app.run(port=5000, host='0.0.0.0')

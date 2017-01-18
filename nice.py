from random import choice

from flask import Flask, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

INSULTS = [
    'a jerk', 'annoying', 'generally terrible', 'an asshole', 'inadequate', 'illogical']


@app.route('/')
def start_here():
    """Home page."""

    return """<!doctype html><html>
    Hi! This is the home page.<br>
    <a href="/hello">Hello page</a>
    <html>"""


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    compliment_text = ""
    for i in range(len(AWESOMENESS)):
      compliment_text += """<label>{1}<input type="radio" name="{0}" value="{1}"></label>""".format("compliment", AWESOMENESS[i])

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>You now have all the example code you need to make your own route that will dish out insults instead. Make another route called /diss that dishes out one of several insults. Set up a separate form in the HTML returned from /hello that goes to /diss.


        <form action="/greet">
          <label>What's your name? <input type="text" name="person"></label>
          <input type="submit">""" + compliment_text + """
          </input>
        </form>
        Don't want a compliment?! Fill out this form instead:

        <form action="/diss">
          <label>What's your name? <input type="text" name="person"></label>
          <input type="submit">
          </input>
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    # compliment = choice(AWESOMENESS)
    compliment = request.args.get("compliment")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi %s I think you're %s!
      </body>
    </html>
    """ % (player, compliment)

@app.route('/diss')
def disssss():
    insult = choice(INSULTS)
    player = request.args.get('person')
    return """
    <!doctype html>
    <html>
      <head>
        <title>A Diss</title>
      </head>
      <body>
        Hi %s!  No offense, but I think you're %s.
      </body>
    </html>
    """ %(player, insult)



if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)

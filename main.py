from flask import Flask, request

from caesar import encrypt_string

app = Flask(__name__)
app.config['DEBUG'] = True

header = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>Web Caesar</title>
    </head>
    <body>
'''

footer = '''
    </body>
</html>
'''

form = '''
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <!-- create your form here -->

      <form action"/" method="POST">
        <label for="rot">Rotate By: </label>
        <input type="text" name="rot" value="0" />
        <textarea name="text">{0}</textarea>
        <input type="submit" value="Rotate" />
      </form>

    </body>
</html>
'''
@app.route("/", methods=['POST'])
def encrypt():
    rot_amt = int(request.form['rot'])
    phrase = str(request.form['text'])

    new_phrase = encrypt_string(phrase, rot_amt)

    return form.format(new_phrase)

@app.route("/")
def index():
    empty_message = ""
    return form.format(empty_message)

app.run()

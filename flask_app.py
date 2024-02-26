from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<p>Dit is Les 11 - Opdr. 6!</p>'

if __name__ == '__main__':
    app.run()

#Opdr 4. Na uitvoeren van command: "git checkout -b main" krijg ik het volgende terug: "Switched to a new branch 'main'".
#Dit betekent dat we een nieuwe branch hebben aangemaakt met de modifier "-b".
#Met "checkout" schakel je over naar de zojuist aangemaakte branch.
#main is de naam van de branch die we net hebben aangemaakt.
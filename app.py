from flask import Flask, render_template, request
from src.spellChecker import SpellChecker

spellchecker = SpellChecker()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.get_json()
        word = data['word']

        suggestions = spellchecker.spell_check(word, 10)
        print(word, suggestions)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

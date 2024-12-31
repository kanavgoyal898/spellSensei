from flask import Flask, render_template, request, jsonify
from src.spellChecker import SpellChecker

spellchecker = SpellChecker()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    suggestions = []
    if request.method == 'POST':
        data = request.get_json()
        word = data['word']
        suggestions = spellchecker.spell_check(word, 5)
        return jsonify(suggestions=suggestions)
    return render_template('index.html', suggestions=suggestions)

if __name__ == '__main__':
    app.run(debug=True)

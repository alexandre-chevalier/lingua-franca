from flask import *
from deeplClass import DeeplClass

app = Flask(__name__)
deepl_trans = DeeplClass()

@app.route("/")
def main_page():
    retrieve_lang = deepl_trans.retrieve_language()
    return render_template("main.html", language = retrieve_lang)

@app.route("/traitement", methods=['POST'])
def traitement_requetes():
    text = request.form.get('texte')
    lang = request.form.get('lang')
    if lang == "EN":
        lang = "EN-GB"
    translate_language = deepl_trans.translate_language(text, lang)
    return jsonify({"message": translate_language})

if __name__ == '__main__':
    app.run(debug=True)
from flask import *
from deeplClass import DeeplClass

app = Flask(__name__)
deepl_trans = DeeplClass()

@app.route("/")
def main_page():
    retrieve_lang = deepl_trans.retrieve_language()
    return render_template("main.html", language = retrieve_lang)

if __name__ == '__main__':
    app.run(debug=True)
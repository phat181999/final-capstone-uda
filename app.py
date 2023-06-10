from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    html = "<h1>HELLO WORLD I'M HO TAN PHAT FROM VIET NAM</h1>"
    return html.format(format)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
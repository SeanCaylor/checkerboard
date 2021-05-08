from flask import Flask, render_template
app = Flask(__name__)

@app.errorhandler(404)
def error(e):
    return "I'm afraid I can't let you do that, Star Fox"

@app.route('/')
@app.route('/<int:width>')
@app.route('/<int:width>/<int:length>')
@app.route('/<int:width>/<int:length>/<string:color1>')
@app.route('/<int:width>/<int:length>/<string:color1>/<string:color2>')
def homepage(width = 8, length = 8, color1 = "crimson", color2 = "black"):
    return render_template('index.html', width = width, length = length, color1 = color1, color2 = color2)

if __name__ == "__main__":
    app.run(debug = True)
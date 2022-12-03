from flask import Flask, render_template
app = Flask(__name__)


@app.route('/play')
def threeboxes():
    return render_template("index.html", color = "blue", number=3)

@app.route('/play/<int:kevinnum>')
def number(kevinnum):
    return render_template("index.html", color = "blue", number = kevinnum)

@app.route('/play/<int:pynum>/<pycolor>')
def number_color(pycolor, pynum):
    return render_template("index.html", color = pycolor, number = pynum)





if __name__=="__main__":
    app.run(debug=True)


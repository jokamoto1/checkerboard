from flask import Flask
from flask.templating import render_template

app = Flask(__name__)
@app.route('/')
def checkerboard():
    return render_template('index.html', row = 8 , col = 8, color1 = "green", color2 = "black")
@app.route('/<int:row>/<int:col>')
def checkerboard1(row, col):
    return render_template('index.html',row = row, col = col, color1 = "green", color2 = "black")
@app.route('/<int:row>/<int:col>/<string:color1>/<string:color2>')
def checkerboard2(row, col, color1, color2):
    return render_template('index.html',row = row, col = col, color1 = color1, color2 = color2 )
if __name__=="__main__":   
    app.run(debug=True) 
    
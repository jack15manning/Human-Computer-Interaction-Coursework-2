from flask import Flask, render_template
from flask import request
from wtforms import Form, SelectField, validators
app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def home(): 
    return render_template('Dashboard.html')
    
@app.route('/news', methods=['GET','POST'])
def news():
    return render_template('News.html')

@app.route('/search', methods=['GET','POST'])
def search():
    return render_template('Search.html')
    
@app.route('/article', methods=['GET','POST'])
def article():
    return render_template('Article.html')
    
@app.route('/systems', methods=['GET','POST'])
def systems():
    return render_template('Systems.html')
    
@app.route('/faculties', methods=['GET','POST'])
def faculties():
    return render_template('Faculties.html') 
if __name__ == '__main__':
    app.run(debug = True)

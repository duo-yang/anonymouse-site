from flask import Flask, render_template, request,redirect
from flask_talisman import Talisman
import os


app = Flask(__name__)
if(os.environ['FLASK_ENV']!="development"): Talisman(app)

@app.route('/', methods=['GET', 'POST'])
def home():
	return render_template('index.html')

@app.route('/about/', methods=['GET', 'POST'])
def about():
	return render_template('aboutpage.html')
@app.route('/news/',methods=['GET'])
def news():
	return render_template('news.html')
@app.route('/staff/',methods=['GET','POST'])
def staff():
	return render_template('staff.html')


if __name__ == '__main__':
	app.run()

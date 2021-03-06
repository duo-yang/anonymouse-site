from flask import Flask, render_template, request,redirect
from flask_talisman import Talisman,GOOGLE_CSP_POLICY
import os

app = Flask(__name__)
csp={'default-src':['\'self\'','https://*']}
try:
	if(os.environ['FLASK_ENV']!="development"): 
		#print("prouction")
		Talisman(app,content_security_policy=csp)
	#else: 
		#print("development encountered")
except:
	#print("could not get flask_env")
	Talisman(app,content_security_policy=csp)

@app.route('/', methods=['GET'])
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
@app.route('/downloads/',methods=['GET','POST'])
def downloads():
	return render_template('download.html')


if __name__ == '__main__':
	app.run()

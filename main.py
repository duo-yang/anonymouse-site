from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
	return render_template('index.html')

@app.route('/about/', methods=['GET', 'POST'])
def about():
	return render_template('aboutpage.html')
@app.route('/news/',methods=['GET'])
def news():
	return render_template('news.html')


if __name__ == '__main__':
	app.run()

from flask import render_template, request, send_from_directory
from snabbafakta import app, db
from snabbafakta.models import Question

@app.route('/')
def index():
	questions = question = Question.query.all()
	context = {'questions': questions}
	return render_template('index.html', **context)

@app.route('/fragor/<slug>')
def question(slug):
	question = Question.query.filter_by(slug=slug).first()
	context = {'question': question}
	return render_template('question.html', **context)

@app.route('/om')
def about():
	return render_template('about.html')

@app.route('/foresla', methods=['GET', 'POST'])
def suggest():
	if request.method == 'POST':
		pass
	else:
		return render_template('suggest.html')

@app.route('/img/<name>')
def img(name):
	return send_from_directory(app.config['IMG_DIR'], name)
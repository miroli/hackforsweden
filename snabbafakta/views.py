from flask import render_template
from snabbafakta import app, db
from snabbafakta.models import Question

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/fragor/<slug>')
def question(slug):
	question = Question.query.filter_by(slug=slug).first()
	context = {'question': question}
	return render_template('question.html', **context)
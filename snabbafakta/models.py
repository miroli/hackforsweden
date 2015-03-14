from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Question(db.Model):
	__tablename__ = 'question'

	id = db.Column(db.Integer, primary_key=True)
	slug = db.Column(db.String())
	question = db.Column(db.String())
	text = db.Column(db.String())
	iframe = db.Column(db.String())
	source = db.Column(db.String())

	def __init__(self, slug, question, text, iframe, source):
		self.slug = slug
		self.question = question
		self.text = text
		self.iframe = iframe
		self.source = source

	def __repr__(self):
		return '<question: {}>'.format(self.question)

class Suggestion(db.Model):
	__tablename__ = 'suggestion'

	id = db.Column(db.Integer, primary_key=True)
	question = db.Column(db.String())
	sender = db.Column(db.String())

	def __init__(self, question, text, sender):
		self.question = question
		self.text = text
		self.sender = sender

	def __repr__(self):
		return '<question: {}>'.format(self.question)
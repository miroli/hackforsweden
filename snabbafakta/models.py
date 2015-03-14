from snabbafakta import db
# from sqlalchemy.dialects.postgresql import JSON

class Question(db.Model):
	__tablename__ = 'question'

	id = db.Column(db.Integer, primary_key=True)
	slug = db.Column(db.String())
	question = db.Column(db.String())
	source = db.Column(db.String())

	def __init__(self, slug, question, source):
		self.slug = slug
		self.question = question
		self.source = source

	def __repr__(self):
		return '<question {}>'.format(self.question)
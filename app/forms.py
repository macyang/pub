from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, IntegerField
from wtforms.validators import DataRequired, NumberRange

class SimplePlotForm(Form):
    input0 = StringField('input0', validators=[DataRequired()])
    n = IntegerField('n', validators=[NumberRange(min=1, max=250)])

class CatNForm(Form):
    input0 = StringField('input0', validators=[DataRequired()])
    n = IntegerField('n', validators=[NumberRange(min=1, max=250)])

class KmeansForm(Form):
    inputFile = StringField('inputFile', validators=[DataRequired()])
    numClusters = IntegerField('numClusters', validators=[NumberRange(min=2, max=10)])
    numIterations = IntegerField('Iterations', validators=[NumberRange(min=2, max=20)])

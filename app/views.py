from flask import render_template, flash, redirect
from app import app
from .forms import KmeansForm, SimplePlotForm, CatNForm
from .guru import runKmeans, runCatN, getContexts, getJobs
import json
import requests

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'guru'}
    return render_template('index.html',
                           title='GURU',
                           user=user)

@app.route('/app/kmeans', methods=['GET', 'POST'])
def kmeans():
    form = KmeansForm()
    if form.validate_on_submit():
      form.result = runKmeans(form.inputFile,
			      form.numClusters,
			      form.numIterations)
      resp = form.result
      return render_template('kmeans.html', 
                           title='Cluster Analysis : K-means',
                           form=form, resp=resp)
    return render_template('kmeans.html', 
                           title='Cluster Analysis : K-means',
                           form=form)

@app.route('/app/simpleplot', methods=['GET', 'POST'])
def simpleplot():
    form = SimplePlotForm()
    if form.validate_on_submit():
      form.result = runCatN(form.input0, form.n)
      resp = form.result
      return render_template('simpleplot.html', 
                           title='Simple Plot',
                           form=form, resp=resp)
    return render_template('simpleplot.html', 
                           title='Simple Plot',
                           form=form)

@app.route('/sys/contexts', methods=['GET'])
def contexts():
    resp = getContexts()
    return render_template('contexts.html', 
                           title='Context List',
                           data=resp)

@app.route('/sys/jobs', methods=['GET'])
def jobs():
    resp = getJobs()
    return render_template('jobs.html', 
                           title='Context List',
                           data=resp)

@app.route('/build', methods=['GET', 'POST'])
def build():
    return render_template('build.html')

@app.route('/test', methods=['GET', 'POST'])
def test():
    return render_template('test.html')

from flask import render_template, flash, request
from app import app
import numpy as np
import cStringIO
import matplotlib.pyplot as plt
import json
import requests
import time

@app.route('/_plot')
def build_plot():

  jobAPI = 'http://localhost:8090/jobs'
  jobId = request.args.get('jobid')
  r = requests.get(jobAPI + '/' + jobId)
  resp = json.loads(r.text)
  # print "XXX plots: ", r.text
  data_list = resp['result']['data']
  xlist = []
  ylist = []
  for dS in data_list:
    d = json.loads(dS)
    xlist.append(d[0])
    ylist.append(d[1])

  # print "XXX xlist: ", xlist
  # print "XXX ylist: ", ylist
  # Generate the plot
  line, = plt.plot(xlist, ylist, marker='o', color='r', ls='')

  f = cStringIO.StringIO()
  plt.savefig(f, format='png')

  # Serve up the data
  header = {'Content-type': 'image/png'}
  f.seek(0)
  data = f.read()

  return data, 200, header

@app.route('/plot', methods=['GET', 'POST'])
def test_plot():

  # Generate the plot
  x = np.linspace(0, 10)
  line, = plt.plot(x, np.sin(x))

  f = cStringIO.StringIO()
  plt.savefig(f, format='png')

  # Serve up the data
  header = {'Content-type': 'image/png'}
  f.seek(0)
  data = f.read()

  return data, 200, header

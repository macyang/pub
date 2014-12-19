import json
import requests
import time

contextAPI = 'http://localhost:8090/contexts'
jobAPI = 'http://localhost:8090/jobs'

def runCatN(input0, n):
  conf = "CatN{"
  conf += "input0=\"tap:nrdd0\","
  conf += "n=" + str(n.data) + "}"
  print "XXX CatN config: ", conf
  job = jobAPI + '?appName=tap&classPath=tap.engine.CatN&context=tap-context'
  r = requests.post(job, data = conf)
  resp = json.loads(r.text)
  return resp['result']['jobId']

def runKmeans(inputFile, numClusters, numIterations):
  # create the context
  r = requests.post(contextAPI + "/tap-context?num-cpu-cores=4&mem-per-node=512m")

  conf = "FileReader{"
  conf += "inputFile=\"hdfs://hadoop-m/tmp/" + inputFile.data + "\","
  conf += "format=\"CSV\","
  conf += "output0=\"tap:nrdd0\"}"
  # print "XXX filereader config: ", conf
  job = jobAPI + '?appName=tap&classPath=tap.engine.FileReader&context=tap-context&sync=true'
  r = requests.post(job, data = conf)
  resp = json.loads(r.text)
  status = resp['status']
  if (status != 'OK'):
    return r.text

  conf = "ClusterAnalysis{"
  conf += "input0=\"tap:nrdd0\","
  conf += "method=\"KMeans\","
  conf += "numClusters=" + str(numClusters.data) + ","
  conf += "numIterations=" + str(numIterations.data) + "}"
  # print "XXX kmeans config: ", conf
  job = jobAPI + '?appName=tap&classPath=tap.engine.ClusterAnalysis&context=tap-context&sync=true'
  r = requests.post(job, data = conf)
  resp = json.loads(r.text)
  return resp['result']


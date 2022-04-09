import plotly.express as px
import numpy
import csv
def plotFigure(data_path):
  with open(data_path) as csvfile:
    df = csv.DictReader(csvfile)
    fig = px.scatter(df, x='Marks In Percentage', y='Days Present', color="Roll No")
    fig.show()

def getDataSource(data_path):
  temp=[]
  icecreamsales=[]
  with open(data_path) as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
      temp.append(float(row["Marks In Percentage"]))
      icecreamsales.append(float(row["Days Present"]))
  return{"x": temp, "y": icecreamsales} 

def findCorrelation(data_source):
  correlation = numpy.corrcoef(data_source["x"], data_source["y"])
  print('Correlation is ',correlation[0, 1])

datapath = './content/Student Marks vs Days Present.csv'
dataSource = getDataSource(datapath)
findCorrelation(dataSource)
plotFigure(datapath)
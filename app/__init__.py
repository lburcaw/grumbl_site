from flask import Flask
app = Flask(__name__)
from app import views

#from sklearn.externals import joblib

#global clf
#clf = joblib.load('/Users/lauren/Documents/insight_project/model/rf_4feat.pkl')
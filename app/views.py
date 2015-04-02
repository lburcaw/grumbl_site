from flask import render_template, request, make_response
from app import app
import pymysql as mdb
import get_latlong_goog as ll
import matplotlib
matplotlib.use('AGG')
from sklearn.externals import joblib
import numpy as np
from datetime import datetime, date 
#import seaborn as sns
import plot_horizbar as phb
import plot_monthprob_interp as pmp


@app.route('/')
@app.route('/index')
def index():
  return render_template("input.html",title = "Input")

@app.route('/output')
def grumbl_output():
  #pull 'ID' from input field and store it
  addy = request.args.get('ID')
  # Get Lat/Long from address
  f = ll.googleGeocoding(addy)
  latlong = ll.getGeocodeLatLong(f)
  lat = latlong['lat']
  lon = latlong['lng']

  # round to nearest thousandth
  lat_rnd = np.round(lat,3)
  lon_rnd = np.round(lon,3)

  # Make sure it's in Queens!
  if lat_rnd < 40.555 or lat_rnd > 40.800 or lon_rnd < -73.961 or lon_rnd > -73.701:
      return render_template("error_queens.html")
  
  # Get month info 
  date = request.args.get('date')
  try:
      datetime.strptime(date, "%B")
  except ValueError:
      return render_template("error_date.html")

  mo_str = datetime.strptime(date, '%B')
  month = int(mo_str.strftime('%m'))

  db= mdb.connect(user="root", host="localhost", db="insight_project", charset='utf8')
  
  # Query database
  with db:
    cur = db.cursor()
    cur.execute('''SELECT prob_blg, prob_nz, prob_st, prob_vm, month 
                 FROM demo_probs WHERE latitude = '%f' AND longitude = '%f';''' %(lat_rnd,lon_rnd))
    local = cur.fetchall()
  local_arr = np.array(local)
  
  with db:
    cur = db.cursor()
    cur.execute("SELECT * FROM quantiles WHERE month = '%d';" %(month))
    quantiles = np.array(cur.fetchall()).astype(float).flatten()
  quantiles = quantiles[:-1]

  db.close()

  
  labels = ('Building','Noise','Street','Vermin')
 
  month_result = local_arr[local_arr[:,4]==month][:,:4].flatten().astype(float)

  # Get quantiles to figure out low/avg/high
  low = np.less_equal(month_result,quantiles[:4])
  hi = np.greater_equal(month_result,quantiles[8:12])
  rankval = np.ones(4,)+(-1*low)+hi
  rankdict = {0: 'Low',1: 'Average', 2: 'High'}
  rank = [rankdict[x] for x in rankval]

  perc = np.round(month_result*100).astype(int)
  max_label = labels[np.argmax(perc)]
  max_perc = max(perc)
  
  # Plot figures
  hbar_name=phb.plot_hbar(labels,perc,date)
  monthprob_name = pmp.interp_probs(local_arr[:,:4].astype(float))
  
  return render_template("output.html", monthprob_name = monthprob_name,
   hbar_name = hbar_name, rank = rank, probs=perc, addy = addy, date = date, max_label=max_label.lower(),max_perc=max_perc)

@app.route('/mapimages/<path:filename>')

def return_image(filename):
    response = make_response(app.send_static_file(filename))
    response.cache_control.max_age = 0
    return response

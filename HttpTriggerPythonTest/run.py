import sys, os, calendar, json
from datetime import datetime, timedelta
import os
import argparse

postreqdata = json.loads(open(os.environ['req']).read())
response = open(os.environ['res'], 'w')
data = {
   'name' : postreqdata['name'],
   'dash' : postreqdata['dash'],
   'price' : 542.24
}

json_str = json.dumps(data)
response.write(json_str)
response.close()

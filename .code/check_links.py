import os

import yaml
import requests

for file_name in os.listdir('.'):

    if file_name.endswith( '.yaml' ):

        with open( file_name , 'r') as file:
            data = yaml.safe_load(file)

        for entry in data:
            del entry['name'] ## remove name data
            for source in entry.values():
                r = requests.get( source )
                if not 200 <= int( r.status_code ) <= 229:
                    raise Exception("Source ", source, " failed")

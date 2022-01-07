import os
import json

import yaml
import pandas as pd

try:
 os.mkdir('./dist/')
except:
 pass

for file_name in os.listdir('.'):

    if file_name.endswith( '.yaml' ):

        with open( file_name , 'r') as file:
            data = yaml.safe_load(file)

        data = pd.DataFrame.from_dict( data )

        data.to_json( './dist/' + file_name.replace('.yaml', '.json'), orient = 'records' ) ## this leads to ugly escaped jsons, workaround
        ## json.dump( data.values.tolist() , open(  './dist/' + file_name.replace('.yaml', '.json'), 'w') )
        data.to_csv( './dist/' + file_name.replace('.yaml', '.csv'), index = False )

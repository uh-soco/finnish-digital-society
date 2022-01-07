import os
import json

import yaml
import pandas as pd

for file_name in os.listdir('.'):

    if file_name.endswith( '.yaml' ):

        with open( file_name , 'r') as file:
            data = yaml.safe_load(file)

        data = pd.DataFrame.from_dict( data )

        ##data.to_json( file_name.replace('.yaml', '.json'), orient = 'records' ) ## this leads to ugly escaped jsons, workaround
        json.dump( data.values.tolist() , open( file_name.replace('.yaml', '.json'), 'w') )
        data.to_csv( file_name.replace('.yaml', '.csv'), index = False )

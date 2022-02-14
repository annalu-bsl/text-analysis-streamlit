'''

Code that import the json data from the s3 bucket. The source is from Amazon's open data project with reviews from the
products ans its coefficients of helpfulness
https://registry.opendata.aws/helpful-sentences-from-reviews/

'''

import json
import streamlit as st
import pandas as pd
import boto3
import io
import os
import json

#name of the bucket
bucket_name = 'helpful-sentences-from-reviews'

#names of the json files in the bucket
Keys = ['train.json', 'test.json']

@st.cache(persist = True)
def get_data():
    s3 = boto3.client('s3',
                    aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID'),
                    aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
                    )

    d = {}
    for key in Keys:
        obj = s3.get_object(Bucket = bucket_name, Key = key)
        #getting name of the dataframe
        key_name = key.split('.json')[0]
        #creating dictionary of dataframes
        d[key_name] = pd.read_json(obj['Body'], lines = True)
    return d
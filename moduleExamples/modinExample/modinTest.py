import ray
import time

import pandas
import os

os.environ["MODIN_ENGINE"] = "ray"  # Modin will use Ray
# os.environ["MODIN_ENGINE"] = "dask"
ray.init(num_cpus=4)
import modin.pandas as pd

import numpy as np

#import urllib.request
#s3_path = "https://modin-test.s3.us-west-1.amazonaws.com/yellow_tripdata_2015-01.csv"
#urllib.request.urlretrieve(s3_path, "taxi.csv")

# 1

start = time.time()
pandas_df = pd.read_csv("taxi.csv", quoting=3)
df = pd.concat([pandas_df]*5)
df['trip_distance'].apply(lambda x: x*20)
end = time.time()
pandas_duration = end - start
print("modin Time to read with pandas: {} seconds".format(round(pandas_duration, 3)))

# 2
start = time.time()
pandas_df_A = pandas.read_csv("taxi.csv", quoting=3)
df_A = pandas.concat([pandas_df_A]*5)
df_A['trip_distance'].apply(lambda x: x*20)
end = time.time()
pandas_duration = end - start
print("pandas Time to read with pandas: {} seconds".format(round(pandas_duration, 3)))
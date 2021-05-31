import pandas as pd
from pandas import read_csv
import geopandas as gpd
from geopandas import GeoDataFrame
from shapely.geometry import Point, LineString, shape
from glob import glob

file_names = glob(r'F:\Quadrant_Sin_comprimir\02\part-0000*.csv')
list = []
for file_name in file_names:
    df = read_csv(file_name, names = ['Device_ID', 'Lat', 'Lon', 'GPS_Accu', 'Timestamp', 'IP', 'OS_ID', 'OS', 'Country', 'Quad_ID', 'Publisher'], low_memory=False)
    list.append(df)
frame = pd.concat(list, axis=0, ignore_index=True)
df = frame[frame['Country'] == 'MX']
df['Timestamp1'] = df['Timestamp'].astype(str)
df['Timestamp1'] = df['Timestamp1'].str[:10]
df['Timestamp1'] = pd.to_datetime(df['Timestamp1'], unit='s')
df['Timestamp2'] = df['Timestamp1'].values.astype('datetime64[D]')

#Lo queremos en formato str
df['Timestamp2'] = df['Timestamp1'].astype(str)
df['Timestamp2'] = df['Timestamp2'].str[:10]
df['AvantiID'] = df['Device_ID'] + df['Timestamp2']
df.to_csv(r'F:\Quadrant_prueba\parte_0000_todaslaspartes.csv')

file_names = glob(r'F:\Quadrant_Sin_comprimir\02\part-0001*.csv')
list = []
for file_name in file_names:
    df = read_csv(file_name, names = ['Device_ID', 'Lat', 'Lon', 'GPS_Accu', 'Timestamp', 'IP', 'OS_ID', 'OS', 'Country', 'Quad_ID', 'Publisher'], low_memory=False)
    list.append(df)
frame = pd.concat(list, axis=0, ignore_index=True)
df = frame[frame['Country'] == 'MX']
df['Timestamp1'] = df['Timestamp'].astype(str)
df['Timestamp1'] = df['Timestamp1'].str[:10]
df['Timestamp1'] = pd.to_datetime(df['Timestamp1'], unit='s')
df['Timestamp2'] = df['Timestamp1'].values.astype('datetime64[D]')

#Lo queremos en formato str
df['Timestamp2'] = df['Timestamp1'].astype(str)
df['Timestamp2'] = df['Timestamp2'].str[:10]
df['AvantiID'] = df['Device_ID'] + df['Timestamp2']
df.to_csv(r'F:\Quadrant_prueba\parte_0001_todaslaspartes.csv')

file_names = glob(r'F:\Quadrant_Sin_comprimir\02\part-0002*.csv')
list = []
for file_name in file_names:
    df = read_csv(file_name, names = ['Device_ID', 'Lat', 'Lon', 'GPS_Accu', 'Timestamp', 'IP', 'OS_ID', 'OS', 'Country', 'Quad_ID', 'Publisher'], low_memory=False)
    list.append(df)
frame = pd.concat(list, axis=0, ignore_index=True)
df = frame[frame['Country'] == 'MX']
df['Timestamp1'] = df['Timestamp'].astype(str)
df['Timestamp1'] = df['Timestamp1'].str[:10]
df['Timestamp1'] = pd.to_datetime(df['Timestamp1'], unit='s')
df['Timestamp2'] = df['Timestamp1'].values.astype('datetime64[D]')

#Lo queremos en formato str
df['Timestamp2'] = df['Timestamp1'].astype(str)
df['Timestamp2'] = df['Timestamp2'].str[:10]
df['AvantiID'] = df['Device_ID'] + df['Timestamp2']
df.to_csv(r'F:\Quadrant_prueba\parte_0002_todaslaspartes.csv')
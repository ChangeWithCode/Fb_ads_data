import pandas as pd
import urllib.request

df=pd.read_csv('data.csv')



for index,i in df.iterrows():
    if 'jpg' in i['Media']:
        f = open(str(index) + '.jpg', 'wb')
        f.write(urllib.request.urlopen(i['Media']).read())
        f.close()
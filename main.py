import pandas as pd
import requests
pd.set_option('display.max_columns', None)  #
import time
import numpy as np
test = 'https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=PerGame&Scope=S&Season=2023-24&SeasonType=Regular%20Season&StatCategory=PTS'

r = requests.get(url=test).json()
headers = r['resultSet']['headers']
data = r['resultSet']['rowSet']
#print(data)
headers2 = ['Rank','Player','min','fg_pct','ft_pct','pts']
df1 = data[0][2]
for i in range(5):
    print(data[i][2])
    print(data[i][7])


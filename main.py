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

#print(pd.DataFrame(data, columns = headers))
print("Top 5 players sorted by PPG (season averages): ")
print("----------------------------------------")
for i in range(5):
    print("NAME = " + str(data[i][2]))
    print("MIN = " + str(data[i][6]))
    print("FG_PCT = " + str(round(data[i][9] * 100,2)) + "%")
    print("PTS = " + str(data[i][23]))
    print("AST = " + str(data[i][19]))
    print("REB = " + str(data[i][18]))
    print("PTS+REB+AST = " + str(round(data[i][18]+data[i][19]+data[i][23],3)))
    print("----------------------------------------")



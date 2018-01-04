

import pymysql

con = pymysql.connect(
    host="localhost",
    user="root",
    password="123456",
    db="websites",
    port=3306,
    use_unicode=True,
    charset="utf8"
)
cur = con.cursor()

sql = "SELECT type,AVG(price) FROM Airbnb_Shanghai GROUP BY type"

cur.execute(sql)
result = cur.fetchall()
print(result)

roomType=[]
price=[]

for field in result:
    roomType.append(field[0])
    price.append(int(field[1]))

print(roomType)
print(price)


import plotly
plotly.tools.set_credentials_file(username='yyc', api_key='yfwQuYOyxJAeamQvdivC')

import plotly.plotly as py
from plotly.graph_objs import *

trace0 = Scatter(
    x = roomType,
    y = price
)

data = Data([trace0])

py.plot(data, filename = 'basic-line')
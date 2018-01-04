import pymysql

import plotly
plotly.tools.set_credentials_file(username='yyc', api_key='1puNznRHHWs5kPei8ESP')

import plotly.plotly as py
from plotly.graph_objs import *

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

city = ''
trace0 = ''
trace1 = ''
trace2 = ''

#每个城市图表
for i in range(0,3,1):
    if i == 2:
        city = 'Shanghai'
    if i == 1:
        city = 'Beijing'
    if i == 0:
        city = 'Chengdu'

    sql = "SELECT type,AVG(price) FROM Airbnb_"+city+" GROUP BY type"

    cur.execute(sql)
    result = cur.fetchall()
    print(result)

    roomType=[]
    price=[]

    for field in result:
        roomType.append(field[0])
        price.append(int(field[1]))

    if i == 2:
        Shanghai = Scatter(
            x=roomType,
            y=price,
            name='Shanghai'
        )
    if i == 1:
        Beijing = Scatter(
            x=roomType,
            y=price,
            name='Beijing'
        )
    if i == 0:
        Chengdu = Scatter(
            x=roomType,
            y=price,
            name='Chengdu'
        )


    print(roomType)
    print(price)

data = Data([Shanghai])

py.plot(data, filename = 'Shanghai')

data = Data([Beijing])

py.plot(data, filename = 'Beijing')

data = Data([Chengdu])

py.plot(data, filename = 'Chengdu')

#每个城市平均
for i in range(0,3,1):
    if i == 2:
        city = 'Shanghai'
    if i == 1:
        city = 'Beijing'
    if i == 0:
        city = 'Chengdu'

    sql = "SELECT AVG(price) FROM Airbnb_"+city+" "

    cur.execute(sql)
    result = cur.fetchall()
    print(result)

    price=int(result[0][0])

    print(price)

    if i == 2:
        Shanghai = Scatter(
            x="Shanghai",
            y=price,
            name='Shanghai'
        )
    if i == 1:
        Beijing = Scatter(
            x="Beijing",
            y=price,
            name='Beijing'
        )
    if i == 0:
        Chengdu = Scatter(
            x="Chengdu",
            y=price,
            name='Chengdu'
        )

data = Data([Chengdu,Shanghai,Beijing])

py.plot(data, filename = 'avg')

#每个城市比较
sql = "SELECT Airbnb_Shanghai.type,AVG(Airbnb_Shanghai.price),AVG(Airbnb_Chengdu.price),AVG(Airbnb_Beijing.price) FROM Airbnb_Shanghai " \
      "JOIN Airbnb_Chengdu ON Airbnb_Shanghai.type = Airbnb_Chengdu.type " \
      "JOIN Airbnb_Beijing ON Airbnb_Shanghai.type = Airbnb_Beijing.type " \
      "GROUP BY type"

cur.execute(sql)
result = cur.fetchall()
print(result)
roomType=[]
shanghaiPrice=[]
ChengduPrice=[]
BeijingPrice=[]

for field in result:
    roomType.append(field[0])
    shanghaiPrice.append(int(field[1]))
    ChengduPrice.append(int(field[2]))
    BeijingPrice.append(int(field[3]))


Shanghai = Scatter(
    x=roomType,
    y=shanghaiPrice,
    name='Shanghai'
)

Chengdu = Scatter(
    x=roomType,
    y=ChengduPrice,
    name='Chengdu'
)

Beijing = Scatter(
    x=roomType,
    y=BeijingPrice,
    name='Beijing'
)

print(roomType)
print(shanghaiPrice)
print(ChengduPrice)
print(BeijingPrice)

data = Data([Chengdu,Shanghai,Beijing])

py.plot(data, filename = 'compare')
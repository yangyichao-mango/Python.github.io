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
        )
    if i == 1:
        Beijing = Scatter(
            x=roomType,
            y=price,
        )
    if i == 0:
        Chengdu = Scatter(
            x=roomType,
            y=price,
        )


    print(roomType)
    print(price)

data = Data([Shanghai])

py.plot(data, filename = 'basic-line1')

data = Data([Beijing])

py.plot(data, filename = 'basic-line2')

data = Data([Chengdu])

py.plot(data, filename = 'basic-line3')


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
        )
    if i == 1:
        Beijing = Scatter(
            x="Beijing",
            y=price,
        )
    if i == 0:
        Chengdu = Scatter(
            x="Chengdu",
            y=price,
        )

data = Data([Chengdu,Shanghai,Beijing])

py.plot(data, filename = 'basic-line4')
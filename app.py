from flask import Flask, render_template
import requests
import json
app = Flask(__name__)

@app.route('/india')
def hello_world():
    return "Hello World"


class Cases:
    def __init__(self, loc, cci, ccf, dis, deaths,num, loc2):
        self.loc = loc
        self.cci = cci
        self.ccf = ccf
        self.dis = dis
        self.deaths = deaths
        self.num = num
        self.loc2 = loc2


    def __str__(self):
        print("location:", self.loc)
        print("confirmedCasesIndian:  ",self.cci)
        print("confirmedCasesForeign: ",self.ccf)
        print("discharged:",self.dis)
        print("Deaths:",self.deaths)
        print("Number:",self.num)
        print("location1:", self.loc2)
@app.route('/regional')
def covidData():

    r = requests.get('https://api.rootnet.in/covid19-in/stats/latest')
    r2 = requests.get('https://api.rootnet.in/covid19-in/contacts')
    x = r.json()
    x2 = r2.json()
    # print(r)
    length = len(x['data']['regional'])-1
    xlist = []
    # for i in range(1, length):
    #     xlist.append(Cases(x['data']['regional'][i]['loc'],x['data']['regional'][i]['confirmedCasesIndian'],x['data']['regional'][i]['confirmedCasesIndian'],x['data']['regional'][i]['discharged'],x['data']['regional'][i]['deaths']))
    # print(xlist)
    # z = Cases(x['data']['regional'][1]['loc'],x['data']['regional'][1]['confirmedCasesIndian'],x['data']['regional'][1]['confirmedCasesIndian'],x['data']['regional'][1]['discharged'],x['data']['regional'][1]['deaths'])
    for i in range(1, length):
        xlist.append(Cases(x['data']['regional'][i]['loc'],x['data']['regional'][i]['confirmedCasesIndian'],x['data']['regional'][i]['confirmedCasesIndian'],x['data']['regional'][i]['discharged'],x['data']['regional'][i]['deaths'], x2['data']['contacts']['regional'][i]['number'], x2['data']['contacts']['regional'][i]['loc']))
    # z.__str__()


    #  }
    # x =["akash", "nupur", "nancy", "geeta", "ashok"]
    return render_template("data.html",xlist = xlist)
        # print("location:", x['data']['regional'][i]['loc'])
        # print("confirmedCasesIndian:  ",x['data']['regional'][i]['confirmedCasesIndian'])
        # print("confirmedCasesForeign: ",x['data']['regional'][i]['confirmedCasesIndian'])
        # print("discharged:",x['data']['regional'][i]['discharged'])
        # print("Deaths:",x['data']['regional'][i]['deaths'])
        # print()

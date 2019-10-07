from django.shortcuts import render, redirect
from .models import Product, Alerts, Earnings
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from jchart import Chart
import requests,json




@login_required(login_url='/accounts/login/')
def index(request):

    prod = Product.objects.all()
    alerts = Alerts.objects.all()
    earnings = Earnings.objects.all()
    current_user = request.user
    alerts.offer = True
    # labels=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    # value = [1,2,3,4,5,6,7,8,9,10,11,12]
    # data = {
    #     "labels":labels,
    #     "value":value,
    # }
    # for i in data['value']:
    #     print(i)
    api_address='http://api.openweathermap.org/data/2.5/weather?appid=9b2ff67bcf783bf351ac8bb85a666f48&q='
    city = 'Bangalore'
    url = api_address + city
    json_data = requests.get(url).json()
    response_data = json_data['weather'][0]['main']
    # response_data = json_data['main']['temp']
    return render(request, "index.html", 
    {"response_data": response_data,"prod": prod, "alerts": alerts,"earnings":earnings ,"user": current_user.first_name})



class LineChart(Chart):
    chart_type = 'line'
    def get_datasets(self, **kwargs):
        earnings = Earnings.objects.all()
        for earning in earnings:
            jan = earning.jan
            feb = earning.feb
            mar = earning.mar
            apr = earning.apr
            may = earning.may
            jun = earning.jun
            jul = earning.jul
            aug = earning.aug
            sep = earning.sep
            octo = earning.octo
            nov = earning.nov
            dec = earning.dec
    
        return [{

            'data': [jan,feb,mar,apr,may,jun,jul,aug,sep,octo,nov,dec],
            'backgroundColor': [
                'skyblue',
            ],
            'label': "Monthly Earnings",
        }]
    
    def get_labels(self, **kwargs):
        earnings = Earnings.objects.all()
        for earning in earnings:
            jant = earning.jant
            febt = earning.febt
            mart = earning.mart
            aprt = earning.aprt
            mayt = earning.mayt
            junt = earning.junt
            jult = earning.jult
            augt = earning.augt
            sept = earning.sept
            octot = earning.octot
            novt = earning.novt
            dect = earning.dect
        return [jant, febt,mart,aprt,mayt,junt,jult,augt,sept,octot,novt,dect]


class PieChart(Chart):
    chart_type = 'pie'
    def get_datasets(self, **kwargs):
        earnings = Earnings.objects.all()
        for earning in earnings:
            jan = earning.jan
            feb = earning.feb
            mar = earning.mar
            apr = earning.apr
            may = earning.may
            jun = earning.jun
            jul = earning.jul
            aug = earning.aug
            sep = earning.sep
            octo = earning.octo
            nov = earning.nov
            dec = earning.dec
    
        return [{

            'data': [jan,feb,mar,apr,may,jun,jul,aug,sep,octo,nov,dec],
            'backgroundColor': [
                'skyblue',
                'lightgreen',
                'violet',
                'indigo',
                'maroon',
                'yellow',
                'orange',
                'pink',
                'red',
                'green',
                'black',
                'grey'
            ],
            'label': "Monthly Earnings",
        }]
    
    def get_labels(self, **kwargs):
        earnings = Earnings.objects.all()
        for earning in earnings:
            jant = earning.jant
            febt = earning.febt
            mart = earning.mart
            aprt = earning.aprt
            mayt = earning.mayt
            junt = earning.junt
            jult = earning.jult
            augt = earning.augt
            sept = earning.sept
            octot = earning.octot
            novt = earning.novt
            dect = earning.dect
        return [jant, febt,mart,aprt,mayt,junt,jult,augt,sept,octot,novt,dect]
        


def chart(request):
    render(request, 'index.html', {
        'line_chart': LineChart(),
        'pie_chart': PieChart(),
    })


class Flipkart:

    def order_details(self,order_id):
        return 'Order details' + order_id



flipkart = Flipkart()
print(flipkart.order_details('123'))
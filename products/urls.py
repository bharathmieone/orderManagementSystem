
from django.urls import path
from products import views
from jchart.views import ChartView
from .views import LineChart, PieChart, Flipkart

# LineChart is a class inheriting from jchart.Chart
line_chart = LineChart()
pie_chart = PieChart()



urlpatterns = [

    path('', views.index, name='home'),
    path('charts/line_chart/',ChartView.from_chart(line_chart), name='line_chart'),
    path('charts/pie_chart/', ChartView.from_chart(pie_chart), name='pie_chart'),

]

from django.shortcuts import render
import requests


# Create your views here.

def covid19_API(number):
    URL = 'http://openapi.seoul.go.kr:8088/46694f47746c686738397a4b706d64/json/TbCorona19CountStatus/1/' + str(
        number) + '/'
    API = requests.get(URL).json()
    data = API['TbCorona19CountStatus']['row']
    return data


def main(request):
    today = covid19_API(1)[0]
    data_week = covid19_API(7)
    data_list = covid19_API(365)
    data_week.reverse()
    data_list.reverse()
    context = {"today": today, "data_week": data_week, "data_list": data_list}
    return render(request, 'main.html', context)
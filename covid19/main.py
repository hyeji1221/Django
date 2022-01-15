import requests
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def covid19_API(number):
    URL = 'http://openapi.seoul.go.kr:8088/46694f47746c686738397a4b706d64/json/TbCorona19CountStatusJCG/1/'+str(number)+'/'
    API = requests.get(URL).json()
    data = API['TbCorona19CountStatusJCG']['row']
    return data

if __name__ == '__main__':
    covid19_API(5)
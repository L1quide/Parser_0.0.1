import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup as bs
import csv
def user_face():
    pass

url = 'https://novosibirsk.hh.ru/search/vacancy?area=1&st=searchVacancy&text=Python+junior&from=suggest_post'
headers = {'accept':'*/*','user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/80.0.3987.87 Chrome/80.0.3987.87 Safari/537.36'}
def get_html(*args, **kwargs):
    result = requests.get(url, headers=headers)
    try:
        result.status_code == 200
        print('ok')
        print(result)
    except:
        print('not')

get_html(url, headers)







def parser():
    pass

def writer():
    pass
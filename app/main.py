import requests
from requests.exceptions import HTTPError
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup as bs
import csv
def user_face():
    pass

url = 'https://novosibirsk.hh.ru/search/vacancy?area=1&st=searchVacancy&text=Python+junior&from=suggest_post'
headers = {'accept':'*/*','user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/80.0.3987.87 Chrome/80.0.3987.87 Safari/537.36'}
def get_url(*args, **kwargs):
    pass

def get_html(*args, **kwargs):
    session = requests.Session()
    result = session.get(url, headers=headers, auth=('79537809733','Xervam__13312'))
    try:
        result.status_code == 200
        print('ok')
        return result.text
    except:
        print('Error connect to site')


def get_page_data(html):
    soup = bs(html, 'lxml')
    slise = soup.find_all(attrs={'data-qa':'vacancy-serp__vacancy'})
    for chip in slise:
        try:
            name = chip.find(attrs={'data-qa':'vacancy-serp__vacancy-title'}).text
            print(name)
        except:
            name = ''
        try:
            linck = chip.find(attrs={'data-qa': 'vacancy-serp__vacancy-title'}).get('href')
        except:
            linck = ''
        data = {'name': name, 'linck': linck}
        writer(data)

def writer(data):
    with open('resul', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['name'],data['linck']))

def main(*args, **kwargs):

    get_page_data(get_html(url, headers))















# def page_counter(html):
#     soup = bs(html, 'lxml')
#     page = soup.find_all(attrs={'data-qa':'vacancy-serp__vacancy'})
#     i = 0
#     length = len(page)
#     while length > 0:
#         i += 1
#         payload['page'] = str(i)
#         length -= 1
#         session = requests.Session()
#         result = session.get(url, headers=headers, auth=('79537809733', 'Xervam__13312'), params=payload)
#         print(result.url)
#     return result


if __name__ == '__main__':
    main()
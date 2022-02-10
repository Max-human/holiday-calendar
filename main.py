import requests
from bs4 import BeautifulSoup
from header import headers


def get_html(url, params=None):
    r = requests.get(url, headers=headers, params=params)
    return r





def get_content(html):
    soup = BeautifulSoup(html.text, 'html.parser')
    u = 1
    if u == 1:
        num = 0
        holidays = []
        days = []

        items = soup.find_all('span', class_='caption days_section')

        for item in items:
            holidays.append({
                'title': item.find('span', class_='title').get_text(strip=True)
            }
            )
            if 'День' in holidays[num]['title'] or 'день' in holidays[num]['title']:
                days.append(holidays[num]['title'])
            else:
                break
            num += 1
        u = 0
    return days





def parse():
    html = get_html('https://www.calend.ru/day/')
    print(html)
    if html.status_code == 200:
        print('ok, ', html.status_code)
        return get_content(html)
    else:
        print('error, ', html.status_code)


parse()



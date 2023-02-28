import requests
import json
import datetime as dt

today = dt.datetime.now()
yesterday = today - dt.timedelta(days=1)
tomorrow = today + dt.timedelta(days=1)

# B100005528
# J100005670


def getLunch(day, month):
    school = 'J100005670'
    url = f'https://schoolmenukr.ml/api/high/{school}?date={day}&allergy=hidden&month={month}'
    response = requests.get(url)
    school_menu = json.loads(response.text)
    lunch = school_menu['menu'][0]['lunch']
    for menu in lunch:
        print(menu)


print('\n오늘급식:\n')
getLunch(today.day, today.month)
print('\n내일급식:\n')
getLunch(tomorrow.day, tomorrow.month)
print('\n어제급식:\n')
getLunch(yesterday.day, yesterday.month)

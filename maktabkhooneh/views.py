from django.http.response import HttpResponse, JsonResponse
import requests
from persiantools.jdatetime import JalaliDate, JalaliDateTime
import pyzt
from django.shortcuts import render



def get_today_holidays():
    todays_date = JalaliDate(1395, 3, 1).strftime("%Y/%m/%d")
    url = f'https://holidayapi.ir/jalali/{todays_date}'
    response = requests.get(url)
    data = response.json()
    return data

def holiday(request):
    data = get_today_holidays()
    request = data.get("is_holiday")
    message = 'کاربر گرامی با توجه به تعطیلی امروز ممکن است برخی از سفارشات و یا پشتیبانیها با تاخیر انجام شود'
    if request == True:
            return render(request, 'main_page/main_page.html', context=message)
    else:
        None
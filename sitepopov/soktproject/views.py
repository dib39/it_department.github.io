import sqlite3
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string
import re
from soktproject.models import ListOfRegistration
con = sqlite3.connect("db.sqlite3", timeout=30)
from django.contrib import messages

def index(request):
    return render(request, "soktproject/index.html", {'title': 'Главная'})

def record(request):
    if request.POST:
        pst = request.POST
        fio = pst['fio'].capitalize().replace(' ', '')
        un = pst['vuz'].replace(' ', '').upper()
        phone = pst['phone'].replace(' ', '')
        email = pst['email'].replace(' ', '')
        if (len(fio) * len(un) * len(phone) * len(email) != 0) and (re.findall(r'8\d{10}', phone) or re.findall(r'\+7\d{10}', phone)) and (re.findall(r"\w+@\w+\.\w+", email)):
            field = ListOfRegistration(fio=fio, university=un, phone=phone, email=email)
            field.save()
            messages.success(request, 'Данные успешно отправлены!')
        else:
            messages.warning(request, 'При отправке произошли проблемы. Проверьте правильность введённых данных и повторите попытку!')
    return render(request, "soktproject/record.html", {'title': 'Запись'})

def history(request):
    return render(request, "soktproject/history.html", {'title': 'История'})

def way(request):
    return render(request, "soktproject/way.html", {'title': 'Как добраться?'})

def photo(request):
    return render(request, "soktproject/photo.html", {'title': 'Фото'})

def page_not_found(request, exception):
    return HttpResponseNotFound("Страница не найдена")

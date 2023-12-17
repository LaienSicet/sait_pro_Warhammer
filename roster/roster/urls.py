from django.contrib import admin
from django.shortcuts import render
from django.urls import path
from django.urls import include


def baz_inf_w0(request, w):### экспериментальный уловитель некорректных ссылок
    return render(request, 'roster_1/nahalo.html', {'A': []})### экспериментальный уловитель некорректных ссылок


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('roster_1.urls')),
    path("dv/", include('dver.urls', namespace='users')),
    path("<path:w>", baz_inf_w0, name='AAA_w') ### экспериментальный уловитель некорректных ссылок
]




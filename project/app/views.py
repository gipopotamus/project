import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
import random


def index(request):
    category = ''
    goat_list = {
        'category': category,
        'urls': parser(category='cool')
    }
    context = {'image': random.choice(goat_list.get('urls'))}
    return render(request, 'app/index.html', context=context)


def parser(category):
    url = f"https://yandex.ru/images/search?text=goat%20{category}"
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    similar = soup.find_all('img', class_='serp-item__thumb justifier__thumb')
    links = []
    for i in similar:
        i = "https:" + str(i.get("src"))
        links.append(i)
    return links

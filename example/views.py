# example/views.py
from datetime import datetime
from django.shortcuts import *
import requests

def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Hello from Vercel!</h1>
            <p>The current time is { now }.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)

def ip(request):
    html = requests.get('https://ip.cn/').content.decode()
    return HttpResponse(html)

def ip_api(request):
    url = 'https://ip.cn/' + request.get_full_path()
    response = requests.get(url).content.decode()
    return HttpResponse(html)

def tmp(request):
    filename = '/var/task/django/db/backends/sqlite3/_functions.py'
    with open(filename, mode='r') as f:
        content = f.read()
        i = 1
        c = ''
        for a in content.split('\n'):
            str(i)
            if i < 10:
                '00' + i
            elif i > 10 and i < 100:
                '0' + i
            else:
                i = i
            c = c + i + ' ' + a + '\n'
        content = c.replace('\n', '</br>').replace(' ', '&nbsp;')
    return HttpResponse(content)
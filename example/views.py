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

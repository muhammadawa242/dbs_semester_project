from django.shortcuts import render, HttpResponse
from django import forms
from django.db import connection
from .models import Users

# Create your views here.
def index(req):
    if req.method == 'POST':
        with connection.cursor() as cursor:
            # cursor.execute('declare @s int; set @s = 1;')
            # cursor.execute('set @s = 1;')
            cursor.execute('select * from app_users where id = 1;')
            res = cursor.fetchall()
        
        return render(req, 'app/index.html', {
            'res' : res
        })
    else:
        return render(req, 'app/login.html')

def login(req):
    return render(req, 'app/login.html')

def signup(req):
    return render(req, 'app/signup.html')

def addtask(req):
    return render(req, 'app/addtask.html')

def taskdetails(req):
    return render(req, 'app/taskdetails.html')
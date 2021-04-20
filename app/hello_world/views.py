from django.shortcuts import render
import requests, json


def index(request):

    users="users"
    variable="variable"
    return render(request, 'index.html', {
        "users":users, 
        "variable":variable
    })

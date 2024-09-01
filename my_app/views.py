from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def user(request):
    return HttpResponse("<h1>Users</h1>")

def index(request):
    Users = [
        {
            "name": "John Doe",
            "age": 30
        },
        {
            "name": "Jane Smith",
            "age": 25
        },
        {
            "name": "Alice Johnson",
            "age": 40
        },
        {
            "name": "Bob Brown",
            "age": 35
        }
        ]

    return render(request,"index.html",context={"User":Users})
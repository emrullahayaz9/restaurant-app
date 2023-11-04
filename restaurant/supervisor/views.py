from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from menu import models
from supervisor.models import Tables 
from .models import InstantOrders
from django.contrib.auth.decorators import login_required
from table_sessions.models import Tables

def login1(request):
    form = AuthenticationForm()
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            instant_orders = InstantOrders.objects.all().values()
            boolean = False
            login(request, user)
            orders=models.Order.objects.all().values()
            order_set = {}
            j = 0
            for i in instant_orders:
                order_set[i["table"]]=models.Order.objects.get(id=i["order_id"])
                j+=1
            active_tables = Tables.objects.filter(is_full=True) 
            return render(request, "login_success.html", {"username":username,"boolean":boolean,"orders":orders, "form":form, "user":user,"active_tables":active_tables, "instant":instant_orders, "order_set":order_set})
        else:
            boolean = True
            errorMessage = "username or password incorrect"
            return render(request, "login_page.html", {"errorMessage":errorMessage, "boolean":boolean, "form":form,"instant":instant_orders})

    elif request.method=="GET":
         return render(request, "login_page.html", {"form":form})
 
@login_required(login_url="http://127.0.0.1:8000/supervisor/required")   
def logout_view(request):
    logout(request)
    return render(request, "SuccessLogout.html")

def checkout(request, table_number):
    x = InstantOrders.objects.get(table = table_number)
    


def delete_instants(request):
    InstantOrders.objects.all().delete()
    return HttpResponseRedirect("http://127.0.0.1:8000/supervisor/login")

def required(request):
    return render(request, "login_required.html")
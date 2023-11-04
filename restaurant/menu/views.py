from django.shortcuts import render, HttpResponseRedirect
from . import models
from django.contrib.auth.decorators import login_required
from supervisor.models import InstantOrders
from table_sessions.models import Tables

def login_page(request):
    return HttpResponseRedirect("http://127.0.0.1:8000/customer/")


def menu(request, id):
    food_names  = list(i["food_name"] for i in models.Food.objects.all().values())
    drink_names = list(i["drink_name"] for i in models.Drink.objects.all().values())
    salad_names = list(i["salad_name"] for i in models.Salad.objects.all().values())
    desert_name = list(i["desert_name"] for i in models.Desert.objects.all().values())
    get_status = Tables.objects.get(id=id)

    if request.method == "POST":
       food = ""
       drink = ""
       salad = ""
       desert = ""
       total = 0
       table_reference = Tables.objects.get(table_number = id)       
       reference = models.Order.objects.get_or_create(table_number=table_reference)       
       for i in food_names:
           if request.POST.get(i) == "on":
               food= food+i+", "
               the_food = models.Food.objects.get(food_name = i).price
               total+=the_food
       for i in drink_names:
           if request.POST.get(i) == "on":
               drink = drink+i+", "
               the_drink = models.Drink.objects.get(drink_name = i).price
               total+=the_drink
       for i in salad_names:
           if request.POST.get(i) == "on":
               salad = salad+i+", "
               the_salad = models.Salad.objects.get(salad_name = i).price
               total+=the_salad
       for i in desert_name:
           if request.POST.get(i) == "on":
               desert = desert+i+", "
               the_desert = models.Desert.objects.get(desert_name = i).price
               total+=the_desert
       
                
       food = reference.food + food  
       drink = reference.drink+drink
       desert = reference.desert + desert
       salad = reference.salad + salad
       total = reference.total_price+total
       exist_order = models.Order.objects.get_or_create(table_number=table_reference)
       exist_order.food=food
       exist_order.drink=drink
       exist_order.desert = desert
       exist_order.salad=salad
       exist_order.total=total

       exist_order.save()
       exist_order = models.Order.objects.get(table_number=table_reference)

#       models.Order(id="{reference.id}",table_number=id,food = food, drink=drink, salad= salad, desert=desert,total_price=total)
       #order.save()
       InstantOrders(table=id, order=exist_order).save()
       return render(request, "success.html")
        
    if request.method == "GET":
        print("here get")
        #table_reference = Tables.objects.get(table_number = id)
        #order = models.Order(table_number = table_reference, food=" ", drink=" ", salad=" ", desert=" ", total=0)
        #InstantOrders(id=id, table=id, order=order).save()

        deserts = models.Desert.objects.all().values
        foods = models.Food.objects.all().values
        salads = models.Salad.objects.all().values
        drinks = models.Drink.objects.all().values
        return render(request, "menu.html", {
            "deserts":deserts,
            "salads":salads,
            "drinks":drinks,
            "foods":foods
        })
    
    
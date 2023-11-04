from django.shortcuts import render, HttpResponseRedirect
from . import models
from django.contrib.auth import authenticate, login, logout
def table_number_session(request):
    if request.method=="POST":
        table_number_password = request.POST.get("table_number")
        user = authenticate(request, username=table_number_password, password=table_number_password)
        if user is not None:
            boolean = False
            login(request, user)
            #if not models.Tables.objects.get(table_password=table_number_password).is_full:
            x= models.Tables.objects.get(table_password=table_number_password)
            models.Tables(id=x.id, table_number = x.table_number, table_password=x.table_password, is_full = True).save()
            return HttpResponseRedirect(f"http://127.0.0.1:8000/menu/page/{x.table_number}")
            # else:
            #     boolean = True
            #     error_message = ("this table is reserved or full")
            #     return render(request, "table_number.html", {"boolean":boolean, "error":error_message })
        else:
            boolean = True
            error_message = "Table password incorrect"
            return render(request, "table_number.html",{"error":error_message,"boolean":boolean})
    elif request.method=="GET":

        return render(request, "table_number.html")
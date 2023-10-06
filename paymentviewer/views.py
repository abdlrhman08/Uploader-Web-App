from django.shortcuts import redirect, render

# Create your views here.
from django.http import HttpResponse, HttpRequest
from django.contrib.auth import models, authenticate, login as signin
from django.contrib.auth.decorators import login_required

import pandas as pd
import numpy as np

from .models import Accounts


def index(request):
    return redirect("login")

def login(request: HttpRequest):

    if (request.method == "POST"):
        user: models.User = authenticate(request, username=request.POST["uname"], password=request.POST["psw"])

        if (user.is_authenticated):
            signin(request, user)
            return redirect("uploader")
    return render(request, "paymentviewer/index.html")

@login_required
def uploader(request: HttpRequest):

    if (request.method == "POST"):
        data = pd.read_excel(request.FILES["datafile"])
        cleared_data = data.replace({np.nan: None})

        accounts = [{
            "type": row["type"],
            "email": row["email"],
            "email_pass": row["email_pass"],
            "password": row["password"],
            "battle_tag": row["battle_tag"],
            "name": row["name"],
            "number": row["number"],
            "safe_um_user": row["safe_um_user"],
            "safe_um_pass": row["safe_um_pass"],
            "creation_date": row["creation_date"],
            "birth_date": row["birth_date"],
            "hex_secret_key": row["hex_secret_key"],
            "serial": row["serial"],
            "restore_code": ["restore_code"]
        } for _, row in cleared_data.iterrows()]
        
        request.session["account_data"] = accounts

        return render(request, "paymentviewer/uploader.html", {"accounts": accounts})
    
    return render(request, "paymentviewer/uploader.html")

@login_required
def confirm(request: HttpRequest):

    Accounts.objects.bulk_create([Accounts(
        type=account["type"],
        email=account["email"],
        password=account["password"],
        battle_tag=account["battle_tag"],
        phonenum=account["phonenum"],
        safe_um_user=account["safe_um_user"],
        safe_um_pass=account["safe_um_pass"],
        birth_date=account["birth_date"],
        hex_secret_key = account["hex_secret_key"] if account["hex_secret_key"] is not None else None,
        serial = account["serial"] if account["serial"] is not None else None,
        restore_code =  account["restore_code"] if account["restore_code"] is not None else None,
        finished=False,
        taken=False        
    ) for account in request.session["account_data"]])        

    return HttpResponse("Done")
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template.context_processors import csrf
from django.contrib.auth.models import User
from .forms import SignUpForm


from django.shortcuts import render, HttpResponse

# Create your views here.
def signup(request):
    c ={}
    c.update(csrf(request))
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user =form.save()
            user.refresh_from_db()
            user.save()
            return HttpResponse("data saved")
    else:
        form = SignUpForm()
        print form

    return render(request,'signup.html',{'form': form},c)


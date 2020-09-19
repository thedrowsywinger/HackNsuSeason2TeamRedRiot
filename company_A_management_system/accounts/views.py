from django.shortcuts import render, redirect

from django.contrib.auth.models import User


def SigningUpCompanyRepresentatives(request):

    return render(request, "accounts/signup.html")
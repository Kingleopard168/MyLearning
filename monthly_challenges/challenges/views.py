from http.client import HTTPResponse
import imp
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
import challenges

monthly_challenges = {
    "january":"Eat no meat for the entire month",
    "february":"walk for at least 20 minuters every day",
    "march":"Learn Django for at least 20 minutes every day",
    "april":"Eat no meat for the entire month",
    "may":"Learn Django for at least 20 minutes every day",
    "june":"at no meat for the entire month",
    "july":"Learn Django for at least 20 minutes every day",
    "august":"walk for at least 20 minuters every day",
    "september":"Eat no meat for the entire month",
    "october":"Learn Django for at least 20 minutes every day",
    "november":"walk for at least 20 minuters every day",
    "december":"Learn Django for at least 20 minutes every day"
}
# Create your views here.

def january(request):
    return HttpResponse("Eat no meat for the entire month")

def february(request):
    return HttpResponse("walk for at least 20 minuters every day")

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    return HttpResponseRedirect("/challenges/"+ redirect_month)
#    return HttpResponse(month)
    
def monthly_challenge(request, month):
    try:
        challenges_text = monthly_challenges[month]
    except:
        return HttpResponseNotFound("this month is not supported")

#    if month == "january":
#       challenges_text = "Eat no meat for the entire month"
#    elif month == "february":
#        challenges_text = "walk for at least 20 minuters every day"
#    elif month == "march":
#        challenges_text = "Learn Django for at least 20 minutes every day"
#    else:
#        return HttpResponseNotFound("this month is not supported")
    return HttpResponse(challenges_text)
from django.shortcuts import render

def home (response):
    return render(response, "NC_website/home1.html")

def rentals (response):
    return render(response, "NC_website/rentals.html")
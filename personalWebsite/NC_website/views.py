from django.shortcuts import render

def home (response):
    return render(response, "NC_website/home1.html")
    # return render(response, "NC_website/NC_base.html")

def rentals (response):
    return render(response, "NC_website/rentals.html")

def services (response):
    return render(response, "NC_website/services.html")

def events (response):
    return render(response, "NC_website/events.html")

def contact (response):
    return render(response, "NC_website/contact.html")
from django.shortcuts import render

def landing_page (response):
    return render(response, 'landing_page/landing_page.html')

from django.shortcuts import render

def index_page(request):
    return render(request, 'index.html')

def about_page(request):
    return render(request, 'about.html')

def contact_page(request):
    return render(request, 'contact.html')


def detail_page(request):
    return render(request, 'detail-page.html')


def listing_page(request):
    return render(request, 'listing-page.html')



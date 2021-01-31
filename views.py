from my_framework import render


def main_view(request):
    return '200 OK', render('index.html')


def about_view(request):
    return '200 OK', render('about.html')


def contacts_view(request):
    return '200 OK', render('contacts.html')

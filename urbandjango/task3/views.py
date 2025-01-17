from django.shortcuts import render

def index(request):
    return render(request, 'third_task/index.html')

def shop(request):
    items = {
        'Консультация': '300 руб.',
        'Клуб "Действия"': '1700 руб.',
        'Ведение аккаунтов': '50000 руб.'
    }
    return render(request, 'third_task/shop.html', {'items': items})

def cart(request):
    return render(request, 'third_task/cart.html')

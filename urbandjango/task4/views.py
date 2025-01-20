from django.shortcuts import render

def index(request):
    return render(request, 'fourth_task/index.html')

def shop(request):
    items = {
        'Игра 1': '500 руб.',
        'Игра 2': '700 руб.',
        'Игра 3': '300 руб.'
    }
    return render(request, 'fourth_task/shop.html', {'items': items})

def games_view(request):
        context = {'games': ['Atomic Heart', 'Cyberpunk 2077']}
        return render(request, 'fourth_task/games.html', context)


def cart(request):
    return render(request, 'fourth_task/cart.html')

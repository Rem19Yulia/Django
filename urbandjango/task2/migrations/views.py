from django.http import HttpResponse
from django.views import View
from django.shortcuts import render

#классовое представление:

class ClassBasedView(View):
    def get(self, request):
        return render(request, 'second_task/class_template.html')


#функциональное представление:

def FunctionBasedView(request):
    return render(request, 'second_task/function_template.html')

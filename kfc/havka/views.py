from django.shortcuts import render

# Генерация стандартного HTTP ответа
from django.http import HttpResponse

# def index(request):
#     return HttpResponse("Hello, World")

def index(request):
    print(request.__dict__)
    return render(request, 'havka/index.html')
def about(request):
    print(request.__dict__)
    return render(request, 'havka/about.html')


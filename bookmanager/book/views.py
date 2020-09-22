from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    # 准备上下文
    context = {'name': '《水浒传》'}

    return render(request, 'index.html', context)

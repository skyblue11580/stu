from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'name': 'hello'
    }

    return render(request, 'index.html', context)

def goods(request, cat_id, goods_id):
    context = {
        'cat_id': 'cat_id为' + cat_id,
        'goods_id': 'goods_id为' + goods_id
    }

    return render(request, 'book/goods.html', context)

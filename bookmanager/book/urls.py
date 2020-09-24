# urlpatterns
from django.urls import path

from book.views import index, goods

urlpatterns = [
    path('index/', index),
    path('', index),
    path('<cat_id>/<goods_id>/', goods)
]
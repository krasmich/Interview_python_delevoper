from django.shortcuts import render

from django.views.generic.list import ListView
from .models import GoodItems


class GoodsModelListView(ListView):
    model = GoodItems
    template_name = 'goods_list.html'

    def get_queryset(self):
        items = GoodItems.objects.all()
        return items

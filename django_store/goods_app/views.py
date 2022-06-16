from django.shortcuts import render, get_object_or_404

from .models import Category, GoodItems


def categories(request):
    return {
        'categories': Category.objects.all()
    }


def all_goods(request):
    goods = GoodItems.on_site.all()
    return render(request, 'goods_app/home.html', {'goods': goods})


def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    goods = GoodItems.on_site.select_related('category').filter(category=category)
    return render(request, 'goods_app/category.html', {'category': category, 'goods': goods})

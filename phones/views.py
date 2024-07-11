from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_pages = request.GET.get('sort')
    items = Phone.objects.all()
    if sort_pages == 'name':
        items = Phone.objects.order_by('name')
    if sort_pages == 'min_price':
        items = Phone.objects.order_by('price')
    if sort_pages == 'max_price':
        items = Phone.objects.order_by('-price')

    context = {'phones': items}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    item = Phone.objects.get(slug=slug)
    context = {'phone': item}
    return render(request, template, context)

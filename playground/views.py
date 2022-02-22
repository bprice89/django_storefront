from itertools import product
from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product
from store.models import Customer
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from store.models import Order
from store.models import OrderItem
from store.models import Collection






def say_hello(request):
    # use double underscore to connect tables
    queryset= OrderItem.objects.filter(product__collection__id=3)
    # queryset = Collection.objects.filter(featured_product__isnull=True)
    # queryset= Order.objects.filter(customer__id=1)
    # queryset= Product.objects.filter(unit_price__range=(20,30))
    # try:
    #     product = Product.objects.get(pk=1) #pk is primary key
    # except ObjectDoesNotExist:
    #     pass
    # query_set = Product.objects.all()
    # query_set.filter().filter()
    # for product in query_set:
    #     print(product)

    # query_set[0:5]

    return render(request, 'hello.html', {'name': 'Mosh', 'products': queryset})

def queries(request):
    # products: inventory < 10 and price < 20
    queryset = Product.objects.filter(inventory__lt=10).filter(unit_price__lt=20)
    return render(request, 'hello.html', {'products': list(queryset)})

def or_operator(request):
    # Products: inventory < 10 OR price < 20
    queryset = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__lt=20))
    return render(request, 'hello.html', {'products': list(queryset)})

def ordering(request):
    # ordering tables asc and desc
    queryset = Product.objects.order_by('title') #ascending
    queryset = Product.objects.order_by('-title') #descending
    return render(request, 'hello.html', {'products': list(queryset)})

def filter_sort(request):
    queryset = Product.objects.filter(collection__id=1).order_by('unit_price')
    return render(request, 'hello.html', {'products': list(queryset)})

def access_individual(request):
    product = Product.objects.order_by('unit_price')[0] #first object in query set
    product = Product.objects.earliest('unit_price') #will get earliest object in set
    product = Product.objects.latest('unit_price') #will get last object in set
    return render(request, 'hello.html', {'products': product})

def values(request):
    queryset = Product.objects.values('id', 'title') #will only grab selected fields(values)
    return render(request, 'hello.html', {'products': queryset})

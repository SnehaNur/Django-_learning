from django.shortcuts import render
from django.http import HttpResponse
from store.models import Order,Product,OrderItem,Customer,Collection
from django.core.exceptions import ObjectDoesNotExist
#from django.db.models.aggregates import Count,Max,Min,Avg,Sum
from django.db.models.functions import Concat
from django.db.models import Value,F,Func,Count
from django.db.models import Q,F

def say_hello(request):
    #queryset= Product.objects.filter(unit_price__range=(20,30))
    #queryset= Product.objects.filter(title__icontains='coffee')
    #queryset= Product.objects.filter(title__startswith='Coffee')
    #queryset= Product.objects.filter(last_update__year=2021)
    #queryset= Product.objects.filter(Q(inventory__lt=10) & ~Q(unit_price__lt=20))
    #queryset= Product.objects.filter(inventory=F('unit_price'))
    #queryset= Product.objects.order_by('title')
    #queryset= Product.objects.all()[:5]
    #queryset= Product.objects.values('id')
    #queryset= Customer.objects.values('id')
    '''queryset= Product.objects.filter(
       id__in=Customer.objects.values('id').distinct()).order_by('title')
    '''
    #queryset= Product.objects.only('id','title')
    #queryset= Product.objects.prefetch_related('promotion').select_related('collection').all()
    #queryset= Product.objects.select_related('collection').order_by('-id')[:10]
    '''queryset= Customer.objects.annotate(
         order_count = Count('order')
    )
    
    queryset= Product.objects.all()
    queryset[0]
    list(queryset)
    
    collection = Collection(pk=11)
    collection.title = 'Games'
    collection.featured_product = None
    collection.save()
    '''
    Collection.objects.filter(pk=11).update(featured_product=None)
    return render(request, 'hello.html', {'name':'Hafu'})

# for aggregate
    #result= Product.objects.aggregate(count = Count('id'))
    #return render(request, 'hello.html', {'name':'Hafu', 'result':result})

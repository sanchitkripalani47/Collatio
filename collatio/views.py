from django.db.models import query
from django.shortcuts import render
from django.http import HttpResponse
import re
from .models import *
from django.contrib.postgres.search import SearchQuery, SearchVector

#Currently active list of filters
class CurrentFilters:

    def __init__(self):
        self.current_filters = []
        self.filter_tag = ""
        self.sortingOrder = 0


current_filter = CurrentFilters()
search_bar_filters = CurrentFilters()


def home(request):
    context={}
    return render(request, 'collatio/home.html', context)


def is_refreshed(current_filter_list, new_filter_list):
    len_current = len(current_filter_list)
    len_new = len(new_filter_list)
    if (len_current != 0): 
        for brand_element in new_filter_list:
            if brand_element not in current_filter_list:
                return False
        return True
    else:
        return False

def search(request, primaryKey):
    tag = Tag.objects.get(id=int(primaryKey))
    products = Product.objects.filter(tags=tag)
    brands = products.values_list('brand', flat=True).distinct()

    queryDict = request.GET.values()
    new_filter = list(queryDict)

    if len(new_filter) != 0:

        if (current_filter.filter_tag == "") or (tag == current_filter.filter_tag):
            if 'Price low to high' in new_filter:
                current_filter.sortingOrder = -1
            elif 'Price high to low' in new_filter:
                current_filter.sortingOrder = 1
            elif not is_refreshed(current_filter.current_filters, new_filter):
                current_filter.current_filters.extend(new_filter)

            if len(current_filter.current_filters) != 0:
                products = products.filter(brand__in=current_filter.current_filters)

            if current_filter.sortingOrder == 1:
                products = products.order_by('-price')
            elif current_filter.sortingOrder == -1:
                products = products.order_by('price')
        else:
            products = Product.objects.filter(tags=tag)
            current_filter.filter_tag = ""
            current_filter.sortingOrder = 0
            current_filter.current_filters = []

        if 'Reset' in new_filter:
            products = Product.objects.filter(tags=tag)
            current_filter.filter_tag = ""
            current_filter.sortingOrder = 0
            current_filter.current_filters = []
    else:
        products = Product.objects.filter(tags=tag)
        current_filter.filter_tag = ""
        current_filter.sortingOrder = 0
        current_filter.current_filters = []

    context={'products': products, 'tag':tag, 'brands':brands, 'current_filter': current_filter}
    return render(request, 'collatio/search.html', context)

def categories(request):
    tags = Tag.objects.all()
    context={'tags':tags}
    return render(request, 'collatio/category.html', context)

def productDetails(request, pk):
    product = Product.objects.get(name=str(pk))

    detailList = list(product.description.split('\\n\\n'))

    context={'product': product, 'detailList':detailList}
    return render(request, 'collatio/product_detail.html', context)

def allProducts(request):
    search_bar_entry = list(request.GET.values())[0]
    search_query = -1
    
    if 'Price low to high' == search_bar_entry:
        search_bar_filters.sortingOrder = -1
    elif 'Price high to low' == search_bar_entry:
        search_bar_filters.sortingOrder = 1
    elif request.GET.get('search_bar'):
        search_query = SearchQuery(search_bar_entry)
        search_bar_filters.filter_tag = search_bar_entry 
        search_bar_filters.current_filters = search_bar_entry

    vector = SearchVector('tags', 'brand', 'name', config='english')

    if search_query != -1:
        all_search_results = Product.objects.annotate(search=vector).filter(search=search_query)
    else:
        all_search_results = Product.objects.annotate(search=vector).filter(search=SearchQuery(search_bar_filters.filter_tag))
    
    tags_id = all_search_results.values_list('tags', flat=True).distinct()
    tags = Tag.objects.filter(id__in=tags_id)

    if search_bar_filters.sortingOrder == 1:
        all_search_results = all_search_results.order_by('-price')
    elif search_bar_filters.sortingOrder == -1:
        all_search_results = all_search_results.order_by('price')

    if len(list(request.GET.values())) == 0:
        all_search_results = Product.objects.annotate(search=vector).filter(search=search_query)
        search_bar_filters.filter_tag = ""
        search_bar_filters.sortingOrder = 0
        search_bar_filters.current_filters = []
    
    context = {'all_search_results': all_search_results, 'search_bar_entry': search_bar_entry, 'tags':tags}

    return render(request, 'collatio/all_products.html', context)
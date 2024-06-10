from django.shortcuts import render
from Main_page.models import Main

# Create your views here.
def product_page(request, id):
    context = {}
    context['product'] = Main.objects.get(id = id)
    print(context['product'])
    return render(request, f'Product_page/product_page1.html', context)
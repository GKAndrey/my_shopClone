from django.shortcuts import render
from .models import Main
from django.contrib.auth.models import User
# Create your views here.
def main_page(request):
    
    # username = User.objects.get(username = request.user.username)
    
    # ...
    product = Main.objects.all()
    
    context = {
        # "login": request.user.username,
        'products': product,
        # "auth": request.user.is_authenticated
    }
    # print(product)
    return render(request, 'Main_page/main.html', context)
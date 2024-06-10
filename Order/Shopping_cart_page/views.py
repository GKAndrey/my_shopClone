from django.shortcuts import render, redirect
from .models import Cart
from Main_page.models import Main

# Create your views here.
def cart_page(request):
    if not request.user.is_authenticated:
        return redirect('main_page')
    carts = Cart.objects.get(user_id=request.user.id)
    context = {}
    context["products_cart"] = []
    try:
        list_id = carts.product_id.split(",")
        num = 1
        for i in list_id:
            context["products_cart"].append({"obj":Main.objects.get(id = i), "num":f"{num}"})
            num += 1
    except:
        pass
    context["opti_prise"] = 0
    context["len_prod"] = num - 1
    print(context["opti_prise"])
    for i in context["products_cart"]:
        context["opti_prise"] += i["obj"].price
        print(context["opti_prise"])
    # print(context, len(context["products_cart"]))
    return render(request, 'Shopping_cart_page/cart.html', context)

def delete_product_cart(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            carts = Cart.objects.get(user_id=request.user.id)
            id_product = request.POST.get("id_product")
            list = carts.product_id
            list = list.split(",")
            list.pop(int(id_product))
            list.pop(-1)
            lists = ''
            for i in list:
                lists += f"{i},"
            carts.product_id = lists
            carts.save()
        else:
            return redirect('main_page')
    return redirect('cart_page')


def add_cart_product(request):
    if not request.user.is_authenticated:
        return redirect('main_page')
    if request.method == 'POST':
        ids = request.POST.get("ids")
        # print(request.user.id)
        if ids:
            carts = Cart.objects.get(user_id=request.user.id)
            carts.product_id += f"{ids},"
            carts.save()
    return redirect('main_page')
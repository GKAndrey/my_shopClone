from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.db.utils import IntegrityError
from Shopping_cart_page.models import Cart

# Create your views here.
# def authorization(request):
#     if request.user.is_authenticated:
#         return redirect('main_page')
#     return render(request, 'Authorization_Registration/authorization.html')

def registration(request):
    if request.user.is_authenticated:
        return redirect('main_page')
    return render(request, 'Authorization_Registration/registration.html')

def register (request):

    context = {}
    # print(request.user.is_authenticated)
    if request.user.is_authenticated:
        return redirect('main_page')
    if request.method == 'POST':
        login_name = request.POST.get("username")
        email = request.POST.get("email")
        number = request.POST.get("number")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        context["login"] = login_name
        context["email"] = email
        context["number"] = number
        context["password"] = password
        context["confirm_password"] = confirm_password
        if login_name and email and number and password and confirm_password:
            if len(password) >= 8:
                try:
                    number = int(number)
                except:
                    context['error'] = 'Мобільний номер не задовольняє шаблон (тільки цифри)'
                finally:
                    if password == confirm_password:
                        try:
                            user_reade = User.objects.create_user(username=login_name, email=email,password=password)
                            login(request, user_reade)
                            print("Join person")
                            Cart.objects.create(user_id=request.user.id)
                            return redirect('main_page')
                        except IntegrityError:
                            print("Error person")
                            context['error'] = 'Такий користувач вже існує'
                    else:
                        print("Error password")
                        context['error'] = 'Паролі не співпадають'
            else:
                print("Error number")
                context['error'] = 'Кількість символів має бути довшою або дорівнювати 8'
        else:
            context['error'] = 'Заповніть всі поля'
    return render(request, 'Authorization_Registration/registration.html', context)

def logins(request):
    context = {}
    context['error'] = ""
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
        context['error'] = 'Ти вже авторизувався'
        return redirect('main_page')
    if request.method == 'POST':
        username = request.POST.get('login')
        password = request.POST.get('password')
        if username and password:
            print(1)
            user = authenticate(username = username, password = password)
            if user:
                print(user)
                login(request, user)
                return redirect('main_page')
            else:
                user = authenticate(email = username, password = password)
                if user:
                    login(request, user)
                    return redirect('main_page', context)
                else:
                    context['error'] = 'Логін або пароль невірні'
        else:
            context['error'] = 'Заповніть всі поля'
    return render(request, 'Authorization_Registration/authorization.html', context)

def logouts(request):
    logout(request)
    return redirect('main_page')
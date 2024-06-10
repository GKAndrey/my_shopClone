"""
URL configuration for Order project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .settings import DEBUG, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static
import Main_page.views as main_page_views
import Product_page.views as product_page_views
import Shopping_cart_page.views as shopping_cart_views
import Contact_page.views as contact_views
import Authorization_Registration.views as authorization_registration_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page_views.main_page, name= "main_page"),
    path('product_page<int:id>/', product_page_views.product_page, name= "product_page"),
    path('cart_page/', shopping_cart_views.cart_page, name= "cart_page"),
    path('add_cart_product/', shopping_cart_views.add_cart_product, name= "add_cart_product"),
    path('contact_page/', contact_views.contact_page, name= "contact_page"),
    path('registration_page/', authorization_registration_views.registration, name= "registrationPage"),
    path('logins/', authorization_registration_views.logins, name='login'),
    path('register/', authorization_registration_views.register, name='register'),
    path('logouts/', authorization_registration_views.logouts, name='logout'),
    path('delete_product_cart/', shopping_cart_views.delete_product_cart, name='delete_product_cart'),
]

if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
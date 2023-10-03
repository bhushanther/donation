from app12 import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_page),
    path('home/',views.home_page, name='home'),
    path('about/',views.about_us, name='about'),
    path('contact/',views.contact_us, name='contact'),
    path('donate/',views.donate_us, name='donate'),
    path('payment_m/',views.payment_method, name='paymentmethod'),
    path('payment/',views.payment_details, name='paymentD'),



    
    

    



]

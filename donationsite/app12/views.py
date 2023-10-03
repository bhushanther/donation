from django.shortcuts import render, redirect
from .models import Donate

def home_page(request):
    return render(request, "index.html")


def about_us(request):
    return render(request, 'about.html')

def contact_us(request):
    return render(request, 'contact.html')




def donate_us(request):
    return render(request, 'donate.html')


        
def payment_method(request):
    return render(request, 'payment.html')


           



def payment_details(request):
    if request.method=="POST":
        full_name=request.POST.get('fullname')
        email=request.POST.get('email')
        amount=request.POST.get('amount')
        

        entry=Donate.objects.create(name=full_name,
                    email=email,
                    amount=amount)
        entry.save()
        return redirect('/payment_m/')

    return render(request, 'payment_details.html')



















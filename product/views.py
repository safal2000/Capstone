from .models import Product
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.contrib.auth import login
from django.contrib.auth.views import LoginView

def online_shop(request):
    """
    Fetches a list of products from a database and generates it on the online shop webpage.
    """
    products = Product.objects.all()  # Fetch a list of products from your database
    return render(request, 'online_shop/online_shop.html', {'products': products})



class ProductDetailView(DetailView):
    """
    Displays a more detailed view of the product in a seperate webpage
    """
    model = Product
    template_name = 'online_shop/product_detail.html'
    context_object_name = 'product'
  


def your_signup_view(request):
    """
    Handles user registration
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

           
            url = reverse('product:online_shop')

            return redirect(url)  
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


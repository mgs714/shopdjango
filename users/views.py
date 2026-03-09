from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import RegisterForm


def register(request):
    if request.user.is_authenticated:
        return redirect('shop:product_list')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Bienvenue {user.first_name} ! Votre compte a été créé.')
            return redirect('shop:product_list')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})


def user_login(request):
    if request.user.is_authenticated:
        return redirect('shop:product_list')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Bienvenue {user.first_name or user.username} !')
            next_url = request.GET.get('next', 'shop:product_list')
            return redirect(next_url)
        else:
            messages.error(request, 'Identifiants incorrects.')
    else:
        form = AuthenticationForm()
        for field in form.fields.values():
            field.widget.attrs['class'] = 'form-control'
    return render(request, 'users/login.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.info(request, 'Vous êtes déconnecté.')
    return redirect('shop:product_list')


def profile(request):
    from orders.models import Order
    orders = []
    if request.user.is_authenticated:
        orders = Order.objects.filter(user=request.user).order_by('-created')[:5]
    return render(request, 'users/profile.html', {'orders': orders})

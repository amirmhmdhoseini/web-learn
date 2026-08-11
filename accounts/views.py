from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from .forms import LoginForm


def login_view(request):

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            user = form.cleaned_data.get('user')

            login(request, user)

            return redirect('/')

    else:
        form = LoginForm()

    context = {
        'form': form
    }

    return render(request, 'accounts/login.html', context)


@login_required
def logout_view(request):
    logout(request)
    return redirect('/')


def signup_view(request):

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = UserCreationForm()

    context = {
        'form': form
    }

    return render(request, 'accounts/signup.html', context)

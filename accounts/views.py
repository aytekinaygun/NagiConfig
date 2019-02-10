from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages
from .forms import LoginForm

def login_view(request):
    if request.user.is_authenticated: # Kullanıcı giriş yapmış ise
        return redirect('/home/')

    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user     = authenticate(username=username, password=password)
        login(request, user)
        # messages.success(request, 'Yeni kayıt başarılı.', extra_tags='alert-success')
        return redirect('/home/')
    context = {
        'form' : form,
        }
    return render(request, 'login_form.html', context)

def logout_view(request):
    logout(request)
    return redirect('/login')

from django.shortcuts import render, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import LoginForm
from django.http import HttpResponse


# Create your views here.

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, password=cd['password'], username=cd['username'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'Admin_site/admin.html')
                else:
                    return HttpResponse('account Diactivated')
            else:
                return HttpResponse('invalid account/username')
    else:
        form = LoginForm()
    return render(request, 'Admin_site/login.html', {'form':form})


                
                


@login_required
def Admin(request):
    return render(request, 'Admin_site/admin.html',)

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from .forms import LoginUserForm
#from ..roster_1.models import Ros

# A = Ros.objects.all()
def logout_user(request):
    logout(request)
    return render(request, 'roster_1/nahalo.html', {'A': []})

def login_user(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user and user.is_active:
                login(request, user)
                return render(request, 'roster_1/nahalo.html', {'A': []})#HttpResponseRedirect(reverse('AAA'))
    else:
        form = LoginUserForm()
    return render(request, 'dver/dver_login.html', {'form': form})

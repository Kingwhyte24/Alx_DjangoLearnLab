from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

# Create your views here.

def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
        
    else:
        form = UserRegisterForm()
        return render(form, 'blog/register.html', {'form': form})

@login_required
def profile_view(request):
    render(request, 'blog/profile.html')
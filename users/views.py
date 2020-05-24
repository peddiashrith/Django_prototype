from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm

# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request, 'Account created for {}. You are now ready to login'.format(username))
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "users/signup.html", {'form':form})
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import places
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm


def index(request):
    attrac = places.objects.all()
    return render(request, 'main/index.html', {'attrac': attrac})


def about(request):
    return render(request, 'main/aboutus.html')



def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return redirect('login')  # Перенаправляем на страницу логина после успешной регистрации
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'user_form': user_form})



@login_required
def user(request):
    return render(request, 'main/user.html')

# Сделать кнопку лайка
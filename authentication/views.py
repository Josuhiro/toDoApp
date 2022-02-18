from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect


# Create your views here.
from tasks.forms import CreateUserForm


def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')  # 'username' bo input się tak nazywa w login.html
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Nazwa użytkownika i/lub hasło są niepoprawne')
    return render(request, 'authentication/login.html')


def registerUser(request):
    form = CreateUserForm()
    form.fields['username'].widget.attrs.update({
        'placeholder': 'Nazwa użytkownika'
    })
    form.fields['password1'].widget.attrs.update({
        'placeholder': 'Hasło'
    })
    form.fields['password2'].widget.attrs.update({
        'placeholder': 'Powtórz hasło'
    })
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Poprawnie stworzono konto' + username)
            return redirect('login')
    context = {'form': form}
    return render(request, 'authentication/register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')

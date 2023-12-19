from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from authentication.forms import UserRegistrationForm,UserSettingsForm,UserProfileForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def register_view(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Account created successfully. You can now log in.')
            return redirect('login')
        else:
            messages.warning(request, 'Invalid credentials. Please correct the errors below.')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f'You have been successfully logged in as {username}')
                return redirect('home')
            

    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

@login_required(login_url="login")
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out')
    return redirect('login')

@login_required(login_url="login")
def setting_change(request):
    if request.method == "POST":
        usersetting = UserSettingsForm(request.POST, instance=request.user)
        userprofile = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if usersetting.is_valid() and userprofile.is_valid():
            current_password = request.POST.get('current_password')
            user = authenticate(request, username=request.user.username, password=current_password)
            if user is not None:
                usersetting.save()
                userprofile.save()
                messages.success(request, f'Your profile has been successfully updated')
                return redirect('setting')
            else:
                messages.warning(request, f'Your current password is wrong')
        else:
            messages.warning(request, f'Some error occurred')
    else:
        usersetting = UserSettingsForm(instance=request.user)
        userprofile = UserProfileForm(instance=request.user.userprofile)

    context = {
        'userprofile': userprofile,
        'usersetting': usersetting
    }
    return render(request, 'setting.html', context)

        

        
        

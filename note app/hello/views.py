from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddTaskForm, UpdateTaskForm
from .models import Task







def home(request):    
    tasks = Task.objects.all()

    #loggin in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #auth
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login Successful!")
            return redirect('home')
        else:
            messages.success(request, "Unable To Login...") 
            return redirect('home')   
    else:
        return render(request, 'home.html', {'tasks':tasks})

def logout_user(request):
    logout(request)
    messages.success(request, "Logout Successful!")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Registration Successful!")
            return redirect('home')
    else:
        form = SignUpForm()            
        return render(request, 'register.html', {'form':form})
    
    return render(request, 'register.html', {'form':form})

def user_task(request, pk):
    if request.user.is_authenticated:
        user_task = Task.objects.get(id=pk)
        return render(request, 'task.html', {'user_task':user_task})
    else:
        messages.success(request, "You Must Be Logged In!")
        return redirect('home')
    

def delete_task(request, pk):
    if request.user.is_authenticated:
        delete_it = Task.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Task Deleted Successfully!")
        return redirect('home')
    else:
        messages.success(request, "You Must Be Logged In!")
        return redirect('home')


def add_task(request):
    form = AddTaskForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_task = form.save()
                messages.success(request, "New Task Added!")
                return redirect('home')
        return render(request, 'add_task.html', {'form':form})
    else:
        messages.success(request, "You Must Be Logged In!")
        return redirect('home')
    


def update_task(request, pk):
    if request.user.is_authenticated:
        current_task = Task.objects.get(id=pk)
        form = UpdateTaskForm(request.POST or None, instance=current_task)
        if form.is_valid():
            form.save()
            messages.success(request, "Task Updated Successfully!")
            return redirect('home')
        return render(request, 'update_task.html', {'form':form})
    else:
        messages.success(request, "You Must Be Logged In!")
        return redirect('home')
    



from django.shortcuts import render, redirect
from .models import Todo
from .forms import Todo_creation_form, Login_form
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


def todo_list(request):
   todos= Todo.objects.all()
   query=request.GET.get('q', '')
   if query:
      todos=Todo.objects.filter(title__icontains=query)
   context={'todos':todos}
   return render(request, 'base/todo_list.html', context)   


@login_required(login_url='login')
def todo_create(request):
   form=Todo_creation_form()
   if request.method=='POST':
      form =Todo_creation_form(request.POST, request.FILES)
      if form.is_valid():
         form.save()
         return redirect('home')
   context={'form':form}
   return render(request, 'base/todo_forms.html', context)


#@login_required(login_url='login')
def todo_details(request, pk):
   todo= Todo.objects.get(pk=pk)
   '''if todo.is_valid():
      todo.save()
      return redirect('create')'''
   context={'todo':todo}
   return render(request, 'base/todo_details.html', context)


def todo_update(request, pk):
   todo=Todo.objects.get(pk=pk)
   form=Todo_creation_form(instance=todo)
   if request.method=='POST':
      form=Todo_creation_form(request.POST, request.FILES, instance=todo)
      if form.is_valid():
         form.save()
         return redirect('home')
   context={'form':form}
   return render(request, 'base/todo_forms.html', context)

#@login_required(login_url='login')
def delete_todo(request, pk):
   todo=Todo.objects.get( pk=pk)
   #form= Todo_creation_form(request.GET, request.FILES)
   if request.method=='POST':
     todo.delete()
     return redirect('home')
   context={'todo':todo}
   return render(request, 'base/confirm_delete.html', context)

def singup_view(request):
   form=UserCreationForm()
   if request.method== 'POST':
      form= Todo_creation_form(request.POST)
      if form.is_valid():
         form.save()
         return redirect('login')
      
   context={'form':form}
   return render(request, 'base/singup.html', context)


def login_view(request):
   form=Login_form()
   if request.method == 'POST':
      form= Login_form(request.POST)
      if form.is_valid():
         username= form.cleaned_data['username']
         password= form.cleaned_data['password']
         user= authenticate(username=username, password=password)
         if user is not None:
            login(request, user)
            return redirect('home')
   
   context={'form':form}
   return render(request, 'base/login.html', context)

def logout_view(request):
   logout(request)
   return redirect('login')
   
# Create your views here.

from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib import messages
from django.contrib.auth import login           #Libreria para autenticar a los usuarios existentes
from django.contrib.auth import logout
from django.contrib.auth import authenticate    #Libreria para verificar si un usuario existe

from django.contrib.auth.models import User

from .forms import RegisterForm

from products.models import Product


def index(request):

  products = Product.objects.all().order_by('-id')

  return render(request, 'index.html', {
    'message': 'Listado de productos',
    'title': 'Productos',
    'products': products,
  })


def login_view(request):                        #Se le cambia el nombre a la funcion para no tener conflictos con libreria
  
  if request.user.is_authenticated:
    return redirect('index')
  
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username, password=password)
    if user:
      login(request, user)                      
      messages.success(request, 'Bienvenido {}'.format(user.username))
      return redirect('index')                  #Si el login fue exitoso se redirige a la pagina de index
    else:
      messages.error(request, 'Usuario o contraseñas no válidos')

  return render(request, 'usuarios/login.html', {

  })


def logout_view(request):
  logout(request)
  messages.success(request, 'Sesión cerrada exitosamente')
  return redirect('login')


def register(request):

  if request.user.is_authenticated:
    return redirect('index')

  form = RegisterForm(request.POST or None)     #Se envia el formulario con los datos del cliente o en su defecto vacio

  if request.method == 'POST' and form.is_valid():    

    user = form.save()
    if user:
      login(request, user)
      messages.success(request, 'Usuario creado exitosamente')
      return redirect('index')


  return render(request, 'usuarios/register.html' ,{
    'form':form
  })
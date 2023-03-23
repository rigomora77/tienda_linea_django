from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib import messages
from django.contrib.auth import authenticate    #Libreria para verificar si un usuario existe
from django.contrib.auth import login           #Libreria para autenticar a los usuarios existentes
from django.contrib.auth import logout

def index(request):
  return render(request, 'index.html', {
    'message': 'Listado de productos',
    'title': 'Productos',
    'products': [
      {'title': 'Playera','price': 5,'stock': True},
      {'title': 'Camisa','price': 7,'stock': True},
      {'title': 'Mochila','price': 20,'stock': False},
      {'title': 'Laptop','price': 500,'stock': False},
    ]
  })


def login_view(request):                        #Se le cambia el nombre a la funcion para no tener conflictos con libreria
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

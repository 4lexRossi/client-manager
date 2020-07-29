from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def login(request):
  return render(request, "login.html")

def submit_login(request):
  if request.POST:
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user:
      login(request, user)
      return redirect("index")
    else:
      messages.error(request, "Usuário/Senha inválidos. Tente novamente")
  return redirect("login")
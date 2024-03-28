from django.shortcuts import render
from django.shortcuts import redirect
from .models import Lanche
from .forms import LancheForm, VendedorForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as login_django
# Create your views here.


def index(request):
    return render(request, 'index.html')


def cadastrar(request):
    if request.user.is_authenticated:
        return render(request, 'cadastrar.html')
    else:
        return render(request, 'login.html')


def home(request):
    lanches = Lanche.objects.all()
    return render(request, "index.html", {"lanches": lanches})


def cadastrar_vendedor(request):
    return render(request, 'cadastrar_vendedor.html')


def salvar(request):
    if request.method == 'POST':
        form = LancheForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = LancheForm()

    lanches = Lanche.objects.all()
    return render(request, 'cadastro.html', {'form': form, 'lanches': lanches})


def salvar_vendedor(request):
    if request.method == 'POST':
        form = VendedorForm(request.POST, request.FILES)
        if form.is_valid():
            username = request.POST.get('nome_vendedor')
            email = request.POST.get('email')
            senha = request.POST.get('senha')
            user = User.objects.create_user(
                username=username, email=email, password=senha)
            user.save()
            form.save()
            return redirect('login')
    else:
        form = VendedorForm()

    vendedores = cadastrar_vendedor().objects.all()
    return render(request, 'cadastro_vendedor.html', {'form': form, 'cadastro_vendedor': cadastrar_vendedor})


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        user = authenticate(username=username, password=senha)
        if user:
            login_django(request, user)
            return render(request, 'cadastrar.html')
        else:
            return render(request, 'login.html')


def deslogar(request):
    logout(request)
    return render(request, 'login.html')


'''
def slv_vendedor(request):

    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
       # contato1 = request.POST.get('contato')
        user = User.objects.create_user(
            username=username, email=email, password=senha)
        user.save()
        return redirect('login')
'''

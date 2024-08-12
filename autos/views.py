from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import AutoForm, RegistroForm, ComentarioForm
from .models import Auto, Comentario
from django.urls import reverse_lazy

@user_passes_test(lambda u: u.is_staff)
def eliminar_comentario(request, comentario_id):
    comentario = get_object_or_404(Comentario, id=comentario_id)
    comentario.delete()
    return redirect('index')

def index(request):
    if request.method == 'POST' and request.user.is_authenticated:
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.usuario = request.user
            comentario.save()
            return redirect('index')
    else:
        form = ComentarioForm()

    comentarios = Comentario.objects.all().order_by('-fecha_creacion')
    return render(request, 'autos/index.html', {'form': form, 'comentarios': comentarios})

class CustomLoginView(LoginView):
    template_name = 'autos/login.html'
    success_url = reverse_lazy('index')

def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('autos_list')
    else:
        form = RegistroForm()
    return render(request, 'autos/registro.html', {'form': form})

def lista_autos(request):
    autos = Auto.objects.all()  
    return render(request, 'autos/lista_autos.html', {'autos': autos})

def detalle_auto(request, auto_id):
    auto = get_object_or_404(Auto, pk=auto_id)
    return render(request, 'autos/detalle_auto.html', {'auto': auto})

@login_required
def crear_auto(request):
    if request.method == 'POST':
        form = AutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('autos_list')  
    else:
        form = AutoForm()
    return render(request, 'autos/crear_auto.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('index')



@login_required
@user_passes_test(lambda u: u.is_staff)
def eliminar_auto(request, auto_id):
    auto = get_object_or_404(Auto, id=auto_id)
    auto.delete()
    return redirect('autos_list')

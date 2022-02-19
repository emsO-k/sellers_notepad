from django.db import IntegrityError
from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from .models import Client, Task
from .forms import TaskForm, ClientForm
from .mailer import send_email
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


@login_required
def home(request):
    tasks = []
    for client in Client.objects.filter(created_by=request.user):
        pending_tasks = Task.objects.filter(created_by=request.user,
                                            client=client.id, completed_date__isnull=True).count()
        completed_tasks = Task.objects.filter(created_by=request.user,
                                              client=client.id, completed_date__isnull=False).count()
        tasks.append({"client": client,
                     "pending": pending_tasks, "completed": completed_tasks})
        tasks = sorted(tasks, key=lambda k: k["pending"], reverse=True)
    return render(request, "taskapp/home.html", {"tasks": tasks})


@login_required
def client_details(request, client_id):
    client = get_object_or_404(Client, pk=client_id, created_by=request.user)
    tasks = Task.objects.filter(created_by=request.user, client=client.id).order_by(
        "completed_date")
    return render(request, "taskapp/details.html", {"client": client, "tasks": tasks})


@login_required
def newtask(request):
    if request.method == 'GET':
        return render(request, "taskapp/newtask.html", {"taskForm": TaskForm()})
    else:
        form = TaskForm(request.POST)
        if form.is_valid():
            if form.cleaned_data["client"] is None:
                new_client = Client(name=form.cleaned_data["new_client"])
                new_client.created_by = request.user
                new_client.save()
                form.instance.client = new_client
            new_task = form.save(commit=False)
            new_task.created_by = request.user
            new_task.save()
            try:
                send_email(
                    f'{new_task.client.name} - {new_task.description[:20]}....', new_task.description, "siw6epMoV@protonmail.com")
            except:
                print("No se pudo enviar el correo")
            return redirect('all_pending_tasks')
        else:
            raise ValueError


@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, created_by=request.user)
    if request.method == "POST":
        task.completed_date = timezone.now()
        task.save()
        return redirect("all_pending_tasks")


@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, created_by=request.user)
    if request.method == 'GET':
        form = TaskForm(instance=task)
        return render(request, "taskapp/newtask.html", {"taskForm": form, "editMode": True, "task_id": task.id})
    else:
        form = TaskForm(request.POST, instance=task)
        form.save()
        return redirect('client_details', client_id=task.client.id)


@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, created_by=request.user)
    if request.method == 'POST':
        client_id = task.client.id
        task.delete()
        return redirect('client_details', client_id=client_id)


@login_required
def all_pending_tasks(request):
    tasks = Task.objects.filter(
        completed_date__isnull=True, created_by=request.user)
    return render(request, "taskapp/details.html", {"tasks": tasks, "title": "Pendientes"})


@login_required
def all_completed_tasks(request):
    tasks = Task.objects.filter(created_by=request.user,
                                completed_date__isnull=False).order_by("completed_date")
    return render(request, "taskapp/details.html", {"tasks": tasks, "title": "Completadas"})


@login_required
def view_clients(request):
    clients = Client.objects.filter(created_by=request.user).order_by("name")
    return render(request, "taskapp/clients.html", {"clients": clients})


@login_required
def edit_client(request, client_id):
    client = get_object_or_404(Client, pk=client_id, created_by=request.user)
    if request.method == 'GET':
        form = ClientForm(instance=client)
        return render(request, "taskapp/client_details.html", {"clientForm": form, "client_id": client.id})
    else:
        form = ClientForm(request.POST, instance=client)
        form.save()
        return redirect('view_clients')


@login_required
def delete_client(request, client_id):
    client = get_object_or_404(Client, pk=client_id, created_by=request.user)
    if request.method == 'POST':
        client.delete()
        return redirect('view_clients')


def signupuser(request):
    if request.method == "GET":
        return render(request, 'taskapp/signup.html', {'form': UserCreationForm()})
    else:
        # Create a new user
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)  # Loguea al usuario
                # Lo redirige a otra pagina para que no se quede en el sign up, es importante sabe que ya quedó logueado luego del signup
                return redirect('home')
            except IntegrityError:
                return render(request, 'taskapp/signup.html', {'form': UserCreationForm(), 'error': "Username has already been taken"})

        else:
            # tell the user the passwords don't match
            return render(request, 'taskapp/signup.html', {'form': UserCreationForm(), 'error': "Passwords did not match"})


def login_user(request):
    if request.method == "GET":
        return render(request, 'taskapp/login.html', {'form': AuthenticationForm()})
    else:
        # Create a new user
        user = authenticate(request,
                            username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'taskapp/login.html',
                          {'form': AuthenticationForm(), 'error': "Usuario o contraseña incorrecta"})
        else:
            login(request, user)
            return redirect('home')


@login_required
def logout_user(request):
    print(request.method)
    if request.method == "POST":
        """
        Se usa POST para los logouts porque si fuera GET,
        los browsers hacen pre-fetch de los GETs,
        con lo cual el usuario sería deslogueado automaticamente
        por culpa del browser. Por eso hay que usar POST.
        """
        logout(request)
        return redirect("home")

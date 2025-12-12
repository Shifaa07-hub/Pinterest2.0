from django.shortcuts import render
from .forms import PinterestForm, UserRegistrationForm
from .models import Pinterest
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.
def homepage(request):
    query = request.GET.get('q')
    pins = Pinterest.objects.all()

    if query:
        pins = pins.filter(text__icontains = query)

    return render(request, 'home.html', {'pins':pins})

@login_required
def createpin(request):
    if request.method == "POST":
        form = PinterestForm(request.POST, request.FILES)
        if form.is_valid():
            pin = form.save(commit=False)
            pin.user = request.user
            pin.save()
            return redirect('home')
    else:
        form = PinterestForm()
    return render(request, 'create.html', {'form':form})
    
@login_required
def editpin(request, pin_id):
    pin = get_object_or_404(Pinterest, pk = pin_id)
    if request.method == "POST":
        form = PinterestForm(request.POST, request.FILES, instance = pin)
        if form.is_valid():
            pin = form.save(commit=False)
            pin.user = request.user
            pin.save()
            return redirect('home')
    else:
        form = PinterestForm()
    return render(request, 'create.html', {'form':form})

@login_required
def deletepin(request, pin_id):
    pin = get_object_or_404(Pinterest, pk = pin_id, user = request.user)
    if request.method == "POST":
        pin.delete()
        return redirect('home')
    return render(request, 'delete.html', {'pin':pin})

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid:
            user = form.save(commit = False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return redirect('home')

    else:
        form = UserRegistrationForm()

    return render(request, 'registration/register.html', {'form':form})

@login_required
def profile(request):
    query = request.GET.get('q')
    user = request.user
    pins = Pinterest.objects.filter(user = user)

    if query:
        pins = pins.filter(text__icontains = query)

    return render(request, 'profile.html', {'user': user, 'pins':pins})

def search(request):
    query = request.GET.get('q', '')
    pins = Pinterest.objects.none()

    if query:
        pins = Pinterest.objects.filter(text__icontains = query)
    
    return render(request, 'search.html', {'query':query, 'pins':pins})
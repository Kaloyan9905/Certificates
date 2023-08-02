from django.shortcuts import render, redirect

from fruitipediaApp.web.forms import ProfileCreateForm, FruitCreateForm, FruitEditForm, FruitDeleteForm, \
    ProfileEditForm, ProfileDeleteForm
from fruitipediaApp.web.models import Profile, Fruit


# Create your views here.

def index(request):
    profile = Profile.objects.all()

    context = {
        'profile': profile,
    }

    return render(request, 'index.html', context)


def dashboard(request):
    fruits = Fruit.objects.all()

    context = {
        'fruits': fruits,
        'profile': Profile.objects.get(),
    }

    return render(request, 'dashboard.html', context)


def create_fruit(request):
    if request.method == 'GET':
        form = FruitCreateForm()
    else:
        form = FruitCreateForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('dashboard')

    context = {
        'form': form,
        'profile': Profile.objects.get(),
    }

    return render(request, 'create-fruit.html', context)


def details_fruit(request, fruit_id):
    fruit = Fruit.objects.filter(pk=fruit_id).get()

    context = {
        'fruit': fruit,
        'profile': Profile.objects.get(),
    }

    return render(request, 'details-fruit.html', context)


def edit_fruit(request, fruit_id):
    fruit = Fruit.objects.filter(pk=fruit_id).get()

    if request.method == 'GET':
        form = FruitEditForm(instance=fruit)
    else:
        form = FruitEditForm(request.POST, instance=fruit)

        if form.is_valid():
            form.save()

            return redirect('dashboard')

    context = {
        'form': form,
        'fruit': fruit,
        'profile': Profile.objects.get(),
    }

    return render(request, 'edit-fruit.html', context)


def delete_fruit(request, fruit_id):
    fruit = Fruit.objects.filter(pk=fruit_id).get()

    if request.method == 'GET':
        form = FruitDeleteForm(instance=fruit)
    else:
        form = FruitDeleteForm(request.POST, instance=fruit)

        if form.is_valid():
            fruit.delete()

            return redirect('dashboard')

    context = {
        'form': form,
        'fruit': fruit,
        'profile': Profile.objects.get(),
    }

    return render(request, 'delete-fruit.html', context)


def create_profile(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('dashboard')

    context = {
        'form': form,
    }

    return render(request, 'create-profile.html', context)


def details_profile(request):
    profile = Profile.objects.get()
    posts = Fruit.objects.count()

    context = {
        'profile': profile,
        'posts': posts,
    }

    return render(request, 'details-profile.html', context)


def edit_profile(request):
    profile = Profile.objects.get()

    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()

            return redirect('details profile')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'edit-profile.html', context)


def delete_profile(request):
    profile = Profile.objects.get()

    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)

        if form.is_valid():
            profile.delete()
            Fruit.objects.all().delete()

            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'delete-profile.html', context)

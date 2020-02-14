from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Vehicle, Deal
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import VehicleForm, DealForm
from allauth.account.views import LoginView


def index(request):
    return render(request, 'transporter_index.html')


def add_vehicle(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES)
        form.save()
        return HttpResponseRedirect(reverse('vehicle-list'))
    form = VehicleForm(initial={'transporter': request.user.profile.id})
    return render(request, 'add_vehicle.html', {'form': form})


def vehicle_list(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'vehicle_list.html', {'vehicles': vehicles})


def edit_vehicle(request, id):
    vehicle = Vehicle.objects.get(id=id)
    return render(request, 'edit_vehicle.html', {'vehicle': vehicle})


def update_vehicle(request, id):
    vehicle = Vehicle.objects.get(id=id)
    form = VehicleForm(request.POST, instance=vehicle)
    if form.is_valid():
        form.save()
        return redirect("/vehicle")
    return render(request, 'edit_vehicle.html', {'vehicle': vehicle})


def delete_vehicle(request, id):
    vehicle = Vehicle.objects.get(id=id)
    vehicle.delete()
    return redirect("/vehicle")



def create_deal(request):
    if request.method == 'POST':
        form = DealForm(request.POST)
        # import pdb;pdb.set_trace()
        form.save()
        return HttpResponseRedirect(reverse('deal-list'))

    form = DealForm()
    return render(request, 'create_deal.html', {'form': form})


def deal_list(request):
    deals = Deal.objects.all()
    return render(request, 'deal_list.html', {'deals': deals})

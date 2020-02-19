from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect
from .models import Vehicle, Deal
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import VehicleForm, DealForm
from allauth.account.views import LoginView


def index(request):
    queryset = request.GET.get('start city')
    queryset1 = request.GET.get('end city')
    queryset2 = request.GET.get('start date')
    queryset3 = request.GET.get('end date')
    if queryset and queryset1:
        deal_lists = Deal.objects.filter(Q(start_city__icontains=queryset), Q(end_city__icontains=queryset1))
        context = {'deal_lists': deal_lists}
        return render(request, 'transporter_index.html', context)
    # if queryset2 and queryset3:
    #     deal_lists = Deal.objects.filter(Q(start_Date=queryset2), Q(end_date=queryset3))
    #     context = {'deal_lists': deal_lists}
    #     return render(request, 'transporter_index.html', context)
    else:
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


def update_vehicle(request, id):
    vehicle = Vehicle.objects.get(id=id)

    if request.method == 'POST':
        form = VehicleForm(request.POST, instance=vehicle)
        form.save()
        return HttpResponseRedirect(reverse('vehicle-list'))
    form = VehicleForm(instance=vehicle)
    return render(request, 'edit_vehicle.html', {'form': form})


def delete_vehicle(request, id):
    vehicle = Vehicle.objects.get(id=id)
    if request.method == 'POST':
        vehicle.delete()
        return redirect('vehicle-list')
    return render(request, 'delete_vehicle.html', {'vehicle': vehicle})


def view_deal(request, deal_id):
    deal = Deal.objects.get(deal_id=deal_id)
    return render(request, 'view_deal.html', {'deal': deal})


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


def delete_deal(request, deal_id):
    deal = Deal.objects.get(deal_id=deal_id)
    if request.method == 'POST':
        deal.delete()
        return redirect('deal-list')
    return render(request, 'delete_vehicle.html', {'deal': deal})


def edit_deal(request, deal_id):
    deal = Deal.objects.get(deal_id=deal_id)
    if request.method == 'POST':
        form = DealForm(request.POST, instance=deal)
        form.save()
        return HttpResponseRedirect(reverse('deal-list'))
    form = DealForm(instance=deal)
    return render(request, 'edit_deal.html', {'form': form})


def view_image(request, id):
    vehicle = Vehicle.objects.get(id=id)
    return render(request, 'view_image.html', {'vehicle': vehicle})
# def search_deal_by_date(request, start_Date, end_date):
#     deal_lists = Deal.objects.filter(Q(start_Date=start_Date),Q(end_date=end_date))
#     context={'deal_lists': deal_lists}
#     return render(request, 'transporter_index.html')

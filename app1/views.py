from django.shortcuts import render, redirect
from .models import Policy, Client, Claim
from .forms import PolicyForm, ClientForm, ClaimForm

# Create your views here.

def policy_list(request):
    policies = Policy.objects.all()
    return render(request, 'policy_list.html', {'policies': policies})


def create_policy(request):
    if request.method == "POST":
        form = PolicyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('policy_list')
    else:
        form = PolicyForm()
    return render(request, 'create_policy.html', {'form':form})

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'client_list.html', {'clients':clients})

def create_client(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'create_client.html', {'form':form})


def claims_list(request):
    claims = Claim.objects.all()
    return render(request, 'claim_list.html', {'claims': claims})

def create_claim(request):
    if request.method == "POST":
        form = ClaimForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ClaimForm()
    return render(request, 'create_claim.html', {'form':form})